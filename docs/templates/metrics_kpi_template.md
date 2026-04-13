# KPI/KRI Template

**Metric Name:** MFA Coverage  
**Control ID(s):** CTRL-AC-01  
**Owner:** Security Engineering  
**Collection Cadence:** Monthly  
**Target/Threshold:** ≥ 99%

## Definition
% of active workforce identities with MFA enabled.

## Data Sources
- IAM user directory
- SIEM authentication logs

## Calculation
`MFA Coverage = (Users with MFA enabled / Active Users) * 100`

## Reporting
- Dashboard: Security Ops
- Escalation on breach of threshold
