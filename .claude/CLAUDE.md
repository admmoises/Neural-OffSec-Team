# PENTEST-WORK

**Workspace profissional para pentesting autorizado com carta de autorização.**

## Context

- 🎯 Foco: Web Applications + Infrastructure
- 🔧 MCP Security Toolkit: 25+ ferramentas
- 🕐 Timezone: America/Sao_Paulo (BRT/BRST)

## MCP Tools Quick Reference

**Recon:** dns_lookup, nmap_scan, sublist3r_enum, theharvester_osint
**Web:** sqlmap_test, nikto_scan, gobuster_scan, wpscan, http_header_analyzer
**Exploit:** metasploit_search, john_crack_hash, hydra_bruteforce
**Crypto:** hash_analyzer, jwt_decoder, sslyze_scan
**Utils:** check_installed_tools, encode_decode, secret_detector

## Workflow Phases (PTES)

1. Pre-Engagement → Authorization + Scope
2. Reconnaissance → Passive OSINT + Active Scanning
3. Vulnerability Assessment → Web + Network Testing
4. Exploitation → PoC Development + Evidence Collection
5. Post-Exploitation → Privilege Escalation + Lateral Movement (se autorizado)
6. Reporting → Auto-generation (PDF + HTML)

## Naming Conventions

**Engagements:** `YYYY-MM-DD-ClientName-type-scope`
Exemplo: `2025-11-09-ACME-web-portal`

**Screenshots:** `YYYYMMDD-HHMMSS-BRT-finding-description.png`
Exemplo: `20251109-143022-BRT-sqli-login-bypass.png`

**Evidências:** `YYYYMMDD-HHMMSS-BRT-evidence-type.ext`
Exemplo: `20251109-150145-BRT-packet-capture.pcap`

**Daily Notes:** `YYYY-MM-DD-notes.md`
Exemplo: `2025-11-09-notes.md`

**Findings:** `FINDING-XXX-short-description.md` (XXX = número sequencial)
Exemplo: `FINDING-001-sql-injection-login.md`

## 🧹 Workspace Hygiene Rules (CRÍTICO)

### Limites Máximos por Engajamento

**Temporários (DELETE após uso):**
- ❌ Scripts de teste: MAX 3 por vez → DELETE imediatamente após uso
- ❌ Logs de ferramentas: MAX 5 dias → DELETE após análise
- ❌ Temp files (.tmp, .bak): DELETE imediatamente
- ❌ Outputs brutos de scanners: Parsear → DELETE raw file

**Permanentes (KEEP):**
- ✅ Screenshots de findings: KEEP todos
- ✅ PCAPs de exploits bem-sucedidos: KEEP todos
- ✅ PoC scripts funcionais: KEEP em `/03-exploitation/successful-exploits/`
- ✅ Daily notes: KEEP todos
- ✅ Finding documents: KEEP todos
- ✅ Final reports: KEEP todos

### Regras de Limpeza Automática

**Claude DEVE automaticamente:**
- DELETE scripts de teste após execução (a menos que seja PoC funcional)
- DELETE outputs brutos de scanners após parsing
- DELETE arquivos .tmp, .log, .bak ao final de cada dia
- MOVER engagamentos concluídos para `@archive/` após 30 dias
- ALERTAR quando `/evidence/screenshots/` > 500 arquivos
- ALERTAR quando workspace total > 5GB

**Estrutura de Teste:**
```
/05-notes/scratchpad/        # Max 10 arquivos .md
└── test-scripts/            # Max 3 scripts, DELETE após uso
```

### Chain of Custody (Evidências Legais)

**Metadados Obrigatórios em Evidências:**
```markdown
---
timestamp: YYYY-MM-DD HH:MM:SS BRT
engagement: clients/CLIENT/YYYY-MM-DD-type-scope
finding: FINDING-XXX
tool: nmap/burp/manual
operator: [seu nome]
hash_sha256: [hash do arquivo]
---
```

**Chain Tracking:** Manter log em `/04-evidence/chain-of-custody.md`

## Reporting Standards

**Severidade:** 🔴 Critical (9.0-10.0) | 🟠 High (7.0-8.9) | 🟡 Medium (4.0-6.9) | 🟢 Low (0.1-3.9)
**Scoring:** CVSS 3.1 obrigatório + justificativa
**Finding:** PoC funcional + Screenshots + Remediação específica + Reprodução passo-a-passo

## Automation Scripts

**New Engagement:**
```bash
python tools/engagement-setup.py \
  --client "ACME-Corp" \
  --type "web-pentest" \
  --scope "*.acme.com" \
  --start-date "2025-11-09"
```

**Generate Report:**
```bash
python tools/report-generator/generate_report.py \
  --engagement clients/ACME-Corp/2025-11-09-web-portal \
  --output both --format professional
```

**Cleanup Workspace:**
```bash
python tools/cleanup-workspace.py \
  --engagement clients/ACME-Corp/2025-11-09-web-portal \
  --dry-run  # Remove --dry-run para executar
```

## Claude Code Behavior

**Durante Pentesting, Claude DEVE:**
- ✅ Criar timestamps em BRT em TODOS os arquivos
- ✅ DELETE scripts de teste após uso
- ✅ Documentar findings imediatamente quando descobertos
- ✅ Parsear outputs de ferramentas e DELETE raw files
- ✅ Manter chain of custody para evidências
- ✅ ALERTAR antes de testes invasivos/destrutivos
- ✅ Sugerir vetores de ataque não testados

**Claude NÃO DEVE:**
- ❌ Deixar scripts de teste acumulando
- ❌ Criar documentação desnecessária
- ❌ Manter logs brutos após parsing
- ❌ Misturar findings de engagements diferentes
- ❌ Executar testes fora do escopo sem confirmar
