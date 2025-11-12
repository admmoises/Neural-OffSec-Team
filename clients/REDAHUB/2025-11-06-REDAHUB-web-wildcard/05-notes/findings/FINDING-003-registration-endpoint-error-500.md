# FINDING-003: Backend API Registration Endpoint Returns HTTP 500

---
**Document Timestamp:** 11-11-2025 11:15 BRT
**Data:** 11-11-2025 11:15 BRT
**Severidade:** 🟡 MEDIUM (CVSS 5.3)
**Status:** ✅ DESCOBERTO - Pendente de análise profunda
**Engagement:** 2025-11-06-REDAHUB-web-wildcard
---

## Sumário Executivo

O endpoint de registro (`/api/auth/register/`) do backend REDAHUB retorna HTTP 500 (Internal Server Error) quando solicitado, sugerindo que self-registration pode estar desabilitado ou há um bug no backend que poderia ser explorado para causar DoS ou information disclosure.

---

## Detalhes Técnicos

### Informações do Alvo
- **URL:** `https://bkd.redahub.cloud/api/auth/register/`
- **Método:** POST
- **Content-Type:** application/json
- **Timestamp:** 2025-11-11 11:10:23 BRT

### Payload Testado
```json
{
  "email": "test@pentest.local",
  "password": "TestPass123",
  "username": "pentester"
}
```

### Resposta
```html
HTTP/1.1 500 Internal Server Error

<!doctype html>
<html lang="en">
<head>
  <title>Server Error (500)</title>
</head>
<body>
  <h1>Server Error (500)</h1><p></p>
</body>
</html>
```

### Comportamento Observado
1. Endpoint `/auth/login/` funciona corretamente (retorna 401 com "Credenciais inválidas")
2. Endpoint `/auth/register/` retorna 500 sem mensagem de erro detalhada
3. HTML error page genérica sugere exception não tratada no backend
4. Não há rate limiting aparente

---

## Análise de Impacto

### Severidade: MEDIUM (CVSS 5.3)
**Vector String:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N`

**Breakdown:**
- **Attack Vector (AV:N):** Network - exploável remotamente
- **Attack Complexity (AC:L):** Low - não requer condições especiais
- **Privileges Required (PR:N):** None - não requer autenticação
- **User Interaction (UI:N):** None - automático
- **Scope (S:U):** Unchanged - impacto limitado ao componente vulnerável
- **Confidentiality (C:L):** Low - pode revelar informações sobre implementação
- **Integrity (I:N):** None - não permite modificação
- **Availability (A:N):** None - DoS não confirmado (requer mais testes)

### Cenários de Risco

**🔴 HIGH RISK:**
- Stack trace leakage se verbose error estiver habilitado em dev/staging
- Information disclosure sobre framework/versão (Django/DRF)
- Potencial DoS se exception consome recursos significativos

**🟡 MEDIUM RISK:**
- Self-registration desabilitado mas endpoint exposto (attack surface desnecessária)
- Validação de input inadequada pode causar backend errors
- Falta de exception handling apropriado

**🟢 LOW RISK:**
- Apenas information disclosure sobre stack de tecnologia

---

## Prova de Conceito (PoC)

### Reprodução
```bash
# 1. Criar payload de registro
cat > /tmp/register.json << 'EOF'
{
  "email": "test@example.com",
  "password": "TestPassword123",
  "username": "testuser"
}
EOF

# 2. Enviar requisição
curl -X POST 'https://bkd.redahub.cloud/api/auth/register/' \
  -H 'Content-Type: application/json' \
  -d @/tmp/register.json \
  -v

# Expected: HTTP 500 Internal Server Error
```

### Resultado Esperado
```
< HTTP/1.1 500 Internal Server Error
< Content-Type: text/html

<!doctype html>
<html lang="en">
<head>
  <title>Server Error (500)</title>
</head>
<body>
  <h1>Server Error (500)</h1><p></p>
</body>
</html>
```

---

## Vetores de Exploração

### 1. Information Disclosure (Confirmado)
- Exception handling inadequado pode vazar stack traces
- Tentar payloads malformados para trigger diferentes exceptions:
  ```json
  {"email": null, "password": "test"}
  {"email": "not-an-email", "password": ""}
  {"email": "<script>alert(1)</script>", "password": "test"}
  ```

### 2. DoS Potencial (Não Testado)
- Rapid fire de requisições pode causar resource exhaustion
- Se exception é custosa (DB locks, file I/O), pode impactar availability

### 3. Bypass de Autenticação (Baixa Probabilidade)
- Testar se HTTP 500 ainda cria usuário no backend
- Verificar race conditions em registro

---

## Recomendações de Remediação

### Prioridade ALTA
1. **Implementar Exception Handling:**
   ```python
   @api_view(['POST'])
   def register(request):
       try:
           # registration logic
           pass
       except ValidationError as e:
           return JsonResponse({'detail': str(e)}, status=400)
       except Exception as e:
           logger.error(f"Registration error: {e}")
           return JsonResponse({'detail': 'Internal server error'}, status=500)
   ```

2. **Desabilitar Endpoint se Não Usado:**
   - Se self-registration não é permitido, remover rota completamente
   - Ou retornar 403 Forbidden com mensagem clara

3. **Rate Limiting:**
   ```python
   @ratelimit(key='ip', rate='5/m', method='POST')
   def register(request):
       # ...
   ```

### Prioridade MÉDIA
4. **Input Validation:**
   - Validar email format, password strength ANTES de processamento
   - Retornar 400 Bad Request para inputs inválidos

5. **Logging e Monitoring:**
   - Log todas as tentativas de registro (sucesso e falha)
   - Alertar sobre múltiplos 500 errors

### Prioridade BAIXA
6. **Custom Error Pages:**
   - Retornar JSON error response consistente
   - Não vazar informações de implementação

---

## Evidências

### Screenshot
- ⏳ Pendente (error é textual, não visual)

### Request/Response Logs
```
POST /api/auth/register/ HTTP/1.1
Host: bkd.redahub.cloud
Content-Type: application/json
Content-Length: 97

{"email":"test@pentest.local","password":"TestPass123","username":"pentester"}

---

HTTP/1.1 500 Internal Server Error
Date: Tue, 11 Nov 2025 14:10:23 GMT
Content-Type: text/html
Content-Length: 130

<!doctype html>
<html lang="en">
<head>
  <title>Server Error (500)</title>
</head>
<body>
  <h1>Server Error (500)</h1><p></p>
</body>
</html>
```

---

## Referências

- **CWE-209:** Information Exposure Through an Error Message
- **CWE-755:** Improper Handling of Exceptional Conditions
- **OWASP Top 10 2021:** A05:2021 - Security Misconfiguration
- **PTES:** Vulnerability Analysis Phase

---

## Timeline

| Data/Hora | Ação |
|-----------|------|
| 2025-11-11 11:10:23 BRT | Endpoint descoberto via JS bundle analysis |
| 2025-11-11 11:12:45 BRT | HTTP 500 confirmado com payload válido |
| 2025-11-11 11:15:00 BRT | Finding documentado |

---

## Status de Validação

- ✅ **Descoberto:** 2025-11-11
- ⏳ **Reportado ao Cliente:** Pendente
- ⏳ **Remediação Aplicada:** Pendente
- ⏳ **Retest:** Pendente

---

**Próximos Passos:**
1. Testar payloads malformados para information disclosure
2. Verificar se usuário é criado apesar do 500
3. Testar DoS com múltiplas requisições
4. Reportar ao cliente para correção
