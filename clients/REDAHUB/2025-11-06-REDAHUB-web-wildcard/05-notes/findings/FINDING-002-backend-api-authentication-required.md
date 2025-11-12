# FINDING-002: Backend API Requer Autenticação (Design Seguro)

---
**Document Timestamp:** 11-11-2025 10:31 BRT
**Metadata Chain of Custody:**
```
timestamp: 11-11-2025 10:31 BRT
engagement: clients/REDAHUB/2025-11-06-REDAHUB-web-wildcard
finding: FINDING-002
tool: manual inspection + curl
operator: Neural Offsec Team
severity: 🟢 INFORMATIONAL (Good Practice)
cvss_score: N/A (Not a vulnerability - secure implementation)
status: CONFIRMED - POSITIVE FINDING
```
---

## Summary

A API backend localizada em `https://bkd.redahub.cloud/api` **requer autenticação adequadamente**, retornando mensagem de erro quando credenciais não são fornecidas. Esta é uma **implementação de segurança correta** que previne acesso não autorizado à API.

## Technical Details

### Discovery

Descoberto através da análise do bundle JavaScript do frontend React em `https://redahub.cloud/static/js/main.023e6df6.js`, onde o endpoint da API foi encontrado hardcoded no código.

**JS Bundle Extract:**
```
https://bkd.redahub.cloud/api
```

### API Testing

**Test Request:**
```bash
curl -sL https://bkd.redahub.cloud/api
```

**Response:**
```json
{"detail":"As credenciais de autenticação não foram fornecidas."}
```

**HTTP Headers:**
```
HTTP/2 301
content-type: text/html; charset=utf-8
cross-origin-opener-policy: same-origin
date: Tue, 11 Nov 2025 13:31:23 GMT
location: /api/
referrer-policy: same-origin
server: gunicorn
vary: origin
x-content-type-options: nosniff
```

### Technology Stack Identified

| Component | Value |
|-----------|-------|
| **Web Server** | gunicorn (Python WSGI HTTP Server) |
| **Framework** | Django REST Framework or Flask (likely Django based on error message format) |
| **Language** | Python |
| **Authentication** | Required (DRF authentication or similar) |
| **IP** | 82.29.59.28 (same as frontend) |
| **Subdomain** | bkd.redahub.cloud |

### Security Headers Present

✅ **Good Security Practices Implemented:**
- `x-content-type-options: nosniff` - Prevents MIME type sniffing
- `referrer-policy: same-origin` - Controls referrer information
- `cross-origin-opener-policy: same-origin` - Prevents cross-origin attacks

### Architecture Confirmed

```
┌─────────────────────────────────────┐
│      React SPA Frontend             │
│    https://redahub.cloud/           │
│    (nginx/1.29.3 + Golang)          │
└─────────────┬───────────────────────┘
              │ HTTPS API Calls
              ▼
┌─────────────────────────────────────┐
│      Python Backend API             │
│  https://bkd.redahub.cloud/api      │
│  (gunicorn + Django/Flask)          │
│  ✅ Authentication Required          │
└─────────────────────────────────────┘
```

## Assessment

### Positive Security Findings

1. ✅ **Authentication Enforced** - API não permite acesso anônimo
2. ✅ **Clear Error Messages** - Mensagem em português claro sobre autenticação
3. ✅ **Security Headers** - Headers básicos de segurança implementados
4. ✅ **HTTPS Only** - API acessível apenas via HTTPS
5. ✅ **Modern Stack** - Python/Django com Gunicorn é stack moderno e seguro

### Recommendations for Further Security

🟡 **MEDIUM PRIORITY** (Melhorias Incrementais):

1. **Rate Limiting**
   - Implementar rate limiting para prevenir brute force em endpoints de login
   - Recomendação: 5 tentativas por minuto por IP

2. **API Documentation**
   - Considerar exposição controlada de OpenAPI/Swagger docs
   - Requer autenticação para acesso à documentação

3. **CORS Policy Review**
   - Header `vary: origin` detectado - verificar política CORS
   - Garantir que apenas domínios autorizados podem fazer requests

4. **Additional Security Headers**
   - Add `Strict-Transport-Security` (HSTS)
   - Consider `Content-Security-Policy` if API retorna HTML
   - Add `X-Frame-Options: DENY`

5. **API Versioning**
   - Implementar versionamento de API (/api/v1/, /api/v2/)
   - Facilita manutenção e backwards compatibility

6. **Response Time Analysis**
   - Garantir que tempos de resposta não revelam informações
   - Username enumeration prevention

## Next Testing Steps

### Authentication Testing (Authorized)

⏳ **PENDING - Requires Explicit Authorization:**

1. **Valid Credentials Testing**
   - Test with provided credentials (if client supplies test accounts)
   - Verify authentication mechanisms (JWT, Session, OAuth2)

2. **Authorization Testing**
   - Test horizontal privilege escalation
   - Test vertical privilege escalation
   - Verify role-based access controls (RBAC)

3. **API Endpoint Enumeration**
   - Discover available endpoints (/api/users, /api/content, etc.)
   - Test each endpoint for proper authorization
   - Check for information disclosure

4. **Input Validation**
   - Test for SQL injection (if applicable)
   - Test for NoSQL injection
   - Test for XSS in API responses
   - Test for command injection

5. **Business Logic Testing**
   - Test workflow bypass
   - Test mass assignment vulnerabilities
   - Test for insecure direct object references (IDOR)

## References

- Django REST Framework Security: https://www.django-rest-framework.org/api-guide/authentication/
- Flask Security Considerations: https://flask.palletsprojects.com/en/2.3.x/security/
- OWASP API Security Top 10: https://owasp.org/www-project-api-security/
- Gunicorn Security: https://docs.gunicorn.org/en/stable/settings.html#security

## Timeline

- **2025-11-11 10:31:23 -03** - Backend API discovered in JS bundle analysis
- **2025-11-11 10:31:30 -03** - Authentication requirement confirmed
- **2025-11-11 10:32:00 -03** - Finding documented (FINDING-002)
- **[PENDING]** - Request test credentials from client for authorized testing
- **[PENDING]** - Comprehensive API security testing with valid authentication

---

**Status:** POSITIVE FINDING - Authentication properly implemented
**Impact:** None (this is good security practice)
**Client Action Required:** None (maintain current implementation)
**Pentest Next Steps:** Request test credentials for authorized API testing
