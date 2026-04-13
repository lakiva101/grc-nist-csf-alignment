#!/usr/bin/env python3
"""
Validate mapping_nist_to_org.csv for required columns and allowed values.
"""

import csv
import sys

REQUIRED_COLS = [
    "function", "category", "subcategory_id", "subcategory_name",
    "org_control_id", "coverage_level", "rationale", "evidence_link", "owner"
]
ALLOWED_COVERAGE = {"Full", "Partial", "None"}

def main(path="mappings/mapping_nist_to_org.csv"):
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            missing = [c for c in REQUIRED_COLS if c not in reader.fieldnames]
            if missing:
                print(f"❌ Missing required columns: {missing}")
                sys.exit(1)

            ok = True
            for i, row in enumerate(reader, start=2):
                cov = row["coverage_level"].strip()
                if cov not in ALLOWED_COVERAGE:
                    print(f"❌ Line {i}: invalid coverage_level '{cov}'. Allowed: {ALLOWED_COVERAGE}")
                    ok = False
                for col in REQUIRED_COLS:
                    if not str(row[col]).strip():
                        print(f"❌ Line {i}: empty required field '{col}'")
                        ok = False

            if ok:
                print("✅ mapping_nist_to_org.csv looks valid.")
                sys.exit(0)
            else:
                sys.exit(1)

    except FileNotFoundError:
        print(f"❌ File not found: {path}")
        sys.exit(1)

if __name__ == "__main__":
    main()
