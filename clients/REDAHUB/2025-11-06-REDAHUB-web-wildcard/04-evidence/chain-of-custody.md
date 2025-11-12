# Registro de Cadeia de Custódia

---
**Timestamp do Documento:** 11-11-2025 14:35 BRT
**Engajamento:** 2025-11-06-REDAHUB-web-wildcard
**Operador:** Neural-OffSec-Team
**Cliente:** REDAHUB Sistema Editorial
**Timezone:** America/Sao_Paulo (BRT/BRST)
**Última Atualização:** 11-11-2025 14:35 BRT
---

## Propósito

Este documento mantém uma **cadeia de custódia legal** para todas as evidências coletadas durante o teste de penetração. Cada peça de evidência (screenshots, PCAPs, logs, exploits) deve ser registrada aqui com verificação criptográfica.

## Registro de Evidências

### Sessão 2025-11-11

#### Screenshots (CAPTURA PENDENTE)

| Timestamp | Finding | Arquivo | Hash SHA256 | Tamanho | Descrição |
|-----------|---------|---------|-------------|---------|-----------|
| *Pendente* | FINDING-001 | 20251111-HHMMSS-BRT-easypanel-login.png | *TBD* | *TBD* | Tela de login Easypanel porta 3000 exposta |
| *Pendente* | FINDING-003 | 20251111-HHMMSS-BRT-registration-500-error.png | *TBD* | *TBD* | Resposta HTTP 500 do endpoint de registro |
| *Pendente* | FINDING-003 | 20251111-HHMMSS-BRT-registration-payload.png | *TBD* | *TBD* | Payload de teste de registro em Burp/curl |
| *Pendente* | FINDING-004 | 20251111-HHMMSS-BRT-gobuster-403-results.png | *TBD* | *TBD* | Scan Gobuster mostrando 403 em arquivos sensíveis |
| *Pendente* | FINDING-004 | 20251111-HHMMSS-BRT-env-file-403-test.png | *TBD* | *TBD* | Teste curl mostrando .env retornando 403 |
| *Pendente* | FINDING-005 | 20251111-HHMMSS-BRT-django-admin-login.png | *TBD* | *TBD* | Painel Django Admin com formulário público de login |
| *Pendente* | FINDING-005 | 20251111-HHMMSS-BRT-django-admin-csrf.png | *TBD* | *TBD* | Token CSRF Django Admin visível no source |

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
| 2025-11-11 [TBD] | Neural-OffSec-Team | Screenshots capturados e hash gerado | *Pendente* |
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

**Última Atualização:** 2025-11-11 14:35:00 BRT
**Status:** 🟡 EM PROGRESSO (screenshots pendentes)
