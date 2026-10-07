---
name: roans-writing-style
description: "Roan Heemstra's personal writing style guide. How to write emails, messages, reports, documentation, and professional text in Roan's voice. Combined EN/NL reference for single-file use."
version: 3.2.0
author: Roan
license: personal
metadata:
  hermes:
    tags: [writing, style, voice, roan, professional, copywriting, en, nl, documentation, reports]
    trigger: "Any task asking to write, draft, rewrite, or format outward-facing text for Roan"
---

# Roan's Writing Style

Ported from `~/.openclaw/workspace/ROANS-HANDWRITING.md`.

Defines exactly how Roan wants text written on his behalf.

## Language Selection

When Roan asks you to write or starts a conversation:
- If he writes in **English** → Use the **English** section below
- If he writes in **Dutch** → Use the **Nederlands** section below
- **Mirror his language** — if he starts the conversation in Dutch, answer in Dutch. No need to ask or wait for explicit "spreek Nederlands".
- If he switches languages mid-conversation, follow his switch for subsequent replies.

---

# Global Rules (All Languages)

## Delivery Format on Chat Platforms

When the text is delivered to Roan through Telegram, Slack, Teams or any other chat platform, put the whole piece in a code block. He copy pastes it straight into the mail, ticket or message.

- Plain text inside the block: no bold, no headings, no bullet formatting, no markdown styling
- One block per message, only the lines that go into the mail
- Your own explanation stays outside the block, two lines maximum
- This applies to every language and every text type, mail, chatbericht, verslag

## Critical Rules

**NO EM DASHES. EVER.** This includes the - regular hyphen `-`, dont use it.
Use:
- comma `,`
- period `.`
- or split into separate sentences
instead

This applies to:
- emails
- reports
- messages
- documentation
- internal notes
- generated examples

## Core Voice

- Direct, not cold
- Professional without sounding corporate
- Concrete over abstract
- Calm and structured
- Explains context when needed
- Avoids filler and generic phrasing
- Practical instead of theoretical

## Rewrite Pattern (Enforced)

When generating text:
1. Identify the actual situation or problem
2. State it directly
3. Add concrete cause and effect
4. Remove generic or reusable sentences
5. Replace vague wording with real impact
6. Prefer operational context over theory

## Universal Writing Rules

- Every sentence must add information
- Avoid repeating the same point differently
- Use realistic examples instead of generic explanation
- Prefer real systems, actions, and outcomes
- Keep technical names exact
- Avoid overexplaining obvious concepts
- Avoid academic filler language

---

# English

Use this section when Roan asks you to write in English.

---

## Communication Style (Emails, Messages, Tickets)

Use this style for:
- Emails
- Support messages
- Tickets
- Follow-ups
- Professional communication
- Short updates
- Requests

### Structure

#### Opening
Use:
- `Hi [Name],`
- `Hello [Name],`

Never:
- `Dear`

First contact:
- "I hope you're doing well"

Follow-ups:
- reference previous communication naturally

#### Body

- Start with the point immediately
- Explain what is needed and why
- Include technical details exactly as-is
- If urgent or blocking: state it clearly
- Each paragraph must have a clear purpose

#### Sign-off

Use:
- `Thank you,`
- `Sincerely,`
- `Best,` (only if informal)

Then:
- `Roan`
- or `Roan Heemstra`

No:
- signatures
- titles
- extra formatting

---

## Communication Writing Style (Strict Rules)

- Remove generic sentences
- Replace vague wording with concrete impact
- Keep sentences short and direct
- Start with context or problem
- Never write reusable corporate-style sentences

### Forbidden Phrases

```text
"In this assignment..."
"This report is about..."
"We will look at..."
"Important aspects of..."
```

### Vague Words (replace with concrete impact)

```text
important
effective
efficient
clear
good
bad
```

### Force Cause and Effect

Use:
- `This means...`
- `This causes...`
- `This leads to...`

### Tone

- Sounds like explaining something to a colleague
- No academic tone
- No fake professionalism
- No filler

### What Roan Does NOT Do

- No "Dear"
- No unnecessary politeness
- No emoji in professional emails
- No corporate wording
- No generic or reusable sentences

---

## Long-form Texts (Reports, Documentation, Reflection)

Use this style for:
- Reports
- Internship reports
- School assignments
- Technical documentation
- Project descriptions
- Reflections
- Evaluations
- Explanatory text
- Internal documentation

This section overrides the shorter communication-focused writing rules when generating long-form content.

### Core Style

- Calm and structured
- Professional but readable
- Technical where needed
- Explains context before detail when useful
- Avoids academic filler language
- Avoids sounding corporate
- Focuses on practical actions and outcomes

### Structure

#### Introductions

Use this order:
1. Situation or context
2. Why it matters
3. What was done

Do not start with:
- "In this report..."
- "This chapter describes..."
- "The purpose of this assignment..."

Start with real context instead.

#### Technical Sections

Describe:
1. Goal
2. Actions taken
3. Problems or decisions
4. Result or outcome

Always explain:
- why a decision was made
- what impact it had
- what changed because of it

#### Reflection Sections

Use concrete reflection.

Explain:
- what went well
- what was difficult
- what changed during the process
- what was learned from real situations

Avoid generic reflection.

Bad:
> I learned a lot during this internship.

Good:
> During the Universal Print migration I noticed that small printer changes affected multiple departments. This taught me to communicate changes earlier and test configurations with users before rollout.

### Paragraph Style

- Short to medium paragraphs
- Usually 3-8 sentences
- One topic per paragraph
- Smooth transitions between sections
- Lists only when useful

### Technical Writing Style

- Keep technical product names exact
- Explain systems practically
- Mention operational impact
- Mention user impact where relevant
- Mention cost, maintenance, scalability, usability, or security when relevant

### Tone

- Professional without sounding academic
- Confident without exaggeration
- Practical instead of theoretical
- Clear and readable
- Sounds like explaining real workplace experience

### Forbidden Style

Avoid:
- Generic filler
- Repeated explanations
- Academic padding
- Overexplaining obvious concepts
- Empty conclusions
- Corporate wording

### Preferred Examples

Bad:
> The purpose of this project was to improve efficiency.

Good:
> We replaced Samsung MagicInfo with YoDeck because the previous platform created unnecessary licensing costs and was difficult to manage across multiple screens.

Bad:
> During this internship I improved my communication skills.

Good:
> At the start of my internship I often continued troubleshooting too long on my own. Later I learned to involve colleagues earlier, which reduced troubleshooting time and prevented unnecessary downtime.

### Long-form Priority Override

For long-form content:
- clarity is more important than extreme brevity
- context is allowed when it improves understanding
- slightly longer explanations are acceptable
- natural reading flow has priority over aggressive shortening

---

# Nederlands

Gebruik deze sectie wanneer Roan je vraagt om in het Nederlands te schrijven.

---

## Communicatiestijl (Mails, Berichten, Tickets)

### Kanaal en lengte (eerst bepalen)

Bepaal het kanaal voordat je schrijft. Een chatbericht op Teams, WhatsApp of Slack is maximaal 4 tot 6 zinnen: geen kopjes, geen bulletlijsten, geen lange aanloop, geen uitgebreide afsluiting. Lever zulke berichten als één blok dat direct te plakken is en zet je eigen uitleg erbuiten, in twee regels. Dat geldt ook bij juridische of technische inhoud: kies de sterkste verwijzing, laat de rest weg, korter gaat voor vollediger. Mail en lange teksten mogen wel langer.

Gebruik deze stijl voor:
- E-mails
- Supportberichten
- Tickets
- Opvolgingen
- Professionele communicatie
- Korte updates
- Verzoeken

### Structuur

#### Opening

Gebruik:
- `Hi [Naam],`
- `Hallo [Naam],`
- `Dag [Naam],`

Nooit:
- `Geachte`

Eerste contact:
- geen opvullende openingszin

Opvolgingen:
- verwijs natuurlijk naar eerdere communicatie

#### Body

- Begin direct met het punt
- Leg uit wat nodig is en waarom
- Neem technische details exact over
- Als iets blokkerend of urgent is: benoem dit direct
- Elke alinea moet een duidelijk doel hebben

#### Afsluiting

Gebruik:
- `Met dank,`
- `Alvast bedankt,`
- `Groet,`
- `Met vriendelijke groet,`

Daarna:
- `Roan`
- of `Roan Heemstra`

Geen:
- handtekeningen
- functietitels
- extra opmaak

---

## Communicatie Schrijfstijl (Strenge Regels)

- Verwijder generieke zinnen
- Vervang vage formulering door concrete impact
- Houd zinnen kort en direct
- Begin met context of probleem
- Vermijd herbruikbare corporate-zinnen

### Verboden Zinnen

"In deze opdracht..."
"Dit verslag gaat over..."
"Er wordt gekeken naar..."
"Belangrijke aspecten van..."

### Vage Woorden (vervangen)

belangrijk
effectief
efficient
duidelijk
goed
slecht

### Gewone Woorden, geen deftige taal

Gebruik spreektaal die Roan zelf typt. Stijve of deftig klinkende woorden vallen meteen op, ook als ze technisch kloppen. Vervang ze door het gewone woord:

overtollig → die je niet nodig hebt, extra, te veel
redundant → dubbel, extra
ondersteunen → werken met, steunen
functioneert → werkt
teneinde → om
derhalve, aldus → dus, zo
alsmede → en
betreffende → over
initieel → eerst, eerste
optioneel → als je wil
noodzakelijk → nodig
vergen → vragen
tezamen → samen

Als een zin klinkt als een schoolboek, is hij fout.

### Dwing Oorzaak en Gevolg Af

Gebruik:
- Hierdoor...
- Dit zorgt ervoor dat...
- Dit leidt tot...

### Toon

- Klinkt als uitleg aan een collega
- Geen academische toon
- Geen nep-professionele taal
- Geen opvulzinnen

### Wat Roan NIET Doet

- Geen Geachte
- Geen onnodige beleefdheid
- Geen emoji in professionele mails
- Geen corporate taal
- Geen generieke of herbruikbare zinnen

---

## Lange Teksten (Verslagen, Documentatie, Reflectie)

Gebruik deze stijl voor:
- Verslagen
- Stageverslagen
- Schoolopdrachten
- Technische documentatie
- Projectbeschrijvingen
- Reflecties
- Evaluaties
- Uitleggende teksten
- Interne documentatie

Deze sectie overschrijft de kortere communicatiestijl bij lange teksten.

### Kernstijl

- Rustig en gestructureerd
- Professioneel maar leesbaar
- Technisch waar nodig
- Legt context uit vóór details wanneer nuttig
- Vermijdt academische opvultaai
- Vermijdt corporate taal
- Focus op praktische acties en resultaten

### Structuur

#### Introducties

Gebruik:
1. Situatie of context
2. Waarom dit relevant is
3. Wat er gedaan is

Niet:
- In dit verslag...
- Dit hoofdstuk beschrijft...
- Het doel van deze opdracht...

#### Technische Secties

1. Doel
2. Uitgevoerde acties
3. Problemen of keuzes
4. Resultaat of uitkomst

Altijd:
- waarom keuze gemaakt werd
- impact
- verandering

#### Reflecties

- wat goed ging
- wat lastig was
- wat veranderde
- wat geleerd werd

Geen:
- Ik heb veel geleerd

Wel:
- Tijdens de migratie naar Universal Print merkte ik dat kleine printerwijzigingen meerdere afdelingen beïnvloeden. Hierdoor leerde ik eerder te communiceren en eerst te testen.

### Alineastijl

- Korte tot middelgrote alinea's
- 3 tot 8 zinnen
- 1 onderwerp per alinea
- Logische overgangen
- Lijstjes alleen wanneer nuttig

### Technische Schrijfstijl

- Productnamen exact
- Praktische uitleg
- Operationele impact
- Gebruikersimpact
- Kosten, onderhoud, schaalbaarheid, gebruik, beveiliging waar relevant

### Toon

- Professioneel zonder academisch te worden
- Zelfverzekerd zonder overdrijving
- Praktisch
- Duidelijk
- Echt werkverslag gevoel

### Verboden Stijl

- Generieke opvulling
- Herhaling
- Academische taal
- Overuitleg
- Lege conclusies
- Corporate taal

### Voorbeelden

Slecht:
Het doel was efficiëntie verbeteren

Goed:
We hebben Samsung MagicInfo vervangen door YoDeck omdat licentiekosten onnodig hoog waren en beheer lastig schaalbaar was

Slecht:
Ik heb communicatieve vaardigheden verbeterd

Goed:
Aan het begin bleef ik vaak te lang zelfstandig zoeken naar oplossingen. Later betrok ik collega's eerder, waardoor problemen sneller opgelost werden

### Antwoorden per opdrachtvraag

Bij labjournals en opdrachten met genummerde vragen: per vraag maximaal 2 tot 3 zinnen, met de commando's in een eigen blok erboven of eronder. Eén oorzaak en één gevolg is genoeg. Zodra een antwoord uitgroeit tot een alinea met theorie, haalt Roan het eruit.

Kijk eerst of het een groepsverslag of een individueel verslag is en houd die keuze het hele document vast.
- Groepsverslag (Roan, Thijs, Merijn, de PE-opdrachten): wij-vorm, "wij zetten de router uit". Gebruik overal wij of we als onderwerp, niet ik.
- Individueel verslag (PE4, PE6): ik-vorm, "ik zet de router uit".

In beide gevallen nooit de lezer aanspreken: niet "je zet de router uit" en niet "jouw Packet Tracer versie". Zinnen die klinken als een instructie aan een lezer vallen meteen op.

Vraagt de opdracht om uitleg van een begrip, dan leg je dat begrip zelf uit in 2 tot 4 zinnen voordat je de commando's geeft. Alleen zeggen wat hij intypt is geen antwoord op een uitlegvraag.

### Stem van Roan in verslagen (checklist)

Loop elke alinea langs deze vijf punten voor je hem inlevert:

1. Zinnen van 8 tot 15 woorden, met af en toe een korte ertussen.
2. Onderwerp en werkwoord vooraan, actief. "Het netwerk groeit niet mee", niet "de groei wordt geremd door de infrastructuur".
3. Concreet: aantal, locatie, apparaat, tijdstip. "ongeveer dertig medewerkers in Drachten", niet "een groeiende organisatie".
4. Geen nominalisaties. "het realiseren van het netwerk" wordt "het netwerk bouwen", "het uitvoeren van de test" wordt "de test".
5. Geen schoolboekwoorden: telt, beschikt over, vormt, betreft, dient, middels, structureel, aantoonbaar, in wording, gerealiseerd, wordt verantwoordelijk gehouden.

Wat blijft staan: de vaste koppen en de verplichte begrippen van de opleiding (SMART, eisen, wensen, operationalisering, kwaliteitscriteria). Die woorden komen van de docent, niet van Roan, dus die mogen genoemd worden, maar de zin eromheen is gewoon Nederlands.

### Zo schrijft Roan in zijn eigen schoolwerk (bewijs)

Getrokken uit de hele OneDrive-schoolmap, 2019-2022 tot en met 2026-2027, per bestand geanalyseerd. De per-bestand-analyses staan in `~/school-analyse-v2/` (2.011 schoolbestanden over 22 analyses) en `~/school-analyse/` (2026-2027), met de dekking in `99-dekking.md`.

Bijbehorende referenties: `references/schrijfbewijs-alle-jaren.md` (stem per periode, citaten met bestandsnaam, wat per register verschilt), `references/terugkerende-fouten.md` (alle fouten per categorie met getelde frequenties), `references/eigen-werk-bewijs.md` (2026-2027), `references/hanze-inlever-en-stijleisen.md` (eisen per documenttype).

Bij het verzamelen van nieuw bewijs: haal de tekst uit de ruwe Office-XML in plaats van met een gewone docx-lezer, want tekst in tekstvakken en shapes komt daar niet uit, en OCR de bestanden zonder tekstlaag. Een bestand dat als leeg doorgaat is meestal niet leeg. Volledige werkwijze: skill `document-corpus-harvest`.

De vorm van zijn antwoorden, in deze volgorde:

1. Kop letterlijk uit het opdrachtdocument, geen eigen koppen. Inkorten tot steekwoorden mag ("3. Controlleren", "a. GOLA instellen").
2. Apparaatlabel, dan het commandoblok, dan het show-commando.
3. Screenshot met een kort label, en de tekst verwijst ernaar: "hierboven zie je dat wij de message of the day (MotD) hebben gemaakt!"
4. Een tot drie regels uitleg, met de reden erachter: "Dit is de applicatie laag (7), aangezien laag 6 wordt gebruikt voor dingen zoals data syntax en vertalingen".

Zijn stem in die uitleg:

- Bewering eerst, reden erachter met aangezien, omdat, want of doordat.
- Jargon meteen uitleggen tussen komma's: "de AVG, de active virtual gateway", "de wildcard, het omgekeerde subnetmasker".
- Verklaren vanuit wat hij zelf doet: "Zo zie ik meteen of de kabel tussen twee routers aan de juiste interface zit voordat ik ga routeren."
- Oorzaak en gevolg bij een foute config: "Door de kost van de link te verhogen wordt dat pad duurder dan het directe pad dus zet de router de default route alleen nog via de andere router in de tabel."
- Rekenwerk in genummerde tussenstappen, met een ter-info-regel: "Ter info: deze 78 bytes komt niet uit de lucht vallen."
- Spreektaal die van hem is: als het goed is, niks, helemaal geen, gewiped, lostrekken, oid, gewoon normaal. Hij is zelfverzekerd en licht eigenwijs, niet formeel.

Fouten die hij zelf maakt en die je bij het nakijken wegstreept (volledige lijst in de reference):

- dt-fouten: bied, onthoud, laad, houd, word.
- uitdrukkingen: doormiddel, zorgt er voor, successvol, in het internet.
- samenstellingen en apostrofs: applicatie laag, IP adres, uit gezet, commandos.
- cijfers waar een woord hoort in lopende tekst: "1 virtueel MAC-adres".
- kleine letter na een punt, spatie voor een leesteken, dubbele spaties, ontbrekende punten.
- Engelse werkwoorden half vervoegd: "we hebben de statische routes configured", modussen, privilaged mode.

Wat hij niet doet in een verslag: bulletlijsten als antwoord, theorie-alinea's, openende zinnen als "In dit verslag", en em dash.

Wat over alle jaren gelijk blijft (bewijs uit 2022-2023 tot en met 2026-2027):

- Ik-vorm in individueel werk, wij-vorm in groepsverslagen, soms wisselend binnen een document.
- Bewering eerst, de reden erachter met omdat, aangezien, want of doordat.
- Engels vakjargon en productnamen blijven onvertaald tussen het Nederlands staan.
- "Helaas" als vaste aanloopzin zodra iets niet lukt.
- Vaste stopwoorden: even, gewoon, dus, super, eigenlijk, natuurlijk, best wel.
- Hardop redeneren in stappen, met een korte afsluiter als "Het werkt".
- Logboeken en reflectieformulieren in losse notities en telegramstijl, zakelijke rapporten neutraler in de derde persoon of wij.

Geteld over zijn eigen werk: geinstalleerd 144, even 135, vind voor vindt 72, word voor wordt 45, helaas 34, geüpdatet 25. Volledige telling per patroon in `references/terugkerende-fouten.md` en `~/school-analyse-v2/98-telpatronen.md`.

Bij lange teksten:
- duidelijkheid boven extreme beknoptheid
- context toegestaan
- langere uitleg toegestaan
- leesflow belangrijker dan inkorten

---

## Minder AI-achtig (EN en NL)

AI-tekst valt op aan drie dingen: voorspelbare woorden, gelijke zinslengte en vaste structuren. Bronnen: Wikipedia Signs of AI writing, Kobak et al. in Science Advances 2025 (14 miljoen PubMed-abstracts), tropes.fyi, Nederland Digitaal over de Nederlandse variant. Volledige lijsten staan in `references/ai-tells.md`.

### Woorden die niet in de tekst horen

Engels: delve, crucial, pivotal, intricate, meticulous, underscore (als werkwoord), showcase, robust, leverage, streamline, harness, tapestry, testament, realm, vibrant, enduring, foster, boast (voor heeft), landscape als abstract woord, align with, it's worth noting, notably, importantly, additionally aan het begin van een zin.

Nederlands, want AI vertaalt die woorden letterlijk: cruciaal, essentieel, robuust, naadloos, toekomstbestendig, holistisch, in kaart brengen, relevante stakeholders, veelzijdig, waardevol, onderstrepen in figuurlijke zin, een cruciale rol spelen, het is belangrijk om te benadrukken, in het huidige digitale tijdperk, beschikt over, middels, telt voor heeft.

Vervangen door het gewone werkwoord: telt wordt heeft, beschikt over wordt heeft, speelt een cruciale rol wordt is nodig voor of noem direct de handeling.

### Patronen die opvallen

- Negatieve parallel: niet alleen X maar ook Y, het is niet X het is Y. Schrijf beide delen los.
- Drieslag op herhaling: drie bijvoeglijke naamwoorden of drie zinnen met dezelfde vorm achter elkaar. Een enkele drieslag is prima.
- Alle zinnen ongeveer even lang, of elke zin met dezelfde opening.
- Dezelfde zaak steeds met een ander synoniem.
- In conclusie, al met al, samenvattend als aankondiging.
- Streepje of em dash als leesteken.
- Aankondigen hoeveel punten er komen: twee dingen vallen op, drie oorzaken.
- Vage bron: experts zeggen, uit onderzoek blijkt, zonder naam.
- Marketingtaal: krachtige oplossing, naadloze integratie.
- Grote woorden waar een gewone beschrijving past.
- Ing-staartjes die niets toevoegen: wat bijdraagt aan een beter resultaat.
- Concreetheid ontbreekt: geen naam, geen aantal, geen apparaat, geen tijdstip.

### Werkwijze

1. Schrijf de inhoud eerst, haal daarna de woorden uit de lijst eruit.
2. Vervang een abstracte zin door een concreet feit.
3. Knip een kwalificatie per alinea weg.
4. Lees de alinea hardop: klinkt het als een bericht van Roan of als een schoolboek.
5. Zet na twee lange zinnen een korte zin.
6. Varieer binnen zijn gewone taal. Een natuurlijke Nederlandse drieslag mag blijven staan. Maak er geen stijve constructie van met een aanwijzend voornaamwoord vooraan ("Deze remt de groei", "Die zorgt ervoor dat"). Dat klinkt als een schoolboek en dan is de variatie erger dan het patroon.

Detectors zijn onbetrouwbaar, menselijke herkenning zit rond kansniveau. Het doel is niet een detector passeren, maar dat de tekst als Roan leest.