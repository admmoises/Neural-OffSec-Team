# OWASP Top 10 (2021) - Testing Checklist

**Engagement:** {{ENGAGEMENT_NAME}}
**Target:** {{TARGET}}
**Tester:** {{TESTER_NAME}}

## A01:2021 – Broken Access Control

- [ ] **Vertical Privilege Escalation**
  - [ ] Access admin functions as regular user
  - [ ] Modify user roles/permissions
  - [ ] Access restricted resources by URL manipulation

- [ ] **Horizontal Privilege Escalation**
  - [ ] Access other users' data by changing user ID
  - [ ] IDOR (Insecure Direct Object References)
  - [ ] Tamper with API endpoints

- [ ] **Path Traversal**
  - [ ] Directory traversal (../, ../../)
  - [ ] File inclusion attacks

## A02:2021 – Cryptographic Failures

- [ ] **Data in Transit**
  - [ ] HTTPS enforced on all pages
  - [ ] Strong TLS version (TLS 1.2+)
  - [ ] Secure cipher suites
  - [ ] HSTS header present

- [ ] **Data at Rest**
  - [ ] Passwords hashed with strong algorithm (bcrypt, Argon2)
  - [ ] Sensitive data encrypted
  - [ ] No hardcoded secrets/keys

- [ ] **Weak Crypto**
  - [ ] Check for MD5/SHA1 usage
  - [ ] Weak random number generation

## A03:2021 – Injection

- [ ] **SQL Injection**
  - [ ] Test all input fields, parameters, headers
  - [ ] Boolean-based blind SQLi
  - [ ] Time-based blind SQLi
  - [ ] Union-based SQLi
  - [ ] Error-based SQLi
  - [ ] Second-order SQLi

- [ ] **NoSQL Injection**
  - [ ] MongoDB injection
  - [ ] JSON-based injection

- [ ] **Command Injection**
  - [ ] OS command injection
  - [ ] Shell metacharacter injection

- [ ] **LDAP/XPath Injection**

- [ ] **Template Injection (SSTI)**

## A04:2021 – Insecure Design

- [ ] **Threat Modeling**
  - [ ] Identify critical business flows
  - [ ] Test security controls in design

- [ ] **Business Logic Flaws**
  - [ ] Purchase negative quantities
  - [ ] Race conditions
  - [ ] Workflow bypass
  - [ ] Price manipulation

## A05:2021 – Security Misconfiguration

- [ ] **Information Disclosure**
  - [ ] Detailed error messages
  - [ ] Stack traces exposed
  - [ ] Server version disclosure
  - [ ] Directory listing enabled

- [ ] **Default Configurations**
  - [ ] Default credentials
  - [ ] Default ports/services
  - [ ] Sample applications present

- [ ] **Security Headers**
  - [ ] X-Content-Type-Options
  - [ ] X-Frame-Options
  - [ ] Content-Security-Policy
  - [ ] X-XSS-Protection
  - [ ] Referrer-Policy

## A06:2021 – Vulnerable and Outdated Components

- [ ] **Dependency Analysis**
  - [ ] Identify all client/server components
  - [ ] Check for known vulnerabilities (CVE)
  - [ ] Verify versions against latest secure versions

- [ ] **npm/pip/composer Vulnerabilities**
  - [ ] Run vulnerability scanners
  - [ ] Check transitive dependencies

## A07:2021 – Identification and Authentication Failures

- [ ] **Password Policy**
  - [ ] Weak password acceptance
  - [ ] No password complexity requirements
  - [ ] No password history

- [ ] **Session Management**
  - [ ] Session fixation
  - [ ] Session ID in URL
  - [ ] No session timeout
  - [ ] Insecure session cookies (no HttpOnly, Secure, SameSite)

- [ ] **Brute Force**
  - [ ] No rate limiting on login
  - [ ] No account lockout
  - [ ] No CAPTCHA

- [ ] **MFA Bypass**
  - [ ] MFA not enforced
  - [ ] MFA code reuse possible

## A08:2021 – Software and Data Integrity Failures

- [ ] **Unsigned Code/Updates**
  - [ ] CI/CD pipeline security
  - [ ] No integrity checks on downloaded libraries

- [ ] **Insecure Deserialization**
  - [ ] Test for serialized objects in cookies/parameters
  - [ ] Tamper with serialized data

## A09:2021 – Security Logging and Monitoring Failures

- [ ] **Logging**
  - [ ] Security events logged (login attempts, access denials)
  - [ ] Log injection possible
  - [ ] Sensitive data in logs

- [ ] **Monitoring**
  - [ ] Alerting on suspicious activities
  - [ ] Log retention policy

## A10:2021 – Server-Side Request Forgery (SSRF)

- [ ] **SSRF Testing**
  - [ ] Test URL parameters for internal resource access
  - [ ] Access cloud metadata (169.254.169.254)
  - [ ] Port scanning via SSRF
  - [ ] Blind SSRF detection

---

## Coverage Summary

**Total Items:** {{TOTAL_ITEMS}}
**Tested:** {{TESTED_COUNT}}
**Vulnerabilities Found:** {{VULN_COUNT}}
**Coverage:** {{COVERAGE_PERCENTAGE}}%

**Findings:**
- 🔴 Critical: {{CRITICAL_COUNT}}
- 🟠 High: {{HIGH_COUNT}}
- 🟡 Medium: {{MEDIUM_COUNT}}
- 🟢 Low: {{LOW_COUNT}}
