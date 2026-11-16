#!/usr/bin/env python3
"""Stijlcontrole voor Nederlandse tekst van Roan.

Telt de woorden en patronen uit deze skill en print ze met de eerste treffer,
zodat je na het schrijven ziet wat er nog in zit. Exitcode 1 bij harde fouten
(streepje als leesteken, &, zowel ... als), anders 0.

Gebruik:
    python3 stijlcheck.py verslag.docx
    python3 stijlcheck.py mail.md --max-zin 20
    python3 stijlcheck.py verslag.docx --register derde
"""
import argparse
import re
import sys

VAGE_WOORDEN = [
    "belangrijk", "effectief", "efficient", "efficiënt", "duidelijk", "goed", "slecht",
]

DEFTIGE_WOORDEN = [
    "overtollig", "redundant", "ondersteunen", "functioneert", "teneinde", "derhalve",
    "aldus", "alsmede", "betreffende", "initieel", "optioneel", "noodzakelijk", "vergen",
    "tezamen", "dadelijk",
]

SCHOOLBOEK_WOORDEN = [
    "telt", "beschikt over", "vormt", "betreft", "dient", "middels", "structureel",
    "aantoonbaar", "in wording", "gerealiseerd", "wordt verantwoordelijk gehouden",
]

AI_WOORDEN = [
    "cruciaal", "essentieel", "robuust", "naadloos", "toekomstbestendig", "holistisch",
    "in kaart brengen", "relevante stakeholders", "veelzijdig", "waardevol", "onderstrepen",
    "het is belangrijk om te benadrukken", "in het huidige digitale tijdperk",
]

OPENERS = [
    "in dit verslag", "in dit rapport", "dit hoofdstuk beschrijft", "dit verslag gaat over",
    "in deze opdracht", "er wordt gekeken naar", "het doel van deze opdracht",
]

HARDE_FOUTEN = [" & ", "zowel "]


def lees(pad: str) -> str:
    if pad.lower().endswith(".docx"):
        try:
            from docx import Document
        except ImportError:
            sys.exit("python-docx ontbreekt: pip install python-docx")
        doc = Document(pad)
        delen = [p.text for p in doc.paragraphs]
        for tabel in doc.tables:
            for rij in tabel.rows:
                delen.append(" | ".join(cel.text for cel in rij.cells))
        return "\n".join(delen)
    with open(pad, encoding="utf-8") as f:
        return f.read()


def tel(tekst: str, woorden) -> dict:
    laag = tekst.lower()
    return {w: laag.count(w) for w in woorden if laag.count(w)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pad")
    ap.add_argument("--max-zin", type=int, default=25)
    ap.add_argument("--register", choices=["derde", "ik", "wij", "vrij"], default="vrij",
                    help="derde = neutrale inleiding, ik/wij = persoonlijk deel")
    args = ap.parse_args()

    tekst = lees(args.pad)
    woorden = len(tekst.split())
    print(f"{args.pad}: {woorden} woorden")

    hard = 0
    streepjes = tekst.count(" - ")
    streepjes += tekst.count("—") + tekst.count("–")
    print(f"streepje als leesteken: {streepjes}")
    hard += streepjes

    for fout in HARDE_FOUTEN:
        n = tekst.lower().count(fout)
        if n:
            print(f"verboden teken of paar '{fout.strip()}': {n}")
            hard += n

    for naam, lijst in (("vaag", VAGE_WOORDEN), ("deftig", DEFTIGE_WOORDEN),
                        ("schoolboek", SCHOOLBOEK_WOORDEN), ("AI-woord", AI_WOORDEN)):
        treffers = tel(tekst, lijst)
        if treffers:
            print(f"{naam}: " + ", ".join(f"{w} x{n}" for w, n in treffers.items()))

    laag = tekst.lower()
    for opener in OPENERS:
        if opener in laag:
            print(f"openende zin: '{opener}'")

    zinnen = [z.strip() for z in re.split(r"(?<=[.!?])\s+", tekst) if z.strip()]
    lang = [z for z in zinnen if len(z.split()) > args.max_zin]
    print(f"zinnen langer dan {args.max_zin} woorden: {len(lang)} van {len(zinnen)}")
    for z in lang[:5]:
        print("   " + z[:110])

    if args.register != "vrij":
        tellingen = {
            "ik": len(re.findall(r"\bik\b", laag)),
            "wij": len(re.findall(r"\bwij\b|\bwe\b", laag)),
            "je": len(re.findall(r"\bje\b|\bjouw\b|\bjij\b", laag)),
        }
        print("register: " + ", ".join(f"{k} x{v}" for k, v in tellingen.items()))
        if args.register == "derde" and (tellingen["ik"] or tellingen["wij"] or tellingen["je"]):
            hard += 1
            print("LET OP: neutrale sectie hoort in de derde persoon")
        if args.register == "ik" and tellingen["wij"]:
            print("LET OP: individueel verslag hoort ik te gebruiken, geen wij")

    print("RESULTAAT: " + ("nee, eerst herschrijven" if hard else "schoon op de harde punten"))
    return 1 if hard else 0


if __name__ == "__main__":
    raise SystemExit(main())
