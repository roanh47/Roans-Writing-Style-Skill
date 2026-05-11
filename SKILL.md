---
name: roans-writing-style
description: "Roan Heemstra's personal writing style guide. How to write emails, messages, and professional text in Roan's voice. Combined EN/NL reference for single-file use."
version: 2.0.0
author: Roan
license: personal
metadata:
  hermes:
    tags: [writing, style, voice, roan, professional, copywriting, en, nl]
    trigger: "Any task asking to write, draft, rewrite, or format outward-facing text for Roan"
---

# Roan's Writing Style

Ported from `~/.openclaw/workspace/ROANS-HANDWRITING.md`.
Defines exactly how Roan wants text written on his behalf.

## Language Selection

When Roan asks you to write:
- **English** - Use the **English** section below
- **Dutch** - Use the **Nederlands** section below

---

## Critical Rules (All Languages)

**NO EM DASHES (---). EVER.**
Use a regular hyphen `-`, comma `,`, or split into two sentences.
This applies to ALL messages, including internal ones to Roan.

## Core Voice

- **Direct, not cold** - says what needs saying without filler
- **Polite but not servile** - respectful, no overdoing it
- **Brief paragraphs** - typically 1-3 sentences
- **Explains context when it matters** - shows why something matters
- **Concrete over abstract** - avoids vague or generic phrasing

## Rewrite Pattern (Enforced)

When generating text:
1. Identify the actual situation or problem
2. State it directly without explaining the topic first
3. Add concrete cause and effect
4. Remove any sentence that could fit any report
5. Replace vague words with specific impact

## Agent Boundary - User-Owned Documents

**Roan edits his own personal documents. The agent does NOT.**

- If Roan says "Ik ga het document bewerken en niet jij" ("I will edit the document, not you"), respect this immediately. Stop any automated editing of his personal reference files.
- The agent may create **new** reference files as derived supplements, but must never overwrite or rename Roan's original files without explicit instruction.
- When in doubt: ask before modifying anything in `~/.hermes/skills/productivity/roans-writing-style/references/`.

---

# English

Use this section when Roan asks you to write in English.

## Structure

### Opening
- `Hi [Name],` or `Hello [Name],` - never "Dear"
- First contact: "I hope you're doing well"
- Follow-ups: reference previous message naturally

### Body
- Start with the point immediately
- Explain what is needed and why
- Include technical details exactly as-is
- If blocking or urgent: state it clearly
- Each paragraph has a clear purpose: what is the issue, why it matters, what needs to happen

### Sign-off
- `Thank you,`
- `Sincerely,`
- `Best,` (only if very informal)
- Then `Roan` or `Roan Heemstra`
- No signatures, titles, or extras

## Writing Style (Strict Rules)

- Remove all generic sentences
- Replace vague wording with concrete impact
- Ensure each sentence adds new information
- Keep sentences short and direct
- Start with context or problem, not theory
- Never write sentences that could apply to any situation

### Forbidden Phrases
```
"In this assignment..."
"This report is about..."
"We will look at..."
"Important aspects of..."
```

### Vague Words (always replace with concrete impact)
`important` - `effective` - `efficient` - `clear` - `good` - `bad`

### Force Cause and Effect
Use: `This means...` - `This causes...` - `This leads to...`

### Language Rules
- Short sentences
- No filler words
- No theory unless needed
- No generic conclusions

## Tone
- Sounds like explaining to a colleague
- No academic tone
- No "nice sounding" filler sentences
- Focus on clarity and outcome

## What Roan Does NOT Do
- No "Dear"
- No filler openings unless intentional
- No emoji in emails
- No unnecessary politeness
- No generic or reusable sentences

## Real Examples (English)

### Following up on a case/ticket:
> Hi Swathi,
>
> Thank you for the update. I appreciate you keeping me in the loop while you coordinate with the internal team.
> I'll look forward to hearing from you as soon as there's more information.
>
> Sincerely,
> Roan

### Asking for something:
> Hello Swathi,
>
> May I request an update on the status of my case? I'm unfortunately still unable to access my tenant.
> I rely on my Microsoft tenant for identity management in Entra ID, and would like to continue using it in the near future.
>
> Thank you,
> Roan

### Providing technical info (no preamble):
> Hello Microsoft Support,
>
> What extra details do you require?
> I would like additional assistance to get this case resolved.
>
> Thank you.
>
> Sincerely,
> Roan

### Short direct message:
> Hi [Name],
>
> The server is down. I need access restored by 14:00 to meet the client deadline.
> Can you confirm when this will be resolved?
>
> Thank you,
> Roan

---

# Nederlands

Gebruik deze sectie wanneer Roan je vraagt om in het Nederlands te schrijven.

## Structuur

### Opening
- `Hi [Naam],` of `Hallo [Naam],` of  `Dag [Naam],`- nooit "Geachte"
- Eerste contact: geen opvulling als "Ik hoop dat deze e-mail u goed bereikt"
- Opvolgingen: verwijs natuurlijk naar het vorige bericht

### Body
- Begin direct met het punt
- Leg uit wat er nodig is en waarom
- Neem technische details exact over zoals ze zijn
- Als het blokkerend of urgent is: zeg dat duidelijk
- Elke alinea heeft een duidelijk doel: wat is het probleem, waarom doet het ertoe, wat moet er gebeuren

### Afsluiting
- `Met dank,`
- `Alvast bedankt,`
- `Groet,`
- `Met vriendelijke groet,`
- Dan `Roan` of `Roan Heemstra`
- Geen handtekeningen, titels, of extra's

## Schrijfstijl (Strenge Regels)

- Verwijder alle generieke zinnen
- Vervang vage formulering door concrete impact
- Zorg dat elke zin nieuwe informatie toevoegt
- Houd zinnen kort en direct
- Begin met context of probleem, niet met theorie
- Schrijf nooit zinnen die in elke situatie zouden passen

### Verboden Zinnen
```
"In deze opdracht..."
"Dit verslag gaat over..."
"Er wordt gekeken naar..."
"Belangrijke aspecten van..."
"Ik hoop dat deze e-mail u goed bereikt" (alleen eerste contact)
```

### Vage Woorden (altijd vervangen door concrete impact)
`belangrijk` - `effectief` - `efficient` - `duidelijk` - `goed` - `slecht`

### Dwing Oorzaak en Gevolg Af
Gebruik: `Hierdoor...` - `Dit zorgt ervoor dat...` - `Dit leidt tot...`

### Taalregels
- Korte zinnen
- Geen opvulwoorden
- Geen theorie tenzij nodig
- Geen generieke conclusies

## Toon
- Klinkt als uitleg aan een collega
- Geen academische toon
- Geen "lekker klinkende" opvulzinnen
- Focus op duidelijkheid en resultaat

## Wat Roan NIET Doet
- Geen "Geachte [Naam]"
- Geen opvullende openingszinnen tenzij expres
- Geen emoji in externe mails
- Geen corporate taal
- Geen onnodige beleefdheid
- Geen generieke of herbruikbare zinnen

## Echte Voorbeelden (Nederlands)

### Opvolging van een case/ticket:
> Hallo Swathi,
>
> Dank voor de update. Ik waardeer dat je me op de hoogte houdt terwijl je dit intern coordineert.
> Ik hoor graag van je zodra er meer informatie is.
>
> Met dank,
> Roan

### Iets vragen:
> Hallo Swathi,
>
> Kan ik een update krijgen over de status van mijn case? Ik kan mijn tenant helaas nog steeds niet benaderen.
> Ik vertrouw op mijn Microsoft tenant voor identity management in Entra ID, en wil deze graag zo snel mogelijk weer gebruiken.
>
> Met dank,
> Roan

### Technische info geven (zonder inleiding):
> Hallo Microsoft Support,
>
> Welke extra gegevens hebben jullie nodig?
> Ik wil graag verdere hulp om dit case opgelost te krijgen.
>
> Met dank.
>
> Met vriendelijke groet,
> Roan

### Kort direct bericht:
> Hallo [Naam],
>
> De server ligt eruit. Ik heb toegang nodig voor 14:00 om de client-deadline te halen.
> Kun je bevestigen wanneer dit opgelost is?
>
> Met dank,
> Roan
