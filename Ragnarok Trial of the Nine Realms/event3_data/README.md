# Runemark Dev Pack — Autonomous Trade Intelligence Challenge (Event 3)

## The Mission

You are tasked with building an autonomous trade and supply-chain intelligence engine for **Runemark**, a multi-nation economic zone comprising twelve trading nations distributed across the West, East, and Inner Seas.

In late 2026, **Vanir**—the region's primary agricultural powerhouse—abruptly enacted a sweeping export ban on rice. The disruption has sent shockwaves through regional food supply chains, maritime shipping lanes, spot commodities markets, and bilateral trade balances. Importers such as **Tolan** and **Midgard** face immediate supply uncertainties, while secondary producers like **Valhalla** are adjusting output and prices in response.

Your system must ingest this repository, examine the multi-format document pool, filter through peripheral noise and deceptive market rumors, withstand corrupted files, track temporal timelines strictly against the as-of date (**25 April 2027**), and calculate the true exposure ranges for affected importing nations.

**There is no spoon-fed schema or pre-baked answer key.** You and your team must design the architecture, discover the bilateral diplomatic exemptions, trace third-party trade substitutions, isolate official truth from biased commentary, and prove your system's intelligence from the raw files.

---

## Folder Layout

```
event3_data/
├── README.md                          ← You are here
├── sample_question.txt                ← Target evaluation challenge & as-of date (2027-04-25)
├── manifest.json                      ← Public metadata catalog (IDs, dates, source types, sectors)
├── hashes.sha256                      ← SHA-256 cryptographic checksums for all 76 document files
└── docs/                              ← The document pool (76 files: 35 TXT, 27 PDF, 14 DOCX)
    ├── VAN-0001 to VAN-0050           # Event 3 records: trade notes, customs notices, press & traps
    ├── ATL-0001 to ATL-0016           # Runemark Atlas: geography, normal baselines & outlet credibility
    └── WLD-0001 to WLD-0010           # Background noise: sports, culture & everyday civic news
```

---

## What Your System Must Uncover

A successful intelligence system must autonomously solve key challenges across the document pool:

1. **Baseline vs. Crisis Deviation:** Accurately derive peacetime trade baselines from historical trade notes and quantify the real percentage gap in import volume and value.
2. **Diplomatic & Bilateral Exemptions:** Uncover formal Government-to-Government (G2G) contractual carve-outs that exempt specific trade partners from headline ban figures.
3. **Third-Party Market Substitution:** Trace how secondary suppliers (such as Valhalla) respond to fill supply deficits and measure the corresponding price surges.
4. **Temporal Clocks & As-Of Filtering:** Respect the strict as-of date (`2027-04-25`), filtering out subsequent trade developments and post-dated commentary.
5. **Source Credibility & Trap Inoculation:** Cross-reference the Atlas Outlet Guide ([`ATL-0012`](file:///e:/RAGNAROK/EnviroPool/event3_data/docs/ATL-0012.txt)) to dismiss sensationalist tabloids, unverified social media chatter, retracted reports, and adversarial prompt injections.
6. **Data Hygiene & Parser Resilience:** Ingest heterogeneous formats (TXT, native text PDF, DOCX) and gracefully handle intentionally damaged, truncated, or malformed files without pipeline crashes.
7. **Exact Evidence Citation:** Attribute every claim, range, and finding down to the immutable paragraph level (`DOC_ID#P[N]`).

---

## Document Format & Citation Rules

Every document in `docs/` begins with a standardized metadata header separated from the body by three dashes:

```text
DOC_ID: VAN-0007
EVENT_ID: E3
TITLE: Gazette publishes rice export restriction decree
SOURCE_NAME: Realm Trade Ministry
SOURCE_TYPE: gov_notice
RELIABILITY: 1
PUB_DATE: 2026-12-14
PUB_TIME: 10:00
COUNTRY: Vanir
SECTOR: rice
LANGUAGE: en
---
[P1] Paragraph text...

[P2] Paragraph text...
```

* **Citation Standard:** Cite evidence using `DOC_ID#P[N]` (e.g. `VAN-0007#P2`).
* **Format Mix:** 35 TXT, 27 PDF, 14 DOCX. All undamaged PDFs are pure vector text—no OCR is needed.
* **Integrity:** Use `hashes.sha256` to verify your local files against intentional benchmark damage.

---

## Attribution & Simulation Notice

*This dataset, including the Runemark geopolitical setting, all nations, companies, trade authorities, individuals, and economic statistics, is entirely simulated for benchmarking and evaluation purposes.*
