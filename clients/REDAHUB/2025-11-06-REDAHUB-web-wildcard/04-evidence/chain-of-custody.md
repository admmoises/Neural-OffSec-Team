# Registro de Cadeia de Custódia

---
**Timestamp do Documento:** 11-11-2025 14:35 BRT
**Engajamento:** 2025-11-06-REDAHUB-web-wildcard
**Operador:** Neural-OffSec-Team
**Cliente:** REDAHUB Sistema Editorial
**Timezone:** America/Sao_Paulo (BRT/BRST)
**Última Atualização:** 15-11-2025 17:18 BRT
---

## Propósito

Este documento mantém uma **cadeia de custódia legal** para todas as evidências coletadas durante o teste de penetração. Cada peça de evidência (screenshots, PCAPs, logs, exploits) deve ser registrada aqui com verificação criptográfica.

## Registro de Evidências

### Sessão 2025-11-15 - Consolidação de Evidências FASE 1

#### Evidências Técnicas Capturadas (HTML/TXT)

| Timestamp | Finding | Arquivo | Hash SHA256 | Tamanho | Descrição |
|-----------|---------|---------|-------------|---------|-----------|
| 15-11-2025 17:17:49 BRT | FINDING-001 | 01-FINDING-001-easypanel-15112025-171749-BRT.html | 715460a80746c66b5b69ccc2c3553409391700383a79e9e3ce56219ff340b95d | 497B | Página login Easypanel porta 3000 (HTTP 200) |
| 15-11-2025 17:18:00 BRT | FINDING-005 | 02-FINDING-005-django-admin-15112025-171800-BRT.html | a6b8305caa2e00f71bbbd26568c18026d58d5294a0443d08efa0749c7050cab7 | 4.2KB | Django Admin login form com CSRF |
| 15-11-2025 17:17:50 BRT | FINDING-008 | 03-FINDING-008-user-enum-invalid-15112025-171750-BRT.txt | facbeff0a49297cfbab16f7fc1e682bd189a19fd7ee90ca19004ffa60a9043dc | 2.6KB | User enumeration test (invalid email) - HTTP 404 |
| 15-11-2025 17:17:50 BRT | FINDING-008 | 04-FINDING-008-user-enum-valid-15112025-171750-BRT.txt | bc4e2aff9fe1500c09698569770e31b7131b05465a2cfd99fd23b7c55989942c | 2.5KB | User enumeration test (valid email) - HTTP 404 |
| 15-11-2025 17:17:51 BRT | FINDING-004 | 05-FINDING-004-403-bypass-15112025-171751-BRT.txt | a9215570f60459edbefe1bd09d86d60b03bf6e86fbc61c11b7310213ee657bc3 | 893B | 403 bypass attempts (.env, .git/config, etc) - Todos HTTP 404 |
| 15-11-2025 17:17:52 BRT | FINDING-003 | 06-FINDING-003-http500-15112025-171752-BRT.txt | 1458f76922c16226cf23a028b4f88e0b79df50b36ef8a7111e1416057984e937 | 2.5KB | HTTP 500 error test em /api/auth/register/ |
| 15-11-2025 17:18:08 BRT | Multi-Finding | 07-nmap-scan-15112025-171808-BRT.txt | dca2aaca22ead38e3b2fce187d25d695d1655e5f49895871f55068376b010979 | 5.8KB | Nmap service scan ports 3000,80,443,8080 |

**Hash Master File:** `EVIDENCE-HASHES-SHA256-15112025-171826-BRT.txt` (✅ Validado - 8/8 arquivos OK)

### Sessão 2025-11-11

#### Screenshots (CAPTURA PENDENTE - OBSOLETO)

| Timestamp | Finding | Arquivo | Hash SHA256 | Tamanho | Descrição |
|-----------|---------|---------|-------------|---------|-----------|
| *Obsoleto* | FINDING-001 | 20251111-HHMMSS-BRT-easypanel-login.png | *Substituído por HTML* | *-* | ✅ Substituído por 01-FINDING-001-easypanel-15112025-171749-BRT.html |
| *Obsoleto* | FINDING-003 | 20251111-HHMMSS-BRT-registration-500-error.png | *Substituído por TXT* | *-* | ✅ Substituído por 06-FINDING-003-http500-15112025-171752-BRT.txt |
| *Obsoleto* | FINDING-003 | 20251111-HHMMSS-BRT-registration-payload.png | *Substituído por TXT* | *-* | ✅ Substituído por 06-FINDING-003-http500-15112025-171752-BRT.txt |
| *Obsoleto* | FINDING-004 | 20251111-HHMMSS-BRT-gobuster-403-results.png | *Substituído por TXT* | *-* | ✅ Substituído por 05-FINDING-004-403-bypass-15112025-171751-BRT.txt |
| *Obsoleto* | FINDING-004 | 20251111-HHMMSS-BRT-env-file-403-test.png | *Substituído por TXT* | *-* | ✅ Substituído por 05-FINDING-004-403-bypass-15112025-171751-BRT.txt |
| *Obsoleto* | FINDING-005 | 20251111-HHMMSS-BRT-django-admin-login.png | *Substituído por HTML* | *-* | ✅ Substituído por 02-FINDING-005-django-admin-15112025-171800-BRT.html |
| *Obsoleto* | FINDING-005 | 20251111-HHMMSS-BRT-django-admin-csrf.png | *Substituído por HTML* | *-* | ✅ Substituído por 02-FINDING-005-django-admin-15112025-171800-BRT.html |

#### Captura de Rede (NENHUMA AINDA)

| Timestamp | Finding | Arquivo | Hash SHA256 | Tamanho | Descrição |
|-----------|---------|---------|-------------|---------|-----------|
| *N/A* | - | - | - | - | Nenhum PCAP capturado nesta sessão |

#### Scripts de Exploração (PENDENTE)

| Timestamp | Finding | Arquivo | Hash SHA256 | Tamanho | Descrição |
|-----------|---------|---------|-------------|---------|-----------|
| *Pendente* | FINDING-003 | exploit-registration-500.py | *TBD* | *TBD* | PoC exploit do endpoint de registro |
| *Pendente* | FINDING-005 | django-admin-bruteforce.py | *TBD* | *TBD* | Script de teste de credenciais Django Admin |

#### Outputs de Ferramentas (PARSEADOS - RAW DELETADOS)

| Timestamp | Ferramenta | Alvo | Arquivo Output | Status |
|-----------|-----------|------|-----------------|--------|
| 2025-11-11 14:28:00 BRT | gobuster | https://redahub.cloud | /tmp/gobuster-redahub-main.txt | ✅ Parseado → DELETE |
| 2025-11-11 14:28:00 BRT | gobuster | https://bkd.redahub.cloud | /tmp/gobuster-redahub-backend.txt | ✅ Parseado → DELETE |
| 2025-11-11 14:28:00 BRT | gobuster | http://3.84.175.55:3000 | /tmp/gobuster-easypanel.txt | ❌ Conexão recusada |
| 2025-11-11 14:30:00 BRT | curl | https://redahub.cloud/.env | /tmp/403-bypass-test.sh | ✅ Testado → DELETE |

---

## Instruções de Verificação

### Gerar Hash SHA256 (macOS)
```bash
shasum -a 256 filename.png
```

### Verificar Integridade
```bash
shasum -a 256 -c checksums.txt
```

### Arquivar Evidências (Fim do Engajamento)
```bash
# Criar arquivo a prova de adulteração
tar -czf evidence-REDAHUB-20251111.tar.gz 04-evidence/
shasum -a 256 evidence-REDAHUB-20251111.tar.gz > evidence-REDAHUB-20251111.tar.gz.sha256

# Criptografar para entrega ao cliente
gpg --encrypt --recipient client@redahub.cloud evidence-REDAHUB-20251111.tar.gz
```

---

## Assinaturas da Cadeia de Custódia

| Data | Operador | Ação | Assinatura |
|------|----------|------|-----------|
| 2025-11-11 14:35:00 BRT | Neural-OffSec-Team | Registro de cadeia de custódia criado | *Assinatura digital TBD* |
| 2025-11-15 17:18:00 BRT | Neural-OffSec-Team | 7 evidências técnicas capturadas e hashes SHA256 calculados | ✅ Concluído |
| 2025-11-15 17:18:00 BRT | Neural-OffSec-Team | Chain of custody atualizada com Sessão 2025-11-15 | ✅ Concluído |
| 2025-11-XX [TBD] | Neural-OffSec-Team | Evidências arquivadas e criptografadas | *Pendente* |
| 2025-11-XX [TBD] | Cliente REDAHUB | Evidências recebidas e verificadas | *Pendente* |

---

## Notas Legais

- Todas as evidências coletadas sob **acordo de teste de penetração autorizado**
- **Carta de Autorização** em arquivo: `00-ENGAGEMENT-INFO.md`
- Manipulação de evidências em conformidade com requisitos **LGPD** (GDPR Brasileiro)
- Cadeia de custódia mantida conforme diretrizes **ISO 27037:2012**
- Evidências admissíveis em procedimentos legais se necessário

---

**Última Atualização:** 2025-11-15 17:18:00 BRT
**Status:** 🟢 FASE 1 CONCLUÍDA (7 evidências capturadas, hashes validados)
