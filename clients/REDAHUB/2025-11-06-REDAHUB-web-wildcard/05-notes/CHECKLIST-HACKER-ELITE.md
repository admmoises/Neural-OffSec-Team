# 🔥 REDAHUB PENTEST - CHECKLIST HACKER ELITE

---
**Document Timestamp:** 12-11-2025 19:20 BRT
**Last Updated:** 12-11-2025 19:20 BRT
**Engagement:** 2025-11-06-REDAHUB-web-wildcard
**Mode:** RED TEAM ELITE - FULL SPECTRUM ATTACK
**Estimated Time:** 6 hours (Phases 1+2+3)
---

## 📊 OVERVIEW

**Target Scope:**
- `redahub.cloud:3000` (Easypanel)
- `bkd.redahub.cloud` (Django REST API)
- `www.redahub.cloud` (Frontend React)
- `s3.redahub.cloud` (MinIO S3)

**Current Progress:** Session 3, 90% → Moving to 100% with gap closure

---

## 🎯 FASE 1: RECON FOCADO EM GAPS CRÍTICOS (2-3h)

### 1.1 MinIO S3 Exploitation 🔴 PRIORIDADE #1

**Timestamp Início:** ___________
**Timestamp Fim:** ___________

- [ ] Testar acesso anonymous ao bucket root (`http://s3.redahub.cloud/`)
- [ ] Enumerar buckets comuns:
  - [ ] `/uploads`
  - [ ] `/backups`
  - [ ] `/static`
  - [ ] `/media`
  - [ ] `/files`
  - [ ] `/documents`
  - [ ] `/images`
  - [ ] `/videos`
  - [ ] `/assets`
  - [ ] `/public`
- [ ] Testar directory listing
- [ ] Testar AWS CLI anonymous access
- [ ] Verificar CORS misconfiguration
- [ ] Tentar download de objetos conhecidos (test.txt, index.html)
- [ ] Enumerar via DNS (bucket.s3.redahub.cloud)
- [ ] Testar authenticated access (se credenciais obtidas)

**Findings Esperados:** Data leak, directory listing, anonymous upload

**Resultado:** ___________

---

### 1.2 Content Discovery Extensivo 🔴 PRIORIDADE #2

**Timestamp Início:** ___________
**Timestamp Fim:** ___________

#### Target: bkd.redahub.cloud
- [ ] Gobuster com raft-medium-directories.txt
- [ ] Gobuster com raft-medium-files.txt
- [ ] API-specific wordlist (api-endpoints.txt)
- [ ] Backup files (Common-DB-Backups.txt)
- [ ] Extensions: `.bak`, `.old`, `.backup`, `.swp`, `.env`, `.json`, `.yml`, `.yaml`
- [ ] Endpoints críticos:
  - [ ] `/api/docs`
  - [ ] `/api/swagger.json`
  - [ ] `/api/openapi.json`
  - [ ] `/api/graphql`
  - [ ] `/api/v1/`
  - [ ] `/api/v2/`
  - [ ] `/admin/`
  - [ ] `/debug/`
  - [ ] `/_debug/`
  - [ ] `/health`
  - [ ] `/metrics`

#### Target: www.redahub.cloud
- [ ] Gobuster com raft-medium-directories.txt
- [ ] JS source maps (`.map` files)
- [ ] Config files (`config.js`, `env.js`)
- [ ] Debug endpoints

#### Target: redahub.cloud:3000 (Easypanel)
- [ ] Gobuster (já sabemos que é SPA, mas vale tentar API routes)
- [ ] Backup files do Easypanel

#### Target: s3.redahub.cloud
- [ ] Content discovery via HTTP (além de bucket enum)

**Findings Esperados:** `.env` com credentials, API docs, backup files, debug endpoints

**Resultado:** ___________

---

### 1.3 Password Reset Flow Testing 🔴 PRIORIDADE #3

**Timestamp Início:** ___________
**Timestamp Fim:** ___________

#### Django Backend (bkd.redahub.cloud)
- [ ] Descobrir endpoint de password reset:
  - [ ] `/api/auth/forgot-password`
  - [ ] `/api/auth/password-reset`
  - [ ] `/api/auth/reset-password`
  - [ ] `/api/password-reset/`
  - [ ] `/v1/auth/reset`
  - [ ] `/v1/auth/forgot`
- [ ] Testar rate limiting no reset (vs. login)
- [ ] User enumeration via reset response
- [ ] Token validation:
  - [ ] Token expiration
  - [ ] Token reuse
  - [ ] Token bruteforce
- [ ] Host header injection (password reset poisoning)
- [ ] Parameter pollution
- [ ] Email flooding (DoS)

#### Easypanel (redahub.cloud:3000)
- [ ] Descobrir tRPC procedure de reset:
  - [ ] `auth.forgotPassword`
  - [ ] `auth.resetPassword`
  - [ ] `auth.requestReset`
- [ ] Mesmos testes acima

**Findings Esperados:** User enumeration sem rate limit, password reset poisoning, account takeover

**Resultado:** ___________

---

### 1.4 Subdomain Brute Force 🟠 PRIORIDADE #4

**Timestamp Início:** ___________
**Timestamp Fim:** ___________

- [ ] DNS brute force com subdomains-top1million-110000.txt
- [ ] Vhost enumeration no IP 82.29.59.28
- [ ] Certificate Transparency Logs (crt.sh)
- [ ] Subdomains comuns:
  - [ ] `staging.redahub.cloud`
  - [ ] `dev.redahub.cloud`
  - [ ] `test.redahub.cloud`
  - [ ] `api.redahub.cloud`
  - [ ] `admin.redahub.cloud`
  - [ ] `internal.redahub.cloud`
  - [ ] `portal.redahub.cloud`
  - [ ] `dashboard.redahub.cloud`
  - [ ] `app.redahub.cloud`
  - [ ] `beta.redahub.cloud`
  - [ ] `dev.bkd.redahub.cloud`
  - [ ] `staging.bkd.redahub.cloud`
  - [ ] `api.bkd.redahub.cloud`
- [ ] Port scanning em novos subdomains descobertos

**Findings Esperados:** Staging/dev environments, internal services

**Resultado:** ___________

---

### 1.5 API Documentation Discovery 🟡 PRIORIDADE #5

**Timestamp Início:** ___________
**Timestamp Fim:** ___________

- [ ] OpenAPI/Swagger:
  - [ ] `/api/docs`
  - [ ] `/api/swagger`
  - [ ] `/api/swagger.json`
  - [ ] `/api/swagger.yaml`
  - [ ] `/api/openapi.json`
  - [ ] `/api/redoc`
  - [ ] `/docs`
  - [ ] `/swagger`
- [ ] GraphQL:
  - [ ] `/api/graphql`
  - [ ] `/graphql`
  - [ ] GraphQL introspection query
- [ ] Django REST Framework:
  - [ ] `/api/` (browsable API)
  - [ ] `/api/schema/`
  - [ ] `/api/v1/`
- [ ] Postman collections via Google dorking
- [ ] GitHub repos (search for API docs)

**Findings Esperados:** API documentation exposta, schema leaks

**Resultado:** ___________

---

## 🎯 FASE 2: EXPLOITATION DOS GAPS (1-2h)

**Nota:** Executar apenas se Fase 1 descobrir vulnerabilidades

### 2.1 Exploitar Vetores Descobertos

**Timestamp Início:** ___________
**Timestamp Fim:** ___________

- [ ] **Se MinIO vulnerável:**
  - [ ] Download de arquivos sensíveis
  - [ ] Enumerar todos os objetos
  - [ ] Procurar por credenciais, keys, tokens
  - [ ] Screenshot de dados sensíveis
  - [ ] Calcular hash SHA256 de evidências

- [ ] **Se `.env` descoberto:**
  - [ ] Download do arquivo
  - [ ] Extrair credenciais (DB, API keys, JWT secrets)
  - [ ] Testar credenciais no Easypanel
  - [ ] Testar credenciais no Django Admin
  - [ ] Documentar como FINDING CRITICAL

- [ ] **Se password reset vulnerável:**
  - [ ] Executar proof-of-concept de account takeover
  - [ ] Documentar passo-a-passo de reprodução
  - [ ] Screenshot de evidências

- [ ] **Se novo subdomain descoberto:**
  - [ ] Full port scan
  - [ ] Tech stack identification
  - [ ] Content discovery
  - [ ] Vulnerability assessment

**Resultado:** ___________

---

## 🎯 FASE 3: VETORES SECUNDÁRIOS (2-3h)

**Nota:** Executar se tempo permitir e Fase 1+2 concluídas

### 3.1 XSS Testing Completo

**Timestamp Início:** ___________
**Timestamp Fim:** ___________

#### Reflected XSS
- [ ] Testar todos os inputs:
  - [ ] Login form (email, password)
  - [ ] Registration form (todos os campos)
  - [ ] Search functionality (se houver)
  - [ ] URL parameters
  - [ ] Headers (User-Agent, Referer, etc)

**Payloads:**
```html
<script>alert(1)</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>
'-alert(1)-'
"><script>alert(1)</script>
javascript:alert(1)
```

#### Stored XSS
- [ ] Registration form → armazenado no profile
- [ ] User profile fields
- [ ] Comments/feedback (se houver)
- [ ] File uploads (filename XSS)

#### DOM-based XSS
- [ ] Analisar bundle React para sinks perigosos
- [ ] Testar manipulação de URL hash/fragment
- [ ] Testar postMessage vulnerabilities

**Findings Esperados:** Reflected/Stored XSS em forms

**Resultado:** ___________

---

### 3.2 CSRF Testing

**Timestamp Início:** ___________
**Timestamp Fim:** ___________

- [ ] Django Admin:
  - [ ] Verificar CSRF token validation
  - [ ] Testar bypass via referer header removal
  - [ ] Testar bypass via origin header manipulation
  - [ ] PoC de CSRF (criar usuário admin)

- [ ] Registration form:
  - [ ] Verificar CSRF protection
  - [ ] PoC de mass account creation

- [ ] Password change:
  - [ ] PoC de CSRF (trocar senha de vítima)

**Findings Esperados:** CSRF em ações sensíveis

**Resultado:** ___________

---

### 3.3 Django REST API Fuzzing

**Timestamp Início:** ___________
**Timestamp Fim:** ___________

- [ ] Enumerar todos os endpoints:
  - [ ] `/api/users/`
  - [ ] `/api/projects/`
  - [ ] `/api/services/`
  - [ ] `/api/deployments/`
  - [ ] `/api/settings/`
  - [ ] `/api/logs/`

- [ ] HTTP method fuzzing (cada endpoint):
  - [ ] GET
  - [ ] POST
  - [ ] PUT
  - [ ] DELETE
  - [ ] PATCH
  - [ ] OPTIONS
  - [ ] HEAD

- [ ] Parameter pollution:
  - [ ] Duplicate params (`?id=1&id=2`)
  - [ ] Array notation (`?id[]=1&id[]=2`)
  - [ ] Nested objects

- [ ] Mass assignment testing:
  - [ ] Adicionar campo `is_admin=true` em POST/PUT
  - [ ] Adicionar campo `role=admin`

- [ ] Rate limiting per-endpoint

**Findings Esperados:** Endpoints não autenticados, mass assignment, IDOR

**Resultado:** ___________

---

### 3.4 IDOR Testing

**Timestamp Início:** ___________
**Timestamp Fim:** ___________

**Pré-requisito:** Obter IDs válidos via endpoints descobertos

- [ ] User ID manipulation:
  - [ ] `/api/users/1` → `/api/users/2`
  - [ ] Verificar access control

- [ ] Project/Service ID manipulation:
  - [ ] Acessar recursos de outros usuários
  - [ ] Modificar recursos alheios (PUT/DELETE)

- [ ] Predictable IDs:
  - [ ] IDs sequenciais
  - [ ] UUIDs predictable

**Findings Esperados:** IDOR horizontal/vertical

**Resultado:** ___________

---

## 📋 SUMMARY CHECKLIST

### FASE 1 - RECON ✅
- [ ] MinIO S3 testado (1.1)
- [ ] Content discovery extensivo (1.2)
- [ ] Password reset explorado (1.3)
- [ ] Subdomain brute force (1.4)
- [ ] API docs descoberta (1.5)

### FASE 2 - EXPLOITATION ✅
- [ ] Vetores descobertos explorados (2.1-2.4)

### FASE 3 - VETORES SECUNDÁRIOS ✅
- [ ] XSS testing (3.1)
- [ ] CSRF testing (3.2)
- [ ] API fuzzing (3.3)
- [ ] IDOR testing (3.4)

### DOCUMENTATION ✅
- [ ] Findings atualizados com timestamps
- [ ] Screenshots capturados
- [ ] Evidências hashadas (SHA256)
- [ ] Chain of custody atualizada
- [ ] Relatório final gerado

---

## 🎯 SUCCESS CRITERIA

**Minimum (60%):**
- Fase 1 completa (5/5 tasks)
- Pelo menos 1 finding novo descoberto

**Target (80%):**
- Fase 1 completa
- Fase 2 executada (se aplicável)
- 3+ findings novos

**Elite (100%):**
- Todas as 3 fases completas
- 5+ findings novos
- 1+ CRITICAL finding descoberto
- Documentação impecável

---

**Auditor:** Neural-OffSec-Team
**Reviewed:** N/A
**Status:** 🔄 IN PROGRESS
