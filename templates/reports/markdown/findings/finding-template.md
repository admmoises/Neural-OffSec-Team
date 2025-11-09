---
finding_id: {{FINDING_ID}}
title: "{{FINDING_TITLE}}"
severity: {{SEVERITY}}
cvss_score: {{CVSS_SCORE}}
cvss_vector: {{CVSS_VECTOR}}
cwe: {{CWE_ID}}
status: {{STATUS}}
---

## {{FINDING_ID}}: {{FINDING_TITLE}}

**Severity:** {{SEVERITY_EMOJI}} {{SEVERITY}} (CVSS {{CVSS_SCORE}})
**CVSS Vector:** `{{CVSS_VECTOR}}`
**CWE:** {{CWE_ID}} - {{CWE_NAME}}
**Affected Component:** {{AFFECTED_COMPONENT}}

---

### Description

{{TECHNICAL_DESCRIPTION}}

**Why This Matters:**
{{BUSINESS_IMPACT_EXPLANATION}}

---

### Impact

**Confidentiality:** {{CONFIDENTIALITY_IMPACT}} (None / Low / High)
**Integrity:** {{INTEGRITY_IMPACT}} (None / Low / High)
**Availability:** {{AVAILABILITY_IMPACT}} (None / Low / High)

**Attack Complexity:** {{ATTACK_COMPLEXITY}} (Low / High)
**Privileges Required:** {{PRIVILEGES_REQUIRED}} (None / Low / High)
**User Interaction:** {{USER_INTERACTION}} (None / Required)

**Business Impact:**
{{BUSINESS_IMPACT}}

**Potential Attacker Goals:**
- {{ATTACKER_GOAL_1}}
- {{ATTACKER_GOAL_2}}
- {{ATTACKER_GOAL_3}}

---

### Proof of Concept

**Location:** {{VULNERABILITY_LOCATION}}
**Vulnerable Parameter/Endpoint:** {{VULNERABLE_PARAMETER}}

**Steps to Reproduce:**

1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}
4. {{STEP_4}}

**Request:**
```http
{{HTTP_REQUEST}}
```

**Response:**
```http
{{HTTP_RESPONSE}}
```

**Evidence:**
![{{EVIDENCE_DESCRIPTION}}]({{SCREENSHOT_PATH}})

**Payload Used:**
```
{{PAYLOAD}}
```

---

### Remediation

#### Immediate Actions (Quick Fix)

{{QUICK_FIX_STEPS}}

#### Long-term Solution (Secure Implementation)

{{LONG_TERM_FIX}}

**Code Example (Secure):**
```{{LANGUAGE}}
{{SECURE_CODE_EXAMPLE}}
```

**Configuration Changes:**
```
{{CONFIGURATION_CHANGES}}
```

---

### Verification Steps

After remediation, verify the fix with these steps:

1. {{VERIFICATION_STEP_1}}
2. {{VERIFICATION_STEP_2}}
3. {{VERIFICATION_STEP_3}}

**Expected Result:** {{EXPECTED_RESULT_AFTER_FIX}}

---

### References

- **OWASP:** {{OWASP_REFERENCE}}
- **CWE:** https://cwe.mitre.org/data/definitions/{{CWE_ID}}.html
- **CVSS Calculator:** https://www.first.org/cvss/calculator/3.1#{{CVSS_VECTOR}}
- **Additional Resources:**
  - {{REFERENCE_1}}
  - {{REFERENCE_2}}

---

### Timeline

- **Discovered:** {{DISCOVERY_DATE}} {{DISCOVERY_TIME}} BRT
- **Reported:** {{REPORT_DATE}}
- **Remediation Deadline:** {{REMEDIATION_DEADLINE}}
- **Verified Fixed:** {{VERIFICATION_DATE}} (if applicable)

---

### Evidence Chain of Custody

```yaml
timestamp: {{TIMESTAMP_BRT}}
engagement: {{ENGAGEMENT_PATH}}
finding: {{FINDING_ID}}
tool: {{TOOL_USED}}
operator: {{OPERATOR_NAME}}
screenshots:
  - {{SCREENSHOT_1}}
  - {{SCREENSHOT_2}}
pcaps:
  - {{PCAP_FILE}}
scripts:
  - {{POC_SCRIPT}}
hash_sha256: {{EVIDENCE_HASH}}
```

---

**Classification:** CONFIDENTIAL
**Finding ID:** {{FINDING_ID}}
**Last Updated:** {{LAST_UPDATED}}
