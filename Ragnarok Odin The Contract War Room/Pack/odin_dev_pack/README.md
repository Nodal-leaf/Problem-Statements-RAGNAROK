# Odin Dev Pack — Quillhub Autonomous Contract Intelligence Challenge

## The Mission

You are tasked with building an autonomous contract intelligence engine for **Quillhub Inc.**, a B2B SaaS company that provides an enterprise route optimization platform called **Route Optimizer**. 

Quillhub has grown quickly, executing multiple commercial agreements across upstream cloud hosting providers, enterprise retail customers, logistics distribution partners, and specialized contractor agencies. However, these agreements were negotiated independently over time, creating hidden legal contradictions, financial liabilities, operational mismatches, and compliance vulnerabilities.

Your system must ingest this repository, analyze the portfolio holistically, monitor incoming operational events across time checkpoints, and surface critical risks, deadlines, and financial exposures.

**There is no spoon-fed schema or pre-baked answer key.** You and your team must design the architecture, discover the contractual relationships, trace the financial leaks, and prove your system's intelligence from the raw files.

---

## Folder Layout

```
odin_dev_pack/
├── README.md                          ← You are here
├── clock.json                         ← Simulated time clock with 3 checkpoint dates
├── generate_pdfs.py                   ← Utility to generate matching PDF twins
├── docs/
│   └── format_spec.md                 ← Input specifications, drop model, and citation rules
└── bundle/
    ├── manifest.json                  ← File list and titles (no relationships revealed)
    ├── company/
    │   └── context.txt                ← Quillhub business profile, addresses, corporate facts
    ├── contracts/
    │   ├── STD.txt & STD.pdf          # Master Standard Terms (incorporated by reference)
    │   ├── A1.txt & A1.pdf            # Upstream Cloud Hosting Agreement
    │   ├── A2.txt & A2.pdf            # Upstream Service Level Agreement (SLA)
    │   ├── A3.txt & A3.pdf            # SLA Amendment No. 1
    │   ├── B1.txt & B1.pdf            # Enterprise Retail Customer Agreement
    │   ├── B2.txt & B2.pdf            # Data Processing & Security Addendum
    │   ├── C1.txt & C1.pdf            # Logistics Customer Agreement
    │   └── D1.txt & D1.pdf            # Independent Contractor Agreement
    ├── data/
    │   ├── payments_ledger.csv        # Historical transaction payments & invoices
    │   └── holidays.csv               # Observed business holidays
    └── events/
        ├── events_drop1.jsonl         # Operational communications & incidents (Drop 1)
        └── events_drop2.jsonl         # Operational communications & incidents (Drop 2)
```

---

## What Your System Must Uncover

A successful system must autonomously solve key challenges across the portfolio:

1. **Cross-Contract Contradictions & Territorial Conflicts**:
   - Detect where separate agreements make incompatible promises to different commercial partners (e.g., exclusivity rights, geographic restrictions, or contradictory commitments).

2. **Upstream vs. Downstream Financial Recovery Gaps**:
   - Trace how outages in upstream infrastructure cascade into customer SLA claims.
   - Calculate whether penalties Quillhub owes downstream can actually be recovered from upstream providers, or if Quillhub is left absorbing unrecoverable losses out of pocket.

3. **Silent Amendment Supersession**:
   - Understand how later amendments silently overwrite earlier rules, change notice periods, and shorten critical claim deadlines.

4. **Hidden External Defaults & Lapsed Policies**:
   - Cross-examine internal company records against customer requirements to identify silent, continuous material breaches of contract.

5. **Timeline & Obligation Tracking**:
   - As the simulated clock advances through checkpoints (`March 15, 2027`, `June 1, 2027`, `September 15, 2027`), determine what obligations are upcoming, due, or overdue.
   - Accurately calculate date math, differentiating calendar days from business days (excluding weekends and observed holidays).

6. **Event Monitoring & Action Drafting**:
   - Ingest real-time incident reports, customer emails, and deliverable submissions. Filter operational noise from actionable contractual events, calculate uptime percentages, and generate formal claim/notice drafts.

7. **Data Hygiene & Resilience**:
   - Real-world contract portfolios contain imperfect data. The dataset includes truncated files, blank executed fields, and malformed records. Your system must handle these gracefully, flag issues, and never hallucinate missing facts.

---

## Core Rules

1. **Strict Verbatim Citations**:
   - Any claim, deadline, or risk your system reports must cite:
     - The Contract ID (e.g. `A1`, `B1`, `STD`)
     - The Section or Clause reference (e.g. `§3.1`, `Special Terms §1`)
     - An exact verbatim quote from the `.txt` file that can be verified via direct text search.

2. **Grounded Reasoning Only (No Hallucinations)**:
   - Your system must explain:
     - **Who did what** (the factual event or outage)
     - **Why it matters under the contract** (the specific clause or threshold triggered)
     - **The legal and financial consequence** (who owes what to whom)
   - Do not invent outside background drama or unstated assumptions. All reasoning must stem strictly from the provided text and events.

3. **Canonical Text Anchor**:
   - The `.txt` files are the canonical text anchors for all citations. Matching `.pdf` twins are provided for realistic document inspection.

4. **Event Name Resolution**:
   - Events refer to parties and people by informal names (e.g., *"Jordan Hale"*, *"StratoNode"*, *"Harbor"*), not contract IDs. Your system must resolve these entities.

---

## Attribution

The Standard Terms in `STD.txt` are adapted from the Common Paper Cloud Service Agreement Standard Terms Version 2.0 under CC BY 4.0. Modifications were made to section numbering, defined terms, and provisions to fit this scenario. Original: https://commonpaper.com/standards/cloud-service-agreement/2.0/

*This dataset is entirely fictional. All companies, individuals, financial amounts, and contract terms are simulated for testing.*
