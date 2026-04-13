# Control Statement

**Control ID:** CTRL-AC-01  
**Name:** Access Control – MFA Enforcement  
**Type:** Technical / Process  
**Owner:** Security Engineering  
**Policy Link:** `/templates/policy_template.md` (or internal link)

## Purpose
Ensure strong authentication and least privilege access across critical systems.

## Procedure
1. MFA enabled for all workforce identities.
2. Privileged accounts require step-up MFA.
3. Quarterly access reviews for critical assets.

## Artifacts / Evidence
- IAM configuration export (date)
- Access review tickets / sign-off
- SIEM logs showing MFA events

## Metrics (KPIs/KRIs)
- % workforce with MFA enabled (target ≥ 99%)
- # privileged accounts without MFA (target = 0)
- # overdue access reviews (target = 0)

## Mapped Standards
- NIST CSF 2.0: Protect → Access Control (PR-AC-01/02)
- (Optional) CIS v8 IG controls, ISO 27001 A.9, etc.

## Exceptions
Document business exceptions with compensating controls and expiry date.
