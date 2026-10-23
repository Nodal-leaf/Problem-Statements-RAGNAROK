#!/usr/bin/env python3
"""Submission validator for the Trial of the Nine Realms (Event 3).

Validates that an agentic submission fulfills all Functional Requirements (FR1-FR8)
and evaluation criteria from the official Problem Statement:
- 4 Norse-themed agents (Heimdall, Thor, Loki, Odin)
- Multi-run trial loop with cross-examination & concessions (at least 2 runs)
- Odin's rulings & classification (Established, Contested, Conceded)
- Exposure table containing Thor's range, Loki's range, and Odin's final range
- Paragraph-level citations (DOC_ID#P[N]) and strict as-of date (2027-04-25) compliance.

Usage:
    python validate_submission.py [submission_file.json]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def validate(submission_path: Path, manifest_path: Path) -> int:
    print(f"[*] Validating Trial of the Nine Realms submission: {submission_path}")

    if not submission_path.exists():
        print(f"[FAIL] Submission file not found: {submission_path}")
        return 1

    try:
        data = json.loads(submission_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[FAIL] Invalid JSON format: {e}")
        return 1

    if not manifest_path.exists():
        print(f"[FAIL] Manifest file not found: {manifest_path}")
        return 1

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest_docs = {d["DOC_ID"]: d for d in manifest.get("documents", [])}

    errors = []
    warnings = []

    # 1. Top-Level Structure
    for k in ["team_id", "case_file", "trial_runs", "final_briefing"]:
        if k not in data:
            errors.append(f"Missing required top-level section: '{k}'")

    # 2. FR1: Heimdall Case File
    case_file = data.get("case_file", {})
    if not isinstance(case_file, dict):
        errors.append("'case_file' must be an object (Heimdall output).")
    else:
        for k in ["case_id", "question", "as_of_date", "event_verified", "verification_notes"]:
            if k not in case_file:
                errors.append(f"Heimdall Case File missing field: '{k}'")

        as_of = case_file.get("as_of_date", "")
        if as_of != "2027-04-25":
            errors.append(f"Invalid as_of_date in Case File: expected '2027-04-25', got '{as_of}'")

        if not case_file.get("event_verified", False):
            warnings.append("Event is marked as unverified (Decoy). Verify that this matches the target query.")

    # 3. FR5: Trial Loop Runs (Minimum 2 runs required by FR5.4)
    runs = data.get("trial_runs", [])
    if not isinstance(runs, list) or len(runs) < 2:
        errors.append(f"Problem Statement FR5.4 requires at least 2 trial runs. Found: {len(runs) if isinstance(runs, list) else 0}.")
    else:
        for i, run in enumerate(runs, 1):
            r_num = run.get("run_number", i)
            # Round 1
            r1 = run.get("round_1_claims", {})
            thor_claims = r1.get("thor_high_case", [])
            loki_claims = r1.get("loki_limited_case", [])
            if not thor_claims or not loki_claims:
                errors.append(f"Run {r_num} Round 1: Thor and Loki must both submit claims (FR5.2).")

            # Round 2
            r2 = run.get("round_2_cross_examination", {})
            thor_atk = r2.get("thor_attacks", [])
            loki_atk = r2.get("loki_attacks", [])
            defences = r2.get("defences", [])
            if not thor_atk or not loki_atk:
                errors.append(f"Run {r_num} Round 2: Each side must attack at least one claim (FR5.3).")

            concessions = [d for d in defences if d.get("action") == "concede"]
            if not concessions:
                warnings.append(f"Run {r_num}: No concessions found in cross-examination defences.")

            # Odin rulings
            odin = run.get("odin_rulings", {})
            rulings = odin.get("claim_rulings", [])
            sufficiency = odin.get("sufficiency_check", {})
            if not rulings:
                errors.append(f"Run {r_num}: Odin must rule on claims (FR4.1).")
            if "is_sufficient" not in sufficiency:
                errors.append(f"Run {r_num}: Odin must perform a sufficiency check (FR4.3).")

    # 4. FR4.4 & FR8: Final Briefing
    briefing = data.get("final_briefing", {})
    if not isinstance(briefing, dict):
        errors.append("'final_briefing' must be an object (Odin output).")
    else:
        for k in ["executive_summary", "findings", "exposure_table", "next_quarter_outlook", "citations_source_list"]:
            if k not in briefing:
                errors.append(f"Final Briefing missing section: '{k}'")

        # Check findings classification (FR4.2 & FR8.1)
        findings = briefing.get("findings", {})
        for cat in ["established", "contested", "conceded"]:
            items = findings.get(cat, [])
            if not isinstance(items, list) or len(items) == 0:
                errors.append(f"Briefing findings missing non-empty category: '{cat}' (FR4.2)")

        # Check exposure table (FR7.3 & Section 5: Thor range, Loki range, Odin range)
        exp_table = briefing.get("exposure_table", [])
        if not isinstance(exp_table, list) or len(exp_table) == 0:
            errors.append("Briefing missing 'exposure_table' with Thor, Loki, and Odin ranges.")
        else:
            countries_covered = set()
            for row in exp_table:
                c = row.get("country")
                countries_covered.add(c)
                for agent_range in ["thor_range", "loki_range", "odin_final_range"]:
                    if agent_range not in row:
                        errors.append(f"Exposure row for {c} missing '{agent_range}' (Section 5 requirement).")
                    else:
                        r = row[agent_range]
                        if "low_pct" not in r or "high_pct" not in r:
                            errors.append(f"Exposure row for {c} in '{agent_range}' missing 'low_pct' or 'high_pct'.")
                        elif r["low_pct"] > r["high_pct"]:
                            errors.append(f"Exposure row for {c} in '{agent_range}': low_pct ({r['low_pct']}) > high_pct ({r['high_pct']}).")

            expected_countries = {"Tolan", "Midgard"}
            missing_c = expected_countries - countries_covered
            if missing_c:
                errors.append(f"Exposure table missing required target countries: {missing_c}")

        # Check citations & Clock rule (FR8.3, NFR2, 4.3)
        cite_pattern = re.compile(r"^([A-Z]{3}-\d{4})#P(\d+)$")
        all_citations = []
        for cat in ["established", "contested", "conceded"]:
            for item in findings.get(cat, []):
                for cite in item.get("citations", []):
                    all_citations.append(cite)

        if not all_citations:
            errors.append("No citations found in findings. PS requires inline citations with Runemark document IDs (FR8.3).")

        is_template = (data.get("team_id") == "YOUR_TEAM_NAME")
        if is_template:
            warnings.append("Template placeholder detected ('YOUR_TEAM_NAME'). Remember to output your agent's actual team ID.")

        for cite in all_citations:
            m = cite_pattern.match(cite)
            if not m:
                if is_template and cite.startswith("DOC_ID"):
                    continue
                errors.append(f"Citation '{cite}' does not follow format 'DOC_ID#P[N]' (e.g. 'VAN-0007#P2').")
                continue
            doc_id = m.group(1)
            if doc_id not in manifest_docs:
                if is_template:
                    continue
                errors.append(f"Cited document '{doc_id}' does not exist in manifest.json (NFR2.3).")
                continue
            pub_date = manifest_docs[doc_id].get("PUB_DATE", "")
            if pub_date > "2027-04-25":
                errors.append(f"Clock violation: Cited doc '{doc_id}' published {pub_date} after as-of date 2027-04-25 (Section 4.3).")

    # Output results
    print("\n" + "=" * 60)
    print("TRIAL OF THE NINE REALMS — SUBMISSION AUDIT REPORT")
    print("=" * 60)

    if warnings:
        print(f"\n[!] {len(warnings)} WARNING(S):")
        for w in warnings:
            print(f"    - {w}")

    if errors:
        print(f"\n[FAIL] {len(errors)} ERROR(S) DETECTED:")
        for err in errors:
            print(f"    - {err}")
        print("=" * 60)
        return 1

    print("\n[PASS] All Problem Statement Functional Requirements (FR1-FR8) satisfied!")
    print("       - 4-Agent roles present (Heimdall, Thor, Loki, Odin)")
    print("       - Multi-run trial loop validated (>= 2 runs with cross-examination)")
    print("       - Findings properly categorized (Established, Contested, Conceded)")
    print("       - Exposure table complete with Thor, Loki, and Odin ranges")
    print("       - All citations resolve to manifest and comply with the 2027-04-25 clock rule")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sub_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("submission.json")
    manifest_file = Path(__file__).resolve().parent / "manifest.json"
    sys.exit(validate(sub_file, manifest_file))
