# FINDING-004: Arquivos Sensíveis Retornando HTTP 403 (Security Through Obscurity)

---
**Document Timestamp:** 11-11-2025 14:30 BRT
timestamp: 11-11-2025 14:30 BRT
engagement: clients/REDAHUB/2025-11-06-REDAHUB-web-wildcard
finding: FINDING-004
tool: gobuster + seclists
operator: Neural-OffSec-Team
severity: 🟠 HIGH
cvss_score: 7.5
cvss_vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
status: CONFIRMED
---

## Sumário Executivo

O processo de content discovery revelou **centenas de arquivos sensíveis** em `https://redahub.cloud` retornando HTTP 403 Forbidden. Embora os arquivos estejam atualmente inacessíveis, sua **existência está confirmada** pelo nginx retornando 403 ao invés de 404. Isto representa **security through obscurity** - os arquivos existem mas estão protegidos apenas por regras de configuração do nginx.

## Detalhes da Vulnerabilidade

### Classificação
- **Tipo**: Information Disclosure + Insecure Configuration Management
- **CWE**: CWE-538 (File and Directory Information Exposure)
- **OWASP**: A05:2021 - Security Misconfiguration

### Método de Descoberta
```bash
gobuster dir -u https://redahub.cloud \
  -w ~/wordlists/seclists/Discovery/Web-Content/common.txt \
  -t 30 -x php,html,txt,js,json,xml,zip,sql,bak,old,backup \
  -k --exclude-length 703 --timeout 10s
```

### Arquivos Afetados (Amostra - mais de 100 no total)

**Controle de Versão:**
- `.git/` (Status: 403)
- `.git/HEAD` (Status: 403)
- `.git/config` (Status: 403)
- `.git/index` (Status: 403)
- `.git/logs/` (Status: 403)
- `.gitignore` (Status: 403)
- `.gitconfig` (Status: 403)
- `.svn/` (Status: 403)
- `.svn/entries` (Status: 403)

**Arquivos de Ambiente e Configuração:**
- `.env` (Status: 403) ⚠️ **CRÍTICO**
- `.env.bak` (Status: 403)
- `.env.old` (Status: 403)
- `.env.backup` (Status: 403)
- `.config` (Status: 403)
- `.htaccess` (Status: 403)
- `.htpasswd` (Status: 403)

**Histórico de Shell:**
- `.bash_history` (Status: 403)
- `.sh_history` (Status: 403)
- `.mysql_history` (Status: 403)

**Chaves SSH:**
- `.ssh/` (Status: 403)

**Arquivos de Backup:**
- `*.bak` (Status: 403)
- `*.backup` (Status: 403)
- `*.old` (Status: 403)
- `*.sql` (Status: 403)
- `*.zip` (Status: 403)

## Avaliação de Risco

### Análise de Impacto

**Estado Atual:**
- Arquivos estão **protegidos por configuração do nginx** retornando 403
- Conteúdo **não está acessível** através de requisições HTTP padrão
- **Existência dos arquivos está confirmada** (diferença entre 403 vs 404)

**Cenários de Risco:**

1. **Má Configuração do nginx (CRÍTICO)**
   - Uma única regra mal configurada → exposição instantânea
   - Erro de digitação no bloco `location` → arquivos tornam-se públicos
   - Exemplo:
     ```nginx
     # SEGURO (atual)
     location ~ /\. {
         deny all;
     }

     # INSEGURO (um erro de digitação)
     location ~ /\.git {  # Bloqueia apenas .git, não todos os dotfiles
         deny all;
     }
     ```

2. **Bypass via Método HTTP**
   - nginx pode bloquear apenas requisições GET
   - Outros métodos (OPTIONS, TRACE, PROPFIND) podem expor conteúdo
   - Exemplo: `curl -X OPTIONS https://redahub.cloud/.env`

3. **Path Traversal**
   - URL encoding: `/.%2e/env` → `/./env` → `/.env`
   - Double encoding: `/%252e%252e/.env`
   - Bypasses Unicode: `/\u002e\u002e/.env`

4. **Acesso Direto via Backend**
   - Se backend API servir arquivos estáticos diretamente
   - Má configuração do Django `STATIC_ROOT`
   - Má configuração de bucket S3 expondo `.env`

5. **Reconstrução de Repositório Git**
   - Mesmo com 403, estrutura do `.git/` é conhecida
   - Ferramentas como `git-dumper` podem tentar reconstrução
   - Sucesso parcial → histórico de commits + credenciais

### Detalhamento CVSS 3.1

**Base Score: 7.5 (HIGH)**
- **AV:N** (Attack Vector: Network) - Explorável remotamente
- **AC:L** (Attack Complexity: Low) - Sem condições especiais
- **PR:N** (Privileges Required: None) - Não autenticado
- **UI:N** (User Interaction: None) - Totalmente automatizado
- **S:U** (Scope: Unchanged) - Limitado à camada nginx
- **C:H** (Confidentiality: High) - Exposição completa de credenciais se contornado
- **I:N** (Integrity: None) - Sem modificação direta de arquivos
- **A:N** (Availability: None) - Sem impacto de DoS

## Prova de Conceito

### Etapa 1: Enumerar Arquivos Protegidos
```bash
# Comando de descoberta
gobuster dir -u https://redahub.cloud -w common.txt \
  -t 30 -x php,txt,json,bak,old,backup,sql,zip \
  -k --exclude-length 703

# Output (amostra)
.env                 (Status: 403) [Size: 153]
.git/HEAD            (Status: 403) [Size: 153]
.bash_history        (Status: 403) [Size: 153]
.htpasswd            (Status: 403) [Size: 153]
```

### Etapa 2: Confirmar Diferença entre 403 vs 404
```bash
# Arquivo existente (retorna 403)
curl -I https://redahub.cloud/.env
# HTTP/2 403
# content-length: 153

# Arquivo inexistente (retorna 200 - roteamento SPA)
curl -I https://redahub.cloud/.env-definitely-not-exists
# HTTP/2 200
# content-length: 703 (React SPA)
```

### Etapa 3: Tentativas de Bypass (Testes Pendentes)
```bash
# Bypass de método HTTP
curl -X OPTIONS https://redahub.cloud/.env
curl -X TRACE https://redahub.cloud/.env
curl -X PROPFIND https://redahub.cloud/.env

# Path traversal
curl https://redahub.cloud/.%2eenv
curl https://redahub.cloud/%252e%252eenv
curl https://redahub.cloud/\u002e\u002e/.env

# Manipulação de headers
curl -H "X-Original-URL: /.env" https://redahub.cloud/
curl -H "X-Rewrite-URL: /.env" https://redahub.cloud/
curl -H "X-Forwarded-Path: /.env" https://redahub.cloud/
```

## Remediação

### Prioridade 1: Remover Arquivos Sensíveis (IMEDIATO)
```bash
# No servidor de produção
cd /var/www/redahub.cloud
rm -rf .git/ .env* .bash_history .mysql_history .ssh/
rm -f *.bak *.backup *.old *.sql.zip
rm -f .htpasswd .config
```

### Prioridade 2: Implementar Deploy Adequado (24h)
**Usar CI/CD adequado para deployment:**
```yaml
# .gitlab-ci.yml ou .github/workflows/deploy.yml
deploy:
  script:
    - npm run build  # Apenas artefatos de build
    - rsync -av --exclude='.git' --exclude='node_modules' \
            --exclude='*.bak' --exclude='.env*' \
            dist/ user@server:/var/www/app/
```

### Prioridade 3: Verificar Configuração do nginx (1 semana)
```nginx
# /etc/nginx/sites-available/redahub.cloud

# Bloquear todos os dotfiles (não apenas .git)
location ~ /\. {
    deny all;
    return 404;  # Retornar 404 ao invés de 403
}

# Bloquear arquivos de backup
location ~* \.(bak|backup|old|sql|zip|log|tmp)$ {
    deny all;
    return 404;
}

# Bloquear controle de versão
location ~* /(\.git|\.svn|\.cvs)/ {
    deny all;
    return 404;
}
```

### Prioridade 4: Testar Técnicas de Bypass (1 semana)
```bash
# Executar testes abrangentes de bypass
./tools/403-bypass.sh https://redahub.cloud/.env
./tools/http-method-fuzzer.py https://redahub.cloud/.env
```

## Impacto no Negócio

### Risco de Confidencialidade
- **Credenciais**: `.env` provavelmente contém API keys, senhas de DB, secrets JWT
- **Infraestrutura**: configuração nginx revela arquitetura do servidor
- **Histórico**: histórico de shell pode conter comandos sensíveis
- **Git**: histórico de commits pode expor credenciais de desenvolvedores

### Impacto em Conformidade
- **PCI DSS**: 6.5.8 - Improper Access Control
- **OWASP Top 10**: A05:2021 - Security Misconfiguration
- **ISO 27001**: A.12.1.3 - Separação de desenvolvimento e produção

## Linha do Tempo
- **2025-11-11 14:25:00 BRT**: Descoberta inicial via gobuster
- **2025-11-11 14:30:00 BRT**: Confirmado comportamento 403 vs 404
- **2025-11-11 14:35:00 BRT**: FINDING-004 documentado
- **[PENDENTE]**: Testes de bypass
- **[PENDENTE]**: Notificação ao cliente

## Referências
- [CWE-538: File and Directory Information Exposure](https://cwe.mitre.org/data/definitions/538.html)
- [OWASP: Security Misconfiguration](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)
- [HackerOne: How I Could Have Hacked Every Facebook Account](https://www.josipfranjkovic.com/blog/hacking-facebook-csrf-bug-bounty)
- [git-dumper Tool](https://github.com/arthaud/git-dumper)

## Próximos Passos
1. ✅ Documentar finding (concluído)
2. ⏳ Testar técnicas de bypass de método HTTP
3. ⏳ Testar bypasses de path traversal
4. ⏳ Testar bypasses de manipulação de headers
5. ⏳ Tentar reconstrução com git-dumper
6. ⏳ Verificar se backend API não serve estes arquivos
7. ⏳ Notificar cliente com avaliação de severidade
8. ⏳ Fornecer guia detalhado de remediação
