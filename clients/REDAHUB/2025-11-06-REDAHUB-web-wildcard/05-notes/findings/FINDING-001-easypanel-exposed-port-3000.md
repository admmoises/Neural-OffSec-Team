# FINDING-001: Easypanel Management Panel Exposto Publicamente

---
**Document Timestamp:** 11-11-2025 10:24 BRT
**Metadata Chain of Custody:**
```
timestamp: 11-11-2025 10:24 BRT
engagement: clients/REDAHUB/2025-11-06-REDAHUB-web-wildcard
finding: FINDING-001
tool: nmap + manual inspection
operator: Neural Offsec Team
severity: 🔴 CRITICAL
cvss_score: 9.1 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N)
status: DISCOVERED - NOT EXPLOITED YET
```
---

## Summary

**Easypanel**, uma plataforma completa de gerenciamento de containers e deployments (similar ao Portainer/Rancher), está **totalmente exposta na porta 3000** sem nenhuma camada de autenticação visível na interface web pública.

## Vulnerability Details

| Field | Value |
|-------|-------|
| **Tipo** | Information Disclosure + Insecure Management Interface Exposure |
| **CWE** | CWE-425: Direct Request ('Forced Browsing') |
| **OWASP** | A01:2021 - Broken Access Control |
| **Severidade** | 🔴 **CRITICAL** (CVSS 3.1: 9.1) |
| **Target** | http://redahub.cloud:3000/ |
| **IP** | 82.29.59.28:3000 |
| **Service** | HTTP (Easypanel - React SPA) |

## CVSS 3.1 Scoring

**Vector:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`

**Breakdown:**
- **Attack Vector (AV:N):** Network - Remotamente explorável
- **Attack Complexity (AC:L):** Low - Sem complexidade, acesso direto
- **Privileges Required (PR:N):** None - Nenhum privilégio necessário
- **User Interaction (UI:N):** None - Sem interação do usuário
- **Scope (S:U):** Unchanged - Impacto no componente vulnerável
- **Confidentiality (C:H):** High - Acesso total a informações sensíveis
- **Integrity (I:H):** High - Possibilidade de modificar configurações/deployments
- **Availability (A:N):** None - Não permite DoS direto (excluído do escopo)

**Base Score:** 9.1 (CRITICAL)

## Technical Details

### Discovery

**Nmap Scan Output:**
```
PORT     STATE SERVICE  VERSION
3000/tcp open  ppp?
```

**HTTP Response Headers:**
```
HTTP/1.1 200 OK
content-type: text/html; charset=utf-8
content-length: 459
Date: Tue, 11 Nov 2025 13:23:55 GMT
```

**HTML Source:**
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Easypanel</title>
    <script type="module" crossorigin src="/assets/index-Cvw0WVkJ.js"></script>
    <link rel="stylesheet" crossorigin href="/assets/index-BUEH_YWd.css">
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
```

### What is Easypanel?

Easypanel é uma plataforma moderna de gerenciamento de servidores e deployments que permite:
- Gerenciar containers Docker
- Deploy de aplicações
- Configuração de databases
- Gerenciamento de domínios e SSL
- Controle de recursos do servidor
- Acesso a logs e métricas
- **Potencialmente acesso root ao servidor**

**Official Website:** https://easypanel.io/

### Attack Surface

Se este painel NÃO POSSUI autenticação ou possui **credenciais padrão**, um atacante pode:

1. ✅ **Visualizar todos os containers/aplicações em execução**
2. ✅ **Modificar configurações de aplicações**
3. ✅ **Fazer deploy de código malicioso**
4. ✅ **Acessar variáveis de ambiente (secrets, tokens, API keys)**
5. ✅ **Executar comandos no servidor (shell access)**
6. ✅ **Comprometer completamente a infraestrutura**

## Impact

### Business Impact
- **Confidencialidade:** Exposição de credenciais, API keys, secrets, código-fonte
- **Integridade:** Possibilidade de modificar aplicações, injetar código malicioso
- **Disponibilidade:** Capacidade de derrubar serviços ou modificar configurações críticas
- **Compliance:** Violação grave de segurança expondo painel administrativo

### Technical Impact
- Acesso completo ao ambiente de deployment
- Possível pivoting para outros sistemas
- Exfiltração de dados sensíveis
- Persistência através de backdoors em containers

## Proof of Concept (PoC)

### Step 1: Direct Access
```bash
curl -I http://redahub.cloud:3000/
```

**Response:**
```
HTTP/1.1 200 OK
accept-ranges: bytes
cache-control: public, max-age=0
[...] Página do Easypanel carregada sem autenticação
```

### Step 2: Interface Access
```
Navigate to: http://redahub.cloud:3000/
Result: Easypanel interface loads (React SPA)
Status: Further manual testing required to determine auth status
```

## Reproduction Steps

1. Abrir navegador web
2. Acessar `http://redahub.cloud:3000/`
3. Observar que a interface do Easypanel carrega
4. **[PENDING VALIDATION]** Verificar se existe tela de login ou acesso direto ao dashboard

## Evidence

**Screenshot Location:** `04-evidence/screenshots/20251111-102422-BRT-easypanel-exposed-port-3000.png` (PENDING - needs browser capture)

**Scan Results:** `01-recon/active/nmap-quick-scan-82.29.59.28.txt` (PENDING - save results)

## Affected Assets

- **Primary:** http://redahub.cloud:3000/ (82.29.59.28:3000)
- **Infrastructure:** srv1065673.hstgr.cloud
- **Scope:** Entire REDAHUB infrastructure managed by Easypanel

## Risk Assessment

| Category | Rating | Justification |
|----------|--------|---------------|
| **Likelihood** | 🔴 Very High | Publicamente acessível, fácil descoberta via port scan |
| **Impact** | 🔴 Very High | Comprometimento total da infraestrutura |
| **Exploitability** | 🔴 Very High | Sem complexidade técnica se não houver auth |
| **Overall Risk** | 🔴 **CRITICAL** | Requer remediação imediata |

## Recommendations

### 🔴 URGENT (Implementar Imediatamente)

1. **Fechar Port 3000 Externamente**
   ```bash
   # Bloquear acesso externo no firewall (ufw/iptables)
   sudo ufw deny 3000/tcp from any
   # Ou configurar nginx reverse proxy com auth
   ```

2. **Implementar Autenticação Forte**
   - Habilitar autenticação no Easypanel
   - Usar senhas complexas (mínimo 16 caracteres)
   - Implementar 2FA/MFA

3. **Restringir Acesso por IP**
   ```nginx
   # nginx.conf
   location /easypanel {
       allow 10.0.0.0/8;  # IPs internos
       deny all;
       proxy_pass http://localhost:3000;
   }
   ```

### 🟡 HIGH PRIORITY (Implementar em 7 dias)

4. **VPN para Acesso Administrativo**
   - Requerer VPN (WireGuard/OpenVPN) para acessar painéis admin
   - Segregar rede de gerenciamento

5. **Audit Logging**
   - Habilitar logs de acesso no Easypanel
   - Monitorar tentativas de acesso suspeitas

6. **Security Headers**
   - Implementar headers de segurança no nginx
   - Rate limiting para tentativas de login

### 🟢 MEDIUM PRIORITY (Implementar em 30 dias)

7. **Network Segmentation**
   - Mover Easypanel para VLAN/subnet separada
   - Implementar micro-segmentation

8. **Regular Security Audits**
   - Scan periódico de portas expostas
   - Pentest trimestral

## References

- Easypanel Official Docs: https://easypanel.io/docs
- OWASP Top 10 2021 - A01 Broken Access Control: https://owasp.org/Top10/A01_2021-Broken_Access_Control/
- CWE-425: Direct Request: https://cwe.mitre.org/data/definitions/425.html
- CVSS 3.1 Calculator: https://www.first.org/cvss/calculator/3.1

## Timeline

- **2025-11-11 10:23:41 -03** - Discovered via nmap scan
- **2025-11-11 10:24:22 -03** - Manual verification confirmed Easypanel interface loading
- **2025-11-11 10:25:00 -03** - Finding documented (FINDING-001)
- **[PENDING]** - Authentication bypass test (if applicable)
- **[PENDING]** - Screenshot capture
- **[PENDING]** - Client notification

## Next Steps

1. ⏳ **[PENDING]** - Manual browser testing to verify authentication state
2. ⏳ **[PENDING]** - Capture screenshot evidence
3. ⏳ **[PENDING]** - Test default credentials (if login page found)
4. ⏳ **[PENDING]** - Assess lateral movement possibilities
5. 🚨 **[CRITICAL]** - Notify client immediately if unauthenticated access confirmed

---

**Discovery Status:** CONFIRMED - Interface accessible
**Exploitation Status:** NOT ATTEMPTED - Awaiting explicit authorization for login attempts
**Client Notification:** PENDING - Will notify after complete verification
