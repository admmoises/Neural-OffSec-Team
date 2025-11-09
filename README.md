# PENTEST-WORK

**Workspace profissional para pentesting autorizado.**

## 📋 Visão Geral

Este workspace foi projetado para pentests profissionais em clientes que contrataram nossos serviços de segurança ofensiva. Estrutura organizada por cliente, templates profissionais e automação completa.

### Características Principais

✅ **Estrutura Organizada**: Por cliente → engajements isolados
✅ **Templates Profissionais**: Reports (MD→PDF+HTML), RoE, Scope
✅ **Automação Completa**: Setup, cleanup, report generation
✅ **MCP Security Toolkit**: 25+ ferramentas integradas
✅ **Timestamps BRT**: Todos arquivos em horário de Brasília
✅ **Workspace Hygiene**: Regras automáticas de limpeza
✅ **Chain of Custody**: Tracking legal de evidências
✅ **Knowledge Base**: Checklists PTES, OWASP, payloads

## 🚀 Quick Start

### 1. Criar Novo Engagement

```bash
python tools/engagement-setup.py \
  --client "ACME-Corp" \
  --type "web-pentest" \
  --scope "portal" \
  --start-date "2025-11-09"
```

**Output:**
```
clients/ACME-Corp/2025-11-09-ACME-Corp-web-pentest-portal/
├── 00-engagement/        # Authorization, scope, RoE
├── 01-reconnaissance/    # OSINT, scanning
├── 02-vulnerability-assessment/  # Testing, findings
├── 03-exploitation/      # PoCs, exploits
├── 04-evidence/          # Screenshots, PCAPs
├── 05-notes/             # Daily notes, findings
└── 06-reports/           # Reports (draft/final)
```

### 2. Executar Pentest com Claude Code + MCP

```bash
cd clients/ACME-Corp/2025-11-09-ACME-Corp-web-pentest-portal
claude
```

**Comandos exemplo:**
```
"Execute reconnaissance completo em acme.com"
→ dns_lookup + sublist3r_enum + nmap_scan + theharvester_osint

"Teste web vulnerabilities em app.acme.com"
→ nikto_scan + gobuster_scan + sqlmap_test + http_header_analyzer

"Documente finding de SQL injection encontrado"
→ Cria FINDING-001-sqli-login.md com timestamp BRT
```

### 3. Gerar Relatórios

```bash
# TODO: Report generator em desenvolvimento
# Por enquanto, use templates em templates/reports/markdown/
```

### 4. Limpar Workspace

```bash
# Dry-run (mostra o que seria deletado)
python tools/cleanup-workspace.py \
  --engagement clients/ACME-Corp/2025-11-09-ACME-Corp-web-pentest-portal \
  --dry-run

# Executar limpeza
python tools/cleanup-workspace.py \
  --engagement clients/ACME-Corp/2025-11-09-ACME-Corp-web-pentest-portal
```

## 📁 Estrutura do Workspace

```
PENTEST-WORK/
├── .claude/
│   └── CLAUDE.md                   # Contexto + regras de hygiene
├── clients/                        # Por cliente
│   └── [CLIENT-NAME]/
│       └── YYYY-MM-DD-type-scope/  # Engagements
├── templates/
│   ├── reports/
│   │   ├── markdown/               # Templates MD
│   │   ├── pandoc/                 # LaTeX/CSS para PDF
│   │   └── html/                   # Dashboard interativo
│   └── engagement/
│       ├── scope-template.md
│       ├── roe-template.md
│       └── checklists/             # OWASP, PTES, Web
├── tools/
│   ├── engagement-setup.py         # Setup automático
│   ├── cleanup-workspace.py        # Limpeza automática
│   └── report-generator/           # (em desenvolvimento)
├── knowledge-base/
│   ├── checklists/
│   │   ├── methodologies/          # PTES, OWASP, OSSTMM
│   │   ├── web/                    # Web pentesting
│   │   ├── network/                # Network pentesting
│   │   └── infrastructure/         # Infrastructure
│   ├── payloads/
│   │   ├── xss/                    # XSS payloads
│   │   ├── sqli/                   # SQL injection
│   │   ├── xxe/                    # XXE
│   │   ├── ssrf/                   # SSRF
│   │   └── command-injection/      # Command injection
│   ├── exploits/
│   │   ├── privilege-escalation/
│   │   ├── web-exploits/
│   │   └── network-exploits/
│   └── references/
│       ├── cvss-guide.md
│       └── remediation-references.md
└── @archive/                       # Engagements finalizados (>30 dias)
```

## 🔧 MCP Security Toolkit (25+ Tools)

### Reconnaissance
- `dns_lookup` - DNS enumeration
- `nmap_scan` - Port/service scanning (quick|full|stealth)
- `sublist3r_enum` - Subdomain discovery
- `theharvester_osint` - OSINT gathering
- `ip_info` - IP intelligence

### Web Testing
- `sqlmap_test` - SQL injection detection
- `nikto_scan` - Web vulnerability scanner
- `gobuster_scan` - Directory/file fuzzing
- `wpscan` - WordPress security
- `http_header_analyzer` - Security headers

### Exploitation
- `metasploit_search` - Exploit database
- `john_crack_hash` - Password cracking
- `hydra_bruteforce` - Credential brute force
- `hash_analyzer` - Hash identification
- `jwt_decoder` - Token analysis

### SSL/TLS & Crypto
- `sslyze_scan` - SSL/TLS analysis
- `password_strength_checker` - Password policy validation

### Utilities
- `encode_decode` - Encoding/decoding
- `secret_detector` - Credentials/API keys detection
- `check_installed_tools` - Tool availability

## 📝 Naming Conventions

**Engagements:**
```
YYYY-MM-DD-ClientName-type-scope
Exemplo: 2025-11-09-ACME-web-portal
```

**Screenshots:**
```
YYYYMMDD-HHMMSS-BRT-finding-description.png
Exemplo: 20251109-143022-BRT-sqli-login-bypass.png
```

**Evidências:**
```
YYYYMMDD-HHMMSS-BRT-evidence-type.ext
Exemplo: 20251109-150145-BRT-packet-capture.pcap
```

**Daily Notes:**
```
YYYY-MM-DD-notes.md
Exemplo: 2025-11-09-notes.md
```

**Findings:**
```
FINDING-XXX-short-description.md
Exemplo: FINDING-001-sql-injection-login.md
```

## 🧹 Workspace Hygiene Rules

### Limites Máximos

**Temporários (DELETE após uso):**
- ❌ Scripts de teste: MAX 3 → DELETE após uso
- ❌ Logs de ferramentas: MAX 5 dias → DELETE após análise
- ❌ Temp files (.tmp, .bak): DELETE imediatamente
- ❌ Outputs brutos: Parsear → DELETE raw file

**Permanentes (KEEP):**
- ✅ Screenshots de findings
- ✅ PCAPs de exploits bem-sucedidos
- ✅ PoC scripts funcionais
- ✅ Daily notes
- ✅ Finding documents
- ✅ Final reports

### Claude Code Behavior

**Claude DEVE:**
- ✅ Criar timestamps em BRT em TODOS os arquivos
- ✅ DELETE scripts de teste após uso
- ✅ Documentar findings imediatamente
- ✅ Parsear outputs e DELETE raw files
- ✅ Manter chain of custody

**Claude NÃO DEVE:**
- ❌ Deixar scripts acumulando
- ❌ Criar documentação desnecessária
- ❌ Manter logs brutos após parsing
- ❌ Misturar findings de engagements diferentes

## 📊 Reporting Standards

### Severity Levels (CVSS 3.1)

- 🔴 **Critical (9.0-10.0)** - Exploitação trivial, impacto massivo
- 🟠 **High (7.0-8.9)** - Exploitação factível, impacto significativo
- 🟡 **Medium (4.0-6.9)** - Exploitação possível, impacto moderado
- 🟢 **Low (0.1-3.9)** - Exploitação difícil, impacto limitado
- ⚪ **Info (0.0)** - Sem impacto direto de segurança

### Finding Requirements

- Título claro e descritivo
- CVSS score calculado com justificativa
- Descrição técnica completa
- Proof-of-concept funcional
- Screenshots/evidências
- Remediação específica (não genérica)
- Referências (CWE, OWASP, CVE quando aplicável)

## 🔄 Workflow PTES (7 Fases)

1. **Pre-Engagement** → Authorization + Scope
2. **Reconnaissance** → Passive OSINT + Active Scanning
3. **Threat Modeling** → Attack surface analysis
4. **Vulnerability Assessment** → Web + Network testing
5. **Exploitation** → PoC development + Evidence collection
6. **Post-Exploitation** → Privilege escalation + Lateral movement (se autorizado)
7. **Reporting** → Auto-generation (PDF + HTML)

## 🛠️ Setup e Dependências

### Python Dependencies

```bash
# Criar ambiente virtual
uv venv
source .venv/bin/activate  # Mac/Linux

# Instalar dependências
uv pip install -r requirements.txt
```

### Scripts Disponíveis

1. **engagement-setup.py** - Cria estrutura de novo engagement
2. **cleanup-workspace.py** - Limpa workspace automaticamente
3. **report-generator/** - Gera relatórios (em desenvolvimento)

## 📚 Knowledge Base

### Checklists

- **PTES Standard** - Metodologia completa de pentest
- **OWASP Top 10 (2021)** - Web application testing
- **Web Pentest Checklist** - Checklist completo de web testing

### Payloads

- **XSS** - Basic, filter bypass, polyglot
- **SQLi** - MySQL, PostgreSQL, MSSQL, Oracle
- **XXE** - XML external entity payloads
- **SSRF** - Server-side request forgery
- **Command Injection** - Linux, Windows

### Exploits

- **Privilege Escalation** - Linux, Windows checklists
- **Web Exploits** - Common PoCs
- **Network Exploits** - Default credentials

## ⚖️ Legal e Ético

**IMPORTANTE:**
- ✅ Todos testes realizados COM carta de autorização
- ✅ Conformidade com leis de crimes cibernéticos
- ✅ Pentesting profissional e ético
- ❌ NUNCA testar sem autorização por escrito
- ❌ NUNCA violar escopo contratual

## 📞 Suporte

**MCP Security Toolkit:**
```bash
# Verificar ferramentas instaladas
check_installed_tools

# Ver documentação completa em:
/Users/th3_w6rst/Desktop/mcp-sec/
```

**Claude Code:**
```bash
# Documentação oficial
~/.claude/plugins/cache/superpowers-developing-for-claude-code/
```

---

**Workspace Version:** 1.0
**Created:** 2025-11-09
**Timezone:** America/Sao_Paulo (BRT/BRST)
**Classification:** CONFIDENTIAL
