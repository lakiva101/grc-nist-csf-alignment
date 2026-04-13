# Overview: NIST CSF 2.0 Alignment Project

This project provides a reusable structure for aligning organizational controls to **NIST Cybersecurity Framework (CSF) 2.0**.  
It includes framework scaffolding, templates, example mappings, and scripts for validation and reporting.

## What This Repository Includes
- A NIST CSF 2.0 catalog scaffold (Functions → Categories → Subcategories)
- Organizational control definitions (YAML)
- Mapping of CSF subcategories to organizational controls (CSV)
- Scripts to validate mapping completeness and generate gap reports
- Documentation and templates for policies, evidence, and metrics

## Why This Is Useful
- Standardizes CSF alignment work
- Helps identify control gaps and missing evidence
- Makes audits and assessments faster
- Supports compliance, GRC, and cybersecurity maturity work

## Core Components
1. **Framework Catalog**  
   Located in: `frameworks/nist_csf_2_0/catalog/nist_csf_2_0_catalog.yaml`  
   Defines the CSF 2.0 functions, categories, and subcategories.

2. **Organization Controls**  
   Located in: `mappings/org_controls.yaml`  
   Contains your control IDs, description, evidence, and metrics.

3. **CSF Mapping**  
   Located in: `mappings/mapping_nist_to_org.csv`  
   Maps each CSF subcategory to one or more controls with coverage levels.

4. **Automation Scripts**  
   Located in: `scripts/`  
   - `validate_mapping.py` checks mapping structure  
   - `generate_gap_report.py` creates a gap analysis report

## How to Use
1. Complete the CSF catalog with the official subcategory text.
2. Add your organizational controls in `org_controls.yaml`.
3. Map controls to CSF subcategories in `mapping_nist_to_org.csv`.
4. Run the scripts to validate and generate gap reports.
5. Use the templates to build policies, evidence records, and metrics.
