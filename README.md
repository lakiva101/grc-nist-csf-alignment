# grc-nist-csf-alignment
Provide a reusable framework to map organizational controls to NIST CSF 2.0, track coverage, identify gaps, and produce lightweight reports for stakeholders and audits.
grc-nist-csf-alignment/
├─ README.md
├─ LICENSE
├─ docs/
│  ├─ overview.md
│  └─ usage.md
├─ frameworks/
│  └─ nist_csf_2_0/
│     ├─ functions/
│     │  ├─ govern.md
│     │  ├─ identify.md
│     │  ├─ protect.md
│     │  ├─ detect.md
│     │  ├─ respond.md
│     │  └─ recover.md
│     └─ catalog/
│        └─ nist_csf_2_0_catalog.yaml
├─ mappings/
│  ├─ org_controls.yaml
│  ├─ mapping_nist_to_org.csv
│  └─ examples/
│     └─ sample_mapping.csv
├─ templates/
│  ├─ control_statement.md
│  ├─ evidence_request_form.md
│  ├─ metrics_kpi_template.md
│  └─ policy_template.md
├─ scripts/
│  ├─ validate_mapping.py
│  └─ generate_gap_report.py
└─ .github/
   └─ workflows/
      └─ validate-mapping.yml
