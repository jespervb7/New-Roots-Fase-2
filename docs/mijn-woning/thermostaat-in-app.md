---
title: Thermostaat bedienen met een app
description: Twee manieren om je Danfoss Icon2-thermostaten via je telefoon te bedienen, en wat de benodigde hardware kost.
status: new
tags:
  - Verwarming
revision_date: "11 november 2026"
---

# Thermostaat bedienen met een app

Je Danfoss Icon2-thermostaten (vloerverwarming) kun je met een app op je telefoon bedienen. Daarvoor heb je extra hardware nodig: óf het officiële Danfoss Ally Gateway-kastje (ongeveer € 170), óf een eigen Home Assistant-systeem met een Zigbee-stick (ongeveer € 45 tot € 225).

!!! tip "Welke past bij jou?"

    - **Wil je het simpel en officieel?** Kies [Danfoss Ally](#optie-1-danfoss-ally-officieel). Kastje aansluiten, app installeren, klaar.
    - **Wil je meer mogelijkheden of heb je al een slim huis?** Kies [Home Assistant](#optie-2-home-assistant-met-zigbee). Meer werk om in te stellen, maar alles blijft lokaal en je kunt het combineren met andere apparaten.

## Hoe werkt het?

In de meterkast (of bij de verdeler van de vloerverwarming) hangt de **Icon2-hoofdregelaar**. Die praat draadloos met de thermostaten in je kamers via **Zigbee**, een draadloze taal voor slimme apparaten. Je telefoon spreekt geen Zigbee. Daarom heb je een "vertaler" nodig die de regelaar met je thuisnetwerk verbindt. Dat is precies wat beide opties hieronder doen.

!!! warning "Kies één van de twee"

    De hoofdregelaar kan maar met één Zigbee-systeem tegelijk verbonden zijn. Je gebruikt dus Danfoss Ally **óf** Home Assistant, niet allebei.

## Vergelijking

| | Danfoss Ally (officieel) | Home Assistant + Zigbee |
| --- | --- | --- |
| **Hardware** | Danfoss Ally Gateway | Zigbee-stick (bijv. Home Assistant Connect ZBT-2) + een apparaat waarop Home Assistant draait |
| **Kosten** | ± € 170 | ± € 45 als je al een Home Assistant-systeem hebt, anders ± € 225 |
| **App** | Danfoss Ally (gratis) | Home Assistant (gratis) |
| **Instellen** | Makkelijk, stap voor stap in de app | Technischer, vraagt wat uitzoekwerk |
| **Werkt zonder internet** | Nee, via de cloud van Danfoss | Ja, alles blijft in huis (op afstand bedienen vraagt wel extra instellen) |
| **Ondersteuning** | Officieel door Danfoss | Door de community, niet door Danfoss |
| **Combineren met andere apparaten** | Beperkt | Ja, met vrijwel alles (lampen, zonnepanelen, enz.) |

De prijzen zijn indicaties van november 2026. Controleer de actuele prijs vlak voor je iets koopt.

## Optie 1: Danfoss Ally (officieel)

Dit is de manier die Danfoss zelf aanbiedt.

**Wat heb je nodig?**

- De **Danfoss Ally Gateway** (artikelnummer `014G2400`). Kost ongeveer **€ 170**, bijvoorbeeld bij [Amazon.nl](https://www.amazon.nl/dp/B08MZ6WJZK){ target=_blank }.
- Een vrije aansluiting op je internetrouter: de gateway gaat met een netwerkkabel aan je router.
- De gratis **Danfoss Ally**-app (iPhone en Android).

**Zo koppel je het**

1. Sluit de gateway met de netwerkkabel aan op je router en steek de stekker in het stopcontact.
2. Installeer de Danfoss Ally-app en maak een account aan.
3. Kies in de app voor *Toestel toevoegen* → *Danfoss Ally Gateway* en volg de stappen.
4. Voeg daarna de Icon2-hoofdregelaar toe aan de gateway (in de app: open de gateway en kies *apparaat toevoegen*).

De precieze stappen staan in de [officiële Nederlandse instructie van Danfoss](https://assets.danfoss.com/documents/latest/374241/AU484256488237nl-NL0101.pdf){ target=_blank }. Meer informatie vind je op de [Icon2-supportpagina van Danfoss](https://www.danfoss.com/nl-nl/products/dhs/hydronic-underfloor-heating/products/danfoss-icon2/danfoss-icon2-support/){ target=_blank }.

!!! note "Handig om te weten"

    Zodra de hoofdregelaar met de gateway verbonden is, krijgt hij automatisch de nieuwste software-updates van Danfoss.

## Optie 2: Home Assistant met Zigbee

[Home Assistant](https://www.home-assistant.io/){ target=_blank } is gratis software waarmee je al je slimme apparaten in één app bedient. De Icon2 werkt volgens de Zigbee 3.0-standaard, dus Home Assistant kan er direct mee praten zonder de cloud van Danfoss.

!!! info "Ervaring van een bewoner"

    Een bewoner gebruikt deze opstelling zelf: Home Assistant met een Home Assistant Connect ZBT-2-stick en de ingebouwde Zigbee-integratie ZHA. Dit werkt, maar is niet officieel ondersteund door Danfoss. Volgens [gebruikers op het Home Assistant-forum](https://community.home-assistant.io/t/zigbee-integration-of-danfoss-icon2-main-controller/675000){ target=_blank } worden de meeste functies goed herkend, maar niet allemaal.

**Wat heb je nodig?**

| Onderdeel | Waarvoor | Prijs (ca.) |
| --- | --- | --- |
| [Home Assistant Connect ZBT-2](https://www.home-assistant.io/connect/zbt-2/){ target=_blank } | De Zigbee-stick: maakt contact met de hoofdregelaar | € 45 |
| [Home Assistant Green](https://www.home-assistant.io/green/){ target=_blank } | Klein kastje waarop Home Assistant draait. Niet nodig als je Home Assistant al op een eigen computer of Raspberry Pi hebt draaien | € 179 |
| Home Assistant-app | Bedienen vanaf je telefoon | Gratis |

Prijsbronnen: [Domadoo](https://www.domadoo.fr/nl/zigbee-dongle/8542-nabu-casa-home-assistant-connect-zbt-2-zigbee-of-usb-adapter-matter-thread-0860011789741.html){ target=_blank } (ZBT-2) en [Nabu Casa](https://www.nabucasa.com/news/2026-01-08-green-pricing-change/){ target=_blank } (Green, adviesprijs sinds januari 2026).

**Zo koppel je het (globaal)**

1. Installeer Home Assistant (op de Green is het al voorgeïnstalleerd) en sluit de ZBT-2-stick aan.
2. Voeg in Home Assistant de integratie **Zigbee Home Automation** (ZHA) toe en kies de ZBT-2 als Zigbee-stick.
3. Zet in ZHA *apparaten toevoegen* aan en zet de Icon2-hoofdregelaar in koppelmodus (zie de [handleiding van de Icon2](https://www.danfoss.com/nl-nl/products/dhs/hydronic-underfloor-heating/products/danfoss-icon2/danfoss-icon2-support/){ target=_blank }).
4. De hoofdregelaar en de thermostaten per kamer verschijnen als apparaten in Home Assistant.

!!! tip "Alternatief: Zigbee2MQTT"

    In plaats van ZHA kun je ook [Zigbee2MQTT](https://www.zigbee2mqtt.io/devices/Icon2.html){ target=_blank } gebruiken, dat de Icon2 ook ondersteunt. Dit vraagt meer technische kennis om op te zetten.

## FAQ

??? question "Heb ik internet nodig om mijn thermostaat te gebruiken?"

    Nee. De thermostaten in je kamers blijven gewoon werken zonder app of internet. De app is een extra: je kunt dan ook vanaf de bank of van buitenshuis de temperatuur aanpassen.

??? question "Kan ik later overstappen van Danfoss Ally naar Home Assistant (of andersom)?"

    Ja. Je moet de hoofdregelaar dan loskoppelen van het ene systeem en opnieuw koppelen aan het andere. Hoe je de koppeling verbreekt, staat in de [handleiding van de Icon2](https://www.danfoss.com/nl-nl/products/dhs/hydronic-underfloor-heating/products/danfoss-icon2/danfoss-icon2-support/){ target=_blank }.

??? question "Werkt dit ook met Google Home, Apple Home of Alexa?"

    Met Home Assistant kun je je thermostaten doorgeven aan Google Home, Apple Home of Alexa. Voor Danfoss Ally kun je op de [Ally-pagina van Danfoss](https://www.danfoss.com/nl-nl/products/dhs/smart-heating/solutions/danfoss-ally/){ target=_blank } nagaan welke koppelingen er zijn.

??? question "Ik kom er niet uit. Wie kan me helpen?"

    Voor Danfoss Ally kun je terecht bij de [support van Danfoss](https://www.danfoss.com/nl-nl/products/dhs/hydronic-underfloor-heating/products/danfoss-icon2/danfoss-icon2-support/){ target=_blank }. Voor Home Assistant is het [Home Assistant-forum](https://community.home-assistant.io/){ target=_blank } de beste plek. Weet je een tip die hier mist? [Deel het!](https://github.com/jespervb7/New-Roots-Fase-2/issues/new?template=1-nieuwe-informatie.yml){ target=_blank }
