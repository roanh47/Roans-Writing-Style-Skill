# Roan's Writing Style Skill

An AI skill that makes AI output sound like an actual human wrote it. Specifically: like I wrote it.

## The problem

You hand your AI a draft, it rewrites it, and everyone who knows you immediately says: "This is so obviously not written by you."

That happens because default AI output is generic. It sounds like everyone and no one. It uses phrases no real person would type. It lacks the small quirks that make text recognizable as yours.

## The solution

Feed your AI your old hand-written documents. Let it extract patterns, rules, and tone. Turn that into a skill file that loads automatically every time the AI writes on your behalf.

That is exactly what this repo contains.

## What this skill does

- Loads automatically when the AI writes, drafts, or rewrites text for you
- Enforces concrete language over vague filler
- Blocks generic phrases like "In this assignment..." or "Important aspects of..."
- Forces cause-and-effect sentences instead of empty descriptions
- Removes em-dashes entirely (use a colon, a comma, or two sentences instead)
- Keeps paragraphs short, usually 1 to 3 sentences
- Uses the correct sign-off format per language, with the greeting and sign-off I actually send
- Keeps three registers apart: a report, a business mail, and a work log are not the same voice
- Counts the leftovers afterwards with `scripts/stijlcheck.py` instead of trusting memory

## Language support

The skill contains two full reference sections:

- **English** for emails, messages, and professional text in English
- **Nederlands** for the same in Dutch

The AI selects the correct section based on the language you ask for.

Inside those two sections it picks a register, because I do not write the same way everywhere:

- Report or school document: neutral, structured, cause and effect
- Business mail: one block, `Beste` as the greeting, full name at the end
- CV or profile: first person, short factual lines, no marketing words
- Work log: telegram style, no full stops, the abbreviations I use myself

The last three come from my own sent mail, my CV and my work log, and they sit in `references/mail-cv-logboek.md`.

## How to use

Place `SKILL.md` in your skills directory:

```
~/skills/roans-writing-style/SKILL.md
```

Or clone this repo and add it as an external skill directory in `config.yaml`:

```yaml
skills:
  external_dirs:
    - /path/to/roans-writing-style-skill.md
```

## Known issues

- Dual-language support works but needs explicit language selection from the user
- The register picker lives in prose, not in code, so an ambiguous prompt can still land in the wrong voice
- The AI sometimes still drifts into generic phrasing on very open-ended prompts
- Fine-tuning continues as I spot more patterns in my own writing

## Origin

This skill was built by analyzing actual emails, messages, and documents I wrote. The AI extracted the rules, I reviewed them, and we iterated until the output matched my real voice.
