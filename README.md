# Ontario Corridor Fire Separation Checker (OBC 3.3.1.4)

What fire separation — and what fire-resistance rating — does a public corridor need in Ontario? The honest answer is one article, not a matrix: OBC 2024 Article 3.3.1.4 sets a 45-minute default and then relaxes it for sprinklered storeys, with carve-outs. This checker walks the article, and adds the exit-enclosure rule of 3.4.4.1.

**Live web tool:** https://dust2engineering.github.io/ontario-corridor-fire-separation-checker/web/

## How it works

- Start from the default: an unsprinklered storey needs a 45 min rated fire separation between a public corridor and the remainder of the storey.
- If the storey is sprinklered and the corridor does not serve a care, care and treatment, detention or residential occupancy, the separation is still required but needs no rating (Sentence (3)).
- On a sprinklered floor area, Sentence (4) can remove the separation entirely: (a) vs the remainder of the storey when travel distance to an exit is ≤ 45 m; (b) vs a room or suite when the corridor meets 3.3.1.9.(6) and 3.4.2.5.(1)(d); (c) vs washroom space, with a combined-separation condition.
- For Group E and F Div. 1/2 corridors using the relief, the sprinkler system must be electrically supervised and signal the fire department (Sentence (5)).
- Exits are a different article: 3.4.4.1 ties the exit-enclosure rating to the floor-assembly rating of Subsection 3.2.2, minimum 45 min, maximum 2 h.

## Data in this repository

- `corridor-rules.json` — every rule of 3.3.1.4 as a condition/requirement/article record, plus the 3.4.4.1 exit rule, in machine-readable form.
- Wording verified against the OBC 2024 (O. Reg. 163/24) text of Article 3.3.1.4 and the official 2024 Compendium text of 3.4.4.1.

## Command line

```bash
python3 corridor_checker.py --sprinklered yes --serves other --travel-distance 30
```

## Worked examples

- [example-sprinklered-office.txt](examples/example-sprinklered-office.txt)
- [example-unsprinklered-residential.txt](examples/example-unsprinklered-residential.txt)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Fire and life safety. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
