# NIST CSF 2.0 Alignment

This repository helps you align organizational controls to the **NIST Cybersecurity Framework (CSF) 2.0**. It includes:
- A catalog scaffold for CSF Functions and Categories
- Templates for control statements, evidence, and KPIs
- CSV/YAML mapping of CSF subcategories to organizational controls
- Scripts to validate mappings and generate gap reports

> **Note**: CSF 2.0 adds the **Govern (GV)** Function. Use NIST’s official CSF 2.0 Core to populate exact subcategory names/IDs before formal reporting.

## Why this repo?
- Standardize alignment work across teams
- Make audits and stakeholder reporting faster
- Provide living documentation with metrics and evidence hooks

## Quick Start
1. Copy the repo.
2. Fill `frameworks/nist_csf_2_0/catalog/nist_csf_2_0_catalog.yaml` with the official CSF 2.0 core (Functions → Categories → Subcategories).
3. Add your internal controls to `mappings/org_controls.yaml`.
4. Map CSF subcategories to org controls in `mappings/mapping_nist_to_org.csv`.
5. Run:
   ```bash
   python scripts/validate_mapping.py
   python scripts/generate_gap_report.py

