# Rules of Engagement (RoE)

**Engagement:** {{ENGAGEMENT_NAME}}
**Cliente:** {{CLIENT_NAME}}
**Data:** {{ROE_DATE}}

## Testing Methodology

**Framework:** PTES (Penetration Testing Execution Standard)

**Phases:**
1. Pre-Engagement Interactions
2. Intelligence Gathering (Reconnaissance)
3. Threat Modeling
4. Vulnerability Analysis
5. Exploitation
6. Post-Exploitation
7. Reporting

## Authorized Testing Techniques

### Reconnaissance
- ✅ Passive OSINT (public sources, DNS, WHOIS)
- ✅ Active network scanning (Nmap, Masscan)
- ✅ Subdomain enumeration
- ✅ Service fingerprinting
- {{CUSTOM_RECON}}

### Vulnerability Assessment
- ✅ Automated vulnerability scanning
- ✅ Manual code review (if source provided)
- ✅ Web application testing (injection, XSS, CSRF, etc.)
- ✅ API security testing
- {{CUSTOM_VULN_ASSESSMENT}}

### Exploitation
- ✅ Proof-of-Concept (PoC) development
- ⚠️ Limited exploitation (staging environments only)
- ❌ No exploitation on production (unless explicitly authorized)
- {{CUSTOM_EXPLOITATION}}

### Post-Exploitation
- ⚠️ Privilege escalation (authorized scope only)
- ⚠️ Lateral movement (within authorized network segments)
- ❌ Data exfiltration prohibited
- ❌ Persistence mechanisms prohibited (must be removed immediately)

## Communication Protocols

### Regular Updates
- **Frequency:** {{UPDATE_FREQUENCY}} (ex: Daily status updates)
- **Method:** {{COMMUNICATION_METHOD}} (ex: Email, Slack, Teams)
- **Contact:** {{PRIMARY_CONTACT}}

### Critical Findings
**Severidade Critical/High encontrada:**
1. **STOP testing** imediatamente
2. Notificar {{CRITICAL_CONTACT}} via {{CRITICAL_METHOD}} (ex: telefone)
3. Documentar finding completo
4. Aguardar go/no-go para continuar

### Emergency Stop
**Trigger:** Sistema instável, downtime não planejado, suspeita de impacto adverso
**Action:**
1. STOP all testing immediately
2. Document current activity and system state
3. Notify {{EMERGENCY_CONTACT}} via {{EMERGENCY_METHOD}}

## Legal and Compliance

### Authorization
- Testing performed under signed authorization letter
- All activities within defined scope
- Compliance with applicable laws (Lei 12.737/2012 - Lei Carolina Dieckmann, etc.)

### Data Handling
- ✅ Findings confidential and encrypted
- ✅ Evidence stored securely
- ❌ No sharing of findings with third parties
- ✅ Data destruction after engagement (per agreement)

### Insurance
- Professional liability insurance: {{INSURANCE_INFO}}

## Incident Response

**Se detectado WAF/IDS/IPS:**
- Continue testing if not blocked
- Document detection mechanisms
- Report in final deliverable

**Se bloqueado:**
- Notify client
- Request whitelist if appropriate
- Document blocking behavior

## Tools and Techniques

**Authorized Tools:**
- Nmap, Masscan (network scanning)
- Burp Suite, OWASP ZAP (web testing)
- SQLMap, Nikto, Gobuster (specialized testing)
- Metasploit (exploitation framework)
- Custom scripts (with approval)

**Prohibited:**
- DoS/DDoS tools (unless explicitly authorized)
- Malware/ransomware
- Tools that modify data destructively

## Signatures

**Pentester:**
Assinatura: ____________________
Data: {{SIGNATURE_DATE}}

**Cliente (Authorized Representative):**
Assinatura: ____________________
Nome: {{CLIENT_REP_NAME}}
Data: {{CLIENT_SIGNATURE_DATE}}
