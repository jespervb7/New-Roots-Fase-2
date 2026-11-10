"""Keep the "Laatst geüpdatet" date of each page correct.

Zensical shows "Laatst geüpdatet" at the bottom of a page when its front matter
contains `revision_date`. This script maintains that field.

Commands
--------
update FILE...
    Used by the pre-commit hook. Sets `revision_date` to today for every given
    page that differs from the last commit (HEAD). Pages without changes are
    left alone, so `pre-commit run --all-files` doesn't touch every date.

check --base REF
    Used in CI on pull requests. For every page changed since REF, checks that
    `revision_date` equals the date of the last commit that changed the page.
    Exits with 1 (and GitHub annotations) if a date is missing or wrong.

backfill [DIR]
    One-off helper. Gives every page in DIR (default: docs) that has no
    `revision_date` yet the date of its last commit.

Dates are written in Dutch, e.g. "10 november 2026".
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

MONTHS_NL = [
    "januari", "februari", "maart", "april", "mei", "juni",
    "juli", "augustus", "september", "oktober", "november", "december",
]
FIELD = "revision_date"
# [ \t] instead of \s: an empty "revision_date:" must not swallow the next line.
FIELD_RE = re.compile(rf'^{FIELD}:[ \t]*"?([^"\r\n]*?)"?[ \t]*$', re.MULTILINE)


# --- dates -------------------------------------------------------------------

def format_nl(d: date) -> str:
    return f"{d.day} {MONTHS_NL[d.month - 1]} {d.year}"


def parse_nl(text: str) -> date | None:
    m = re.fullmatch(r"(\d{1,2}) ([a-z]+) (\d{4})", text.strip())
    if not m or m.group(2) not in MONTHS_NL:
        return None
    return date(int(m.group(3)), MONTHS_NL.index(m.group(2)) + 1, int(m.group(1)))


# --- git ---------------------------------------------------------------------

def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, check=True, encoding="utf-8"
    ).stdout.strip()


def last_commit_date(path: str | Path, rev: str = "HEAD") -> date | None:
    # %as = author date (YYYY-MM-DD) in the author's own timezone; this is the
    # day the pre-commit hook ran, and it survives rebases.
    out = git("log", "-1", "--format=%as", rev, "--", str(path))
    return date.fromisoformat(out) if out else None


def changed_since_head(path: Path) -> bool:
    try:
        git("diff", "--quiet", "HEAD", "--", str(path))
        return False
    except subprocess.CalledProcessError:
        return True


# --- front matter ------------------------------------------------------------

def read(path: Path) -> tuple[str, str]:
    raw = path.read_bytes().decode("utf-8")
    newline = "\r\n" if "\r\n" in raw else "\n"
    return raw.replace("\r\n", "\n"), newline


def write(path: Path, text: str, newline: str) -> None:
    path.write_bytes(text.replace("\n", newline).encode("utf-8"))


def split_front_matter(text: str) -> tuple[str | None, str]:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[4:end], text[end:]
    return None, text


def get_date(text: str) -> str | None:
    front, _ = split_front_matter(text)
    if front is None:
        return None
    m = FIELD_RE.search(front)
    return m.group(1) if m else None


def set_date(text: str, value: str) -> str:
    line = f'{FIELD}: "{value}"'
    front, rest = split_front_matter(text)
    if front is None:
        return f"---\n{line}\n---\n\n{text}"
    if FIELD_RE.search(front):
        front = FIELD_RE.sub(line, front, count=1)
    else:
        front = f"{front}\n{line}"
    return f"---\n{front}{rest}"


# --- commands ----------------------------------------------------------------

def cmd_update(files: list[str]) -> int:
    today = format_nl(date.today())
    changed = []
    for name in files:
        path = Path(name)
        if not path.is_file() or not changed_since_head(path):
            continue
        text, nl = read(path)
        if get_date(text) != today:
            write(path, set_date(text, today), nl)
            changed.append(name)
    for name in changed:
        print(f"Laatst geüpdatet -> {today}: {name}")
    # pre-commit stops the commit when a hook changes files; `git add` and
    # commit again to include the new date.
    return 1 if changed else 0


def cmd_check(base: str) -> int:
    merge_base = git("merge-base", base, "HEAD")
    files = git(
        "diff", "--name-only", "--diff-filter=AMR", merge_base, "HEAD", "--", "docs/"
    ).splitlines()
    errors = 0
    for name in (f for f in files if f.endswith(".md")):
        expected = last_commit_date(name)
        text, _ = read(Path(name))
        actual = get_date(text)
        problem = None
        if actual is None:
            problem = f"{FIELD} ontbreekt; verwacht \"{format_nl(expected)}\""
        elif parse_nl(actual) is None:
            problem = f"{FIELD} \"{actual}\" is geen geldige datum (bijv. \"{format_nl(expected)}\")"
        elif parse_nl(actual) != expected:
            problem = (
                f"{FIELD} is \"{actual}\", maar de pagina is voor het laatst "
                f"gewijzigd op \"{format_nl(expected)}\""
            )
        if problem:
            errors += 1
            print(f"::error file={name},title=Laatst geüpdatet klopt niet::{problem}")
        else:
            print(f"ok  {name}  ({actual})")
    if errors:
        print(
            f"\n{errors} pagina('s) met een verkeerde datum. Installeer de pre-commit "
            "hook (`uv run pre-commit install`) of pas de datum aan in de front matter."
        )
    return 1 if errors else 0


def cmd_backfill(directory: str) -> int:
    count = 0
    for path in sorted(p for p in Path(directory).rglob("*") if p.suffix == ".md"):
        text, nl = read(path)
        if get_date(text):  # skip pages that already have a (non-empty) date
            continue
        d = last_commit_date(path)
        if d:
            write(path, set_date(text, format_nl(d)), nl)
            count += 1
            print(f"{format_nl(d)}: {path.as_posix()}")
    print(f"{FIELD} toegevoegd aan {count} pagina('s)")
    return 0


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")  # Dutch characters on Windows consoles
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("update")
    p.add_argument("files", nargs="*")
    p = sub.add_parser("check")
    p.add_argument("--base", required=True, help="e.g. origin/main")
    p = sub.add_parser("backfill")
    p.add_argument("directory", nargs="?", default="docs")
    args = parser.parse_args()

    if args.command == "update":
        return cmd_update(args.files)
    if args.command == "check":
        return cmd_check(args.base)
    return cmd_backfill(args.directory)


if __name__ == "__main__":
    sys.exit(main())
