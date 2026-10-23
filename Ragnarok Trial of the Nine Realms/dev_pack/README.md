# Trial of the Nine Realms — Supply Chain Disruption Intelligence Challenge

## The Mission

A supply chain disruption has been reported across the Runemark trade network. Most AI tools only summarize the news — sourced facts and speculation get blended together, and decision-makers cannot tell what is certain and what is disputed.

Your task is to build an **adversarial multi-agent courtroom system** that treats every disruption as a court case. The system must ingest the document corpus, verify the event is real, debate the commercial exposure from two opposing sides, and deliver a structured intelligence briefing with every claim graded by nature and confidence.

There is no spoon-fed answer. You and your team must design the architecture, retrieve the right evidence, challenge each other's claims, and prove your system's reasoning from the raw documents.

---

## Folder Layout

```
dev_pack/
├── README.md                  ← You are here
├── submission_schema.json     ← JSON Schema your agent must produce
├── submission_template.json   ← Blank starting template for your agent output
├── validate_submission.py     ← Run this locally before you submit
├── manifest.json              ← Document catalog (IDs, dates, formats, sectors)
├── hashes.sha256              ← File integrity checksums
├── sample_question.txt        ← The target query in plain text
└── docs/                      ← The document pool (76 files: TXT, PDF, DOCX)
    ├── ATL-0001 to ATL-0016   # Runemark Atlas — geography, country profiles, trade routes & outlet credibility tiers
    ├── VAN-0001 to VAN-0050   # Regional commercial records: export notices, customs filings, trade press & industry reports
    └── WLD-0001 to WLD-0010   # General newswire: public affairs, cultural dispatches & civic reporting
```

---

## What Your System Must Uncover

A successful system must autonomously solve challenges across the document pool:

**Event Verification**
Heimdall must confirm the disruption event is real and active as of the as-of date. Fake decoys, retracted notices, and planted injections exist in the corpus and must be caught before the trial begins.

**Opposing Exposure Cases**
Thor and Loki must each build a document-grounded case on opposite sides — high exposure vs. limited exposure — covering both Tolan and Midgard rice imports. Vague positions are not valid claims.

**Cross-Examination & Concessions**
Each side must attack the other's weakest claims with counter-evidence. Agents must either defend with new documents or concede. A system where no one ever concedes has not genuinely debated.

**Judicial Classification**
Odin must distinguish between sourced facts (directly stated in a document) and inferences (derived by reasoning). Every claim must receive a ruling and be classified as Established, Contested, or Conceded.

**Sufficiency Loop**
If the evidence base is thin after the first trial run, Odin returns it for a second round of retrieval. A minimum of two trial runs must be demonstrated.

**Final Intelligence Briefing**
Odin authors the final briefing from his rulings only — not from Thor or Loki's raw arguments. The briefing must include an exposure table (with separate Thor, Loki, and Odin ranges), inline paragraph-level citations, and a next-quarter outlook.

**Source Hygiene**
The corpus contains documents from four outlet credibility tiers (see `ATL-0012`). Your system must not treat a tabloid rumour or a retracted notice as established fact. The as-of date is **25 April 2027** — citing anything published after this date is a clock violation.

---

## Evaluation Rubric

Submissions are scored across seven criteria:

- **Citation Validity** — Do cited paragraphs resolve to real documents dated on or before the as-of date?
- **Range Accuracy** — Does the ground-truth exposure fall inside Thor's range, Loki's range, and Odin's final range?
- **Calibration** — How narrow is Odin's final range when it is correct? Very wide ranges receive no calibration credit.
- **Trap Handling** — Were fake decoy events caught, retractions detected, contradictions tagged as Contested, and prompt injections ignored?
- **Quality of Debate** — Was cross-examination genuine? Was new evidence introduced in defence? Were concessions made where the evidence demanded them?
- **Pipeline Reliability** — Did the pipeline ingest all formats (TXT, PDF, DOCX) gracefully, including intentionally damaged files, without crashing?
- **Reproducibility** — Can the briefing be traced back to the Case File, as-of date, and logged rulings?

---

## Quickstart

**Step 1 — Verify your sandbox files are intact:**
```bash
sha256sum -c hashes.sha256
```

**Step 2 — Build your agent system and produce `submission.json`.**
Use `submission_schema.json` as the contract and `submission_template.json` as your starting point.

**Step 3 — Validate before submitting:**
```bash
python validate_submission.py submission.json
```
A `[PASS]` result means your submission meets all structural requirements and is ready for judging.

---

## Attribution

The Runemark world, nations, trade routes, and document corpus are entirely fictional and created for this challenge. All companies, trade figures, and events are simulated.

The outlet credibility tier model in `ATL-0012` is inspired by standard source reliability frameworks used in intelligence and investigative journalism contexts.

*This dataset is for educational and competition use only.*
