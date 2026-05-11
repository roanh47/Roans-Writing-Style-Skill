# Roan's Writing Style Skill

A Hermes Agent skill that makes AI output sound like an actual human wrote it. Specifically: like I wrote it.

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
- Removes em-dashes entirely (use hyphens or commas instead)
- Keeps paragraphs short, usually 1 to 3 sentences
- Uses the correct sign-off format per language

## Language support

The skill contains two full reference sections:

- **English** for emails, messages, and professional text in English
- **Nederlands** for the same in Dutch

The AI selects the correct section based on the language you ask for.

## How to use

### Hermes Agent

Place `SKILL.md` in your skills directory:

```
~/.hermes/skills/productivity/roans-writing-style/SKILL.md
```

Or clone this repo and add it as an external skill directory in `config.yaml`:

```yaml
skills:
  external_dirs:
    - /path/to/roans-writing-style-skill
```

### Other systems

The file is standard Markdown with YAML frontmatter. Any system that supports knowledge files, system prompts, or custom instructions can use it. Just paste the relevant section into your prompt or upload it as a knowledge file.

## Known issues

- Dual-language support works but needs explicit language selection from the user
- The AI sometimes still drifts into generic phrasing on very open-ended prompts
- Fine-tuning continues as I spot more patterns in my own writing

## Origin

This skill was built by analyzing actual emails, messages, and documents I wrote. The AI extracted the rules, I reviewed them, and we iterated until the output matched my real voice.

## License

Personal. Do whatever you want with this.
