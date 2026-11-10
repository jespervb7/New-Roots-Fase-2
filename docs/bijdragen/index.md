---
title: Hoe kan ik bijdragen?
description: Zo help je mee om deze site aan te vullen en actueel te houden, met of zonder technische kennis.
status: new
tags:
  - Bijdragen
revision_date: "10 november 2026"
---

# Hoe kan ik bijdragen?

Deze site wordt gemaakt door en voor bewoners van New Roots Fase 2. Hoe meer mensen hun kennis delen, hoe nuttiger hij wordt. Weet je iets wat je buren ook moeten weten? Staat er iets niet meer klopt? Help dan mee.

!!! tip "Geen technische kennis nodig"

    Je hoeft niet te kunnen programmeren. Met optie 1 hieronder stuur je gewoon een bericht, en wij zetten het op de site.

## Wat kun je bijdragen?

- **Handleidingen** voor apparaten en installaties in het appartement, zoals de WTW-unit, de thermostaat of de intercom.
- **Contactgegevens** van de VvE, de beheerder, aannemers en leveranciers.
- **Handige tips**, bijvoorbeeld over parkeren, afval, sloten of de fietsenstalling.
- **Correcties**: verouderde informatie, kapotte links of tikfouten.
- **Ideeën** voor nieuwe pagina's of onderwerpen.

## Optie 1: Een idee of correctie doorgeven (makkelijkst)

Je hebt hiervoor een gratis [GitHub-account](https://github.com/signup) nodig.

1. Kies wat je wilt doorgeven:

    [:material-lightbulb-outline: Nieuwe informatie of idee](https://github.com/jespervb7/New-Roots-Fase-2/issues/new?template=1-nieuwe-informatie.yml){ .md-button .md-button--primary target=_blank }
    [:material-pencil-outline: Correctie melden](https://github.com/jespervb7/New-Roots-Fase-2/issues/new?template=2-correctie.yml){ .md-button target=_blank }

2. Log in als dat gevraagd wordt.
3. Vul het formulier in. Niet alles hoeft compleet te zijn. Foto's of screenshots kun je in een tekstvak slepen.
4. Klik op **Create**.

Daarna verwerken wij jouw bijdrage op de site.

## Optie 2: Zelf een pagina aanpassen via de website van GitHub

Wil je de tekst zelf aanpassen? Dat kan rechtstreeks in je browser.

1. Ga op deze site naar de pagina die je wilt aanpassen en klik rechtsboven de titel op het potloodje :material-file-edit-outline:. Je komt dan direct in de editor van die pagina op GitHub.
2. Log in als dat gevraagd wordt. De eerste keer vraagt GitHub om een eigen kopie (*fork*) te maken; klik op **Fork this repository**.
3. Pas de tekst aan. De pagina's zijn geschreven in [Markdown](https://zensical.org/docs/authoring/markdown/), een eenvoudige opmaaktaal. Kijk bij twijfel hoe andere pagina's het doen.

    Zet bovenaan bij `revision_date` de datum van vandaag, bijvoorbeeld `revision_date: "10 november 2026"`. Die datum staat onderaan de pagina als *Laatst geüpdatet*. Vergeet je het? Dan zie je dat bij je pull request en kun je het alsnog aanpassen.
4. Klik op **Commit changes…**, beschrijf kort wat je hebt veranderd en kies **Propose changes**.
5. Klik daarna op **Create pull request**.

Wij bekijken je wijziging en zetten hem online zodra hij is goedgekeurd.

??? info "Een nieuwe pagina toevoegen"

    Klik in de map `docs` op **Add file → Create new file** en geef het bestand een naam in kleine letters met streepjes, bijvoorbeeld `afval-scheiden.md`. Vermeld in je pull request dat het om een nieuwe pagina gaat. Dan zorgen wij dat hij in het menu komt.

    Wil je de pagina ook onder een onderwerp laten vallen in [Onderwerpen A-Z](../tags.md)? Zet bovenaan bijvoorbeeld:

    ```yaml
    ---
    tags:
      - Afval
    ---
    ```

    Kies een onderwerp dat al bestaat. Een nieuw onderwerp voegen wij toe.

## Optie 3: Lokaal werken (voor gevorderden)

Werk je liever op je eigen computer met een live voorbeeld van de site? Je hebt [Git](https://git-scm.com/) en [uv](https://docs.astral.sh/uv/) nodig.

```sh
git clone https://github.com/jespervb7/New-Roots-Fase-2.git
cd New-Roots-Fase-2
uv sync --group dev
uv run pre-commit install
uv run zensical serve --open
```

De site draait nu op <http://localhost:8000> en ververst automatisch als je een bestand opslaat.

Een paar afspraken:

- Pagina's staan in `docs/`, met een map per tabblad (bijv. `docs/mijn-woning/`). Afbeeldingen voor een pagina zet je in `docs/images/<paginanaam>/`, downloadbare bestanden zoals handleidingen in `docs/assets/`.
- Voeg een nieuwe pagina toe aan `nav` in `zensical.toml`, anders staat hij niet in het menu.
- Controleer je werk met `uv run zensical build --clean --strict`. Deze moet zonder waarschuwingen slagen.
- De pre-commit hook zet bij elke pagina die je wijzigt de datum *Laatst geüpdatet* op vandaag. Past hij een datum aan, dan stopt de commit even: doe `git add` en commit opnieuw.
- Werk in een eigen branch en open een pull request naar `main`.

## Richtlijnen voor goede inhoud

- **Schrijf voor je buren.** Gebruik korte zinnen en concrete stappen, en leg vaktermen uit. Gebruik je een afkorting (zoals VvE of WTW)? Zet de uitleg dan in `includes/afkortingen.md`; dan krijgt de afkorting op de hele site automatisch een uitleg als je eroverheen gaat.
- **Noem je bron.** Link naar de officiële handleiding, de VvE-mail of de website van de gemeente. Sla een kopie op in `docs/assets/` als een handleiding offline kan gaan.
- **Wees eerlijk over onzekerheid.** Heb je iets zelf uitgezocht maar is het niet officieel bevestigd? Zeg dat dan.
- **Voeg screenshots of foto's toe** als die helpen, en zorg dat er geen persoonlijke spullen of mensen op staan.

!!! warning "Deze site is openbaar"

    Iedereen op internet kan deze site lezen. Plaats daarom **nooit**:

    - namen, telefoonnummers of e-mailadressen van individuele bewoners;
    - toegangscodes, alarmcodes, wifi-wachtwoorden of sleutelnummers;
    - privélinks naar documenten of dashboards.

    Contactgegevens van organisaties, zoals de VvE-mailbox, de beheerder of aannemers, mogen wel.
