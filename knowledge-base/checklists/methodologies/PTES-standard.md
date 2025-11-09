# PTES (Penetration Testing Execution Standard)

Metodologia padrão para execução de pentests profissionais.

## 1. Pre-Engagement Interactions

### 1.1 Scoping
- [ ] Define in-scope targets (IPs, domains, applications)
- [ ] Define out-of-scope items
- [ ] Identify time windows for testing
- [ ] Establish Rules of Engagement (RoE)
- [ ] Obtain authorization letter

### 1.2 Legal and Administrative
- [ ] NDA signed
- [ ] Statement of Work (SoW) signed
- [ ] Insurance verification
- [ ] Emergency contacts established
- [ ] Communication protocols defined

### 1.3 Intelligence Gathering Goals
- [ ] Define data to be collected
- [ ] Define collection methods
- [ ] Define analysis approach

## 2. Intelligence Gathering (Reconnaissance)

### 2.1 OSINT (Open Source Intelligence)
- [ ] Company information (WHOIS, business registration)
- [ ] Employee information (LinkedIn, social media)
- [ ] Technology stack identification
- [ ] DNS enumeration
- [ ] Subdomain discovery
- [ ] Certificate transparency logs
- [ ] Google dorking
- [ ] Shodan/Censys searches

### 2.2 Infrastructure Analysis
- [ ] Network range identification
- [ ] Port scanning (nmap_scan)
- [ ] Service enumeration
- [ ] OS fingerprinting
- [ ] Technology versions

### 2.3 Service Enumeration
- [ ] HTTP/HTTPS (web servers, frameworks)
- [ ] Email (SMTP, POP3, IMAP)
- [ ] DNS servers
- [ ] Database services
- [ ] File sharing (SMB, NFS, FTP)
- [ ] Remote access (SSH, RDP, VNC)

### 2.4 Application Enumeration
- [ ] Web application mapping
- [ ] API endpoints discovery
- [ ] Hidden directories/files (gobuster_scan)
- [ ] Parameter discovery
- [ ] Technology stack (Wappalyzer)

## 3. Threat Modeling

### 3.1 Asset Identification
- [ ] Critical business assets
- [ ] Data classification
- [ ] System dependencies
- [ ] Trust boundaries

### 3.2 Attack Surface Analysis
- [ ] External attack surface
- [ ] Internal attack surface
- [ ] User entry points
- [ ] Integration points

### 3.3 Threat Scenarios
- [ ] External attacker
- [ ] Insider threat
- [ ] Supply chain attack
- [ ] Social engineering

## 4. Vulnerability Analysis

### 4.1 Automated Scanning
- [ ] Network vulnerability scanning
- [ ] Web application scanning (nikto_scan)
- [ ] Dependency scanning
- [ ] Configuration review

### 4.2 Manual Testing
- [ ] Authentication testing
- [ ] Authorization testing
- [ ] Input validation (SQLi, XSS, etc.)
- [ ] Business logic flaws
- [ ] Session management
- [ ] Cryptography review

### 4.3 Vulnerability Validation
- [ ] Verify scanner findings
- [ ] Eliminate false positives
- [ ] Assess exploitability
- [ ] Determine impact

## 5. Exploitation

### 5.1 Precision Strike
- [ ] Target specific vulnerabilities
- [ ] Develop/adapt exploits
- [ ] Execute PoC
- [ ] Document evidence

### 5.2 Customized Exploitation
- [ ] Custom payloads
- [ ] Bypass security controls
- [ ] Pivot techniques
- [ ] Persistence mechanisms

### 5.3 Zero-Day Research (if in scope)
- [ ] Fuzzing
- [ ] Reverse engineering
- [ ] Custom exploit development

## 6. Post-Exploitation

### 6.1 Infrastructure Analysis
- [ ] Network topology mapping
- [ ] Trust relationships
- [ ] Security controls inventory

### 6.2 Privilege Escalation
- [ ] Vertical privilege escalation
- [ ] Horizontal privilege escalation
- [ ] Kernel exploits
- [ ] Misconfigurations

### 6.3 Maintaining Access
- [ ] Backdoor installation (authorized only)
- [ ] Tunneling
- [ ] Covert channels

### 6.4 Data Exfiltration Simulation
- [ ] Identify sensitive data
- [ ] Demonstrate access (DO NOT exfiltrate actual data)
- [ ] Document data classification

### 6.5 Lateral Movement
- [ ] Internal reconnaissance
- [ ] Credential harvesting
- [ ] Pass-the-hash/ticket
- [ ] Pivoting to other systems

### 6.6 Cleanup
- [ ] Remove backdoors
- [ ] Remove tools
- [ ] Clear logs (document only, do not actually clear)
- [ ] Restore system state

## 7. Reporting

### 7.1 Executive Summary
- [ ] High-level overview
- [ ] Business impact
- [ ] Risk rating
- [ ] Strategic recommendations

### 7.2 Technical Report
- [ ] Methodology
- [ ] Findings with CVSS scores
- [ ] Proof-of-concept steps
- [ ] Evidence (screenshots, logs)
- [ ] Detailed remediation guidance

### 7.3 Deliverables
- [ ] Executive summary (PDF)
- [ ] Technical report (PDF + HTML)
- [ ] Remediation guide
- [ ] Re-test report (if applicable)

---

## PTES Testing Levels

**Level 1 - Compliance Assessment:**
- Vulnerability scanning
- Configuration review
- Policy compliance

**Level 2 - Traditional Pentesting:**
- Active exploitation
- Post-exploitation activities
- Simulated attacker approach

**Level 3 - Red Team Operations:**
- Adversary simulation
- Advanced persistent threat (APT) scenarios
- Physical security testing
- Social engineering
