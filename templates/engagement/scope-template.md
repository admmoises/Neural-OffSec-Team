# Engagement Scope

**Cliente:** {{CLIENT_NAME}}
**Engagement:** {{ENGAGEMENT_NAME}}
**Data Início:** {{START_DATE}}
**Data Fim:** {{END_DATE}}
**Tipo:** {{TYPE}} (Web Application / Network Infrastructure / Full-Stack)

## In-Scope Targets

### Web Applications
- [ ] {{PRIMARY_TARGET}} (ex: https://app.cliente.com)
- [ ] {{SECONDARY_TARGET_1}}
- [ ] {{SECONDARY_TARGET_2}}

### Network Ranges
- [ ] {{IP_RANGE_1}} (ex: 192.168.1.0/24)
- [ ] {{IP_RANGE_2}}

### Domains/Subdomains
- [ ] *.{{DOMAIN}} (ex: *.cliente.com)
- [ ] Specific subdomains:
  - [ ] {{SUBDOMAIN_1}}
  - [ ] {{SUBDOMAIN_2}}

## Out-of-Scope

⛔ **EXPRESSLY PROHIBITED:**
- Third-party services (CDN, analytics, payment gateways)
- Production databases (apenas staging/dev autorizado)
- Email servers (a menos que explicitamente autorizado)
- {{OUT_OF_SCOPE_CUSTOM}}

## Testing Limitations

### Technical Constraints
- [ ] **DoS Testing:** ❌ Prohibited / ⚠️ Limited / ✅ Authorized
- [ ] **Social Engineering:** ❌ Prohibited / ⚠️ Limited / ✅ Authorized
- [ ] **Credential Brute-forcing:** ❌ Prohibited / ⚠️ Limited (max X attempts) / ✅ Authorized
- [ ] **Exploitation:** ❌ Prohibited / ⚠️ PoC only / ✅ Full exploitation authorized
- [ ] **Data Exfiltration:** ❌ Prohibited / ⚠️ Demo data only / ✅ Authorized

### Time Constraints
- **Testing Hours:** {{ALLOWED_HOURS}} (ex: 09:00-18:00 BRT, Mon-Fri)
- **Blackout Periods:** {{BLACKOUT_PERIODS}}

## Success Criteria

**Deliverables:**
- [ ] Comprehensive vulnerability assessment
- [ ] CVSS-scored findings with PoCs
- [ ] Executive summary report (PDF)
- [ ] Technical detailed report (PDF + HTML)
- [ ] Remediation guidance document

**Coverage Goals:**
- [ ] OWASP Top 10 (2021) - 100% coverage
- [ ] API Security Top 10 - 100% coverage
- [ ] Network infrastructure assessment
- [ ] Configuration review

## Authorization

**Carta de Autorização:** ✅ Recebida e arquivada em `00-engagement/authorization-letter.pdf`
**Contato de Emergência:** {{EMERGENCY_CONTACT}} ({{EMERGENCY_PHONE}})
**Comunicação de Achados Críticos:** {{CRITICAL_FINDINGS_CONTACT}}
