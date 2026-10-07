# Bewijs uit Roans eigen schoolwerk (2026-2027)

Bron: de 55 bestanden uit de OneDrive-schoolmap `2026-2027 - Hanze - Jaar 2`, per bestand geanalyseerd. De volledige analyses staan in `/home/roan/school-analyse/`. Alle citaten hieronder zijn letterlijk overgenomen, inclusief fouten en ontbrekende punten.

## Welk materiaal is echt van Roan

- **Individueel:** `PE4 - Roan`, `PE6 - Roan`, `Theorievragen HTTP - Roan Heemstra.docx`, het antwoorddeel van `Opdracht-netwerken-week-3 - v2.docx` (TCP-uitwerking).
- Groep (Roan, Thijs en Merijn, groep 3): de PE-verslagen PE1, PE2, PE3, PE5, PE7 en PE8
- **Geen stijlbewijs:** de opdrachtdocumenten PE 1 t/m PE 10, de Schrijfwijzer, de PPT's, de Kurose & Ross-labs, de praktijkinfobladen, de `.pkt`-bestanden (binair, geen leesbare apparaatnamen of config), de oefentoets-PDF's (geen tekstlaag, met OCR gelezen) en de pcapng-captures (ruwe netwerkdata).

## Vaste vorm van een labjournalantwoord

1. De kop komt letterlijk uit het opdrachtdocument (`A. Netwerk opbouwen en basisconfiguratie`, `D. Passieve interfaces configureren`). Hij verzint geen eigen koppen en kort ze soms in tot steekwoorden: `1 - 2. Ingesteld`, `3. Controlleren`, `a. GOLA instellen`.
2. Per stap: apparaatlabel, commandoblok, show-commando, screenshot, dan 1 tot 3 regels uitleg.
3. Bewijs is de screenshot met een minimaal label (`a. Ping van R06-1 naar R06-2:`). In de tekst verwijst hij naar beelden met een nummer: `de eerste foto is van RS1 en de tweede foto is RS2`.
4. Theorievragen beantwoordt hij wel, maar in 1 tot 3 zinnen. Voorbeeld: `De twee getallen tussen de blokhaken zijn administratieve afstand / metric. De eerste is hoe betrouwbaar de bron is. De tweede waarde is de metric, de kost van het hele pad.`

## Hoe hij uitlegt (zijn echte stem)

- Bewering eerst, reden erachter met aangezien, omdat, want of doordat: `Dit is de applicatie laag (7), aangezien laag 6 wordt gebruikt voor dingen zoals data syntax en vertalingen`.
- Jargon meteen uitleggen tussen komma's: `de AVG, de active virtual gateway`, `de wildcard, het omgekeerde subnetmasker`.
- Output in eigen woorden duiden: `Het sterretje in die regel betekent gateway of last resort en E2 betekent dat de route van buiten het OSPF-domein komt.`
- Verklaren vanuit zijn eigen handelen: `Zo zie ik meteen of de kabel tussen twee routers aan de juiste interface zit voordat ik ga routeren.` en `Met -t blijft de ping lopen, zodat ik tijdens het lostrekken van de kabel zie wat er met de verbinding gebeurt.`
- Naar het beeld wijzen: `hierboven zie je dat wij de message of the day (MotD) hebben gemaakt!`
- Oorzaak en gevolg bij een configuratiewijziging: `Door de kost van de link naar R06-1 te verhogen wordt dat pad duurder dan het directe pad dus zet de router de default route alleen nog via R06-2 in de tabel.`
- Rekenwerk in genummerde tussenstappen (`1. Wat kost één byte aan tijd? 2. Die deling handig maken 3. Invullen 4. De overhead erbij`) met een informele noot: `Ter info: deze 78 bytes komt niet uit de lucht vallen.`

## Spreektaal die hij echt typt

`Als het goed is`, `Niks`, `helemaal geen`, `gewiped`, `lostrekken`, `is meeverhuisd naar`, `oid`, `gewoon normaal`, en over zijn eigen site: `Ik navigeer naar de beste site die er is: https://roanheemstra.nl/`. Hij is zelfverzekerd en licht eigenwijs, nooit formeel.

## Aanspreekvorm in de praktijk

- Individueel werk: ik-vorm. `Ik heb de Multilayer Switch_RMH_0 gekozen, want die heeft zes aangesloten interfaces`
- Groepswerk: in de oudere PE's wisselt het tussen wij en ik (`We hebben dit gedaan met erase startup-config` naast `Ik sluit RS1-Roan Gi0/0/0 aan op ISP 1`); PE8 staat zelfs overwegend in ik-vorm. De regel blijft: kies één vorm en houd hem het hele document vast, wij in groepsverslagen en ik in individuele verslagen, zoals Roan het vraagt.
- Theorievragen: algemene `je` (`Je kan HTTP upgraden naar HTTPS`), en zodra het over zijn eigen handelen gaat `ik`. In een rapport dat om een neutrale stijl vraagt: geen ik, wij of je.

## Fouten die hij zelf maakt (wegstrepen bij het nakijken)

- Werkwoordsvorm: `HTTP bied` (biedt), `De server onthoud` (onthoudt), `dan laad hij` (laadt), `Het uit zetten houd dit tegen` (houdt), `De com poort word herkend` (wordt).
- Vaste uitdrukkingen: `doormiddel` (door middel van), `zorgt er voor` (ervoor), `in het internet` (op het internet), `successvol` (succesvol).
- Aaneen of los: `applicatie laag` (applicatielaag), `IP adres` (IP-adres), `uit gezet` (uitgezet), `commandos` (commando's).
- Verkeerd woord: `weet stabiel zijn` (moet zijn), `modussen` (modi), `het routingtabel wat` (dat), `dezelfde line` (lijn), `privilaged mode` (privileged), `Per las` (LSA), `advertisment` (advertisement), `prifix` (prefix), `Controlleren` (controleren), `ongeauthoriseerde` (ongeautoriseerde).
- Cijfer waar een woord hoort in lopende tekst: `1 virtueel MAC-adres`, `PC-A heeft maar 1 gateway`.
- Opmaakslordigheden: spatie voor een punt (`show cdp neighbors .`), dubbele spaties, ontbrekende punten, kleine letter na een punt (`ik zet het aan`, `het subnet`), `packet tracer` en `ipv.` zonder punten of hoofdletters.

## Wat hij niet doet

Geen bulletlijst voor zijn antwoorden, hij werkt met genummerde stappen en monospace commandoblokken. Geen theoredealnea's, geen aankondigende zinnen als `In dit verslag`, geen streepje als leesteken.
