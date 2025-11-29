# THREAT INTELLIGENCE REPORT - IOCs
## Case: IR-KALINE-2024-001
**Data:** 25/11/2024 19:36 (UTC-3)
**Classificacao:** CONFIDENCIAL - THREAT INTEL

---

## 1. EXECUTIVE SUMMARY

Investigacao OSINT identificou rede de paineis de dados ilegais operando no Brasil, oferecendo consultas de CPF, CNPJ, telefones e outros dados pessoais obtidos de vazamentos. A fonte do relatorio "Consulta [BOT]" faz parte deste ecossistema criminoso.

---

## 2. INDICATORS OF COMPROMISE (IOCs)

### 2.1 Dominios Maliciosos

| Dominio | IP | Status | Descricao |
|---------|-----|--------|-----------|
| botconsulta.com | 38.180.15.63 | ATIVO | Painel de consultas CPF/CNPJ |
| wolfbuscas.net | 172.67.145.229, 104.21.28.116 | ATIVO | Painel completo de consultas |
| detetive.pro | 172.67.218.160, 104.21.62.22 | ATIVO | API de consultas profissionais |
| caipora.pro | [Cloudflare] | ATIVO | Agregador OSINT |

### 2.2 Enderecos IP

```
# IPs Primarios (NAO Cloudflare)
38.180.15.63        # botconsulta.com - Cogent/NL - PRIORITARIO

# IPs Cloudflare (protegidos)
172.67.145.229      # wolfbuscas.net
104.21.28.116       # wolfbuscas.net
172.67.218.160      # detetive.pro
104.21.62.22        # detetive.pro
```

### 2.3 Infraestrutura Tecnica - botconsulta.com

```
IP:         38.180.15.63
Hosting:    Cogent Communications, LLC (US)
            Meppel, NL (Network)
Hostname:   a237571877.local

PORTAS ABERTAS:
- 22/tcp  SSH      OpenSSH 8.9p1 Ubuntu 3ubuntu0.13
- 80/tcp  HTTP     Apache httpd 2.4.52
- 443/tcp HTTPS    Apache httpd 2.4.52 (Ubuntu)

OS: Ubuntu Linux
```

### 2.4 Canais Telegram (C2/Distribuicao)

| Canal | Username | Membros | Tipo |
|-------|----------|---------|------|
| Detetive Pro | @painelconaultas | 9.970 | Vendas/Suporte |
| Wolf Buscas | @5970825168 | N/A | Suporte |
| Anonimo Bot | @annonimobotchannel | N/A | Bot Consultas |
| Canal Minerd | @canalminerdso | N/A | Material/APIs |
| PR1V8 | @pr1v8 | N/A | Vazamentos |
| VIVO FRI | @VIVOFRI | N/A | CC/Checkers |

### 2.5 Contatos Identificados

```
# Detetive.pro
Email:    contato@detetivepainel.com.br
Telefone: +55 17 997270582
Cidade:   Sao Paulo, SP - Brasil

# Wolf Buscas
Telegram: web.telegram.org/a/#5970825168
```

### 2.6 URLs de Login/Painel

```
https://botconsulta.com/login.php
https://www.wolfbuscas.net/auth/login
https://www.wolfbuscas.net/auth/register
https://detetive.pro/login
https://detetive.pro/signup
```

---

## 3. REPOSITORIOS GITHUB (Codigo Fonte)

### 3.1 Bots de Consulta Publicos

| Repositorio | Linguagem | Descricao |
|-------------|-----------|-----------|
| White1Hats/Bot-Consulta | JavaScript | Discord bot CPF/CNPJ/Placa |
| derxankvs/CenterApisV | Python | API Telegram + FastAPI |
| marcoskeh/Consultas_do_professor_bot | Python | Bot Telegram |
| rafinhadufluxo/Innerbloom | Node.js | Automacao CPF Puppeteer |

### 3.2 Analise White1Hats/Bot-Consulta

```
Plataforma: Discord (discord.js v14)
Funcoes:
- Consulta CPF
- Consulta CNPJ
- Consulta CEP
- Consulta IP
- Consulta Placa de veiculo

Comando: /consultapainel
API: Externa (nao especificada publicamente)
```

---

## 4. PRECOS E MONETIZACAO

### 4.1 Wolf Buscas

| Plano | Duracao | Preco |
|-------|---------|-------|
| Diaria | 24h | R$ 20,00 |
| Semanal | 7 dias | R$ 30,00 |
| Mensal | 30 dias | R$ 50,00 |
| Trimestral | 90 dias | R$ 80,00 |
| Semestral | 180 dias | R$ 90,00 |
| Anual | 365 dias | R$ 100,00 |
| Bianual | 730 dias | R$ 150,00 |
| Trienal | 1095 dias | R$ 200,00 |

### 4.2 Detetive.pro

| Plano | Creditos | Preco |
|-------|----------|-------|
| Starter | 350 | R$ 29,90/mes |
| Professional | 1.000 | R$ 79,90/mes |
| Enterprise | 2.500 | R$ 199,90/mes |

**Consultas Avulsas:**
- CPF Simples: R$ 0,20
- CPF Completo: R$ 1,20
- CNPJ: R$ 0,10
- Nome: R$ 3,00
- Telefone: R$ 3,00
- Placa: R$ 71,52
- Processos: R$ 14,40

---

## 5. TTPs (TACTICS, TECHNIQUES & PROCEDURES)

### 5.1 Cadeia de Ataque

```
[VAZAMENTO ORIGINAL]
     |
     v
[DARK WEB / FORUMS]
     |
     v
[COMPILADORES DE DADOS]
     |
     v
[APIs INTERMEDIARIAS]
     |
     v
[PAINEIS WEB] <---> [BOTS TELEGRAM/DISCORD]
     |
     v
[USUARIOS FINAIS (CRIMINOSOS)]
     |
     v
[VITIMAS - FRAUDES/GOLPES]
```

### 5.2 Tecnicas de Evasao

1. **Cloudflare** - Protecao DDoS e anonimizacao de IP real
2. **Telegram** - Comunicacao criptografada, canais anonimos
3. **PIX** - Pagamentos sem rastreio bancario tradicional
4. **Hospedagem offshore** - Servidores fora do Brasil

### 5.3 Fontes de Dados Suspeitas

- Mega Breach Brasil 2021 (223M pessoas)
- Vazamentos Serasa Experian
- TSE / DivulgaCand (fotos eleitorais)
- INSS / RAIS / PIS
- Detran estaduais
- Bases de operadoras de telefonia
- CadastroUnico / Auxilio Brasil

---

## 6. METRICAS DOS SERVICOS

### 6.1 Wolf Buscas (auto-declarado)

| Metrica | Valor |
|---------|-------|
| Consultas realizadas | 1M+ |
| Modulos disponiveis | 30+ |
| Usuarios ativos | 40K+ |

### 6.2 Detetive.pro (auto-declarado)

| Metrica | Valor |
|---------|-------|
| Usuarios ativos | 10.000+ |
| Consultas realizadas | 2M+ |
| Economia gerada | R$ 50M+ |
| APIs integradas | 50+ |

---

## 7. RECOMENDACOES DE BLOQUEIO

### 7.1 Firewall / DNS Block

```
# Dominios para bloqueio
botconsulta.com
wolfbuscas.net
detetive.pro
caipora.pro
*.wolfbuscas.net
*.detetive.pro

# IPs para bloqueio
38.180.15.63
```

### 7.2 Regras de Deteccao (SIEM)

```yaml
# Exemplo Sigma Rule
title: Access to Brazilian Data Leak Panel
status: experimental
logsource:
  category: proxy
detection:
  selection:
    cs-host|contains:
      - 'wolfbuscas'
      - 'botconsulta'
      - 'detetive.pro'
      - 'caipora.pro'
  condition: selection
falsepositives:
  - Legitimate security research
level: high
```

### 7.3 Denuncia

**Telegram:**
- Reportar canais via @NoToScam ou https://telegram.org/support

**Dominios:**
- Cloudflare Abuse: abuse@cloudflare.com
- Cogent Abuse: abuse@cogent.net

**Brasil:**
- ANPD: https://www.gov.br/anpd/
- SaferNet: https://new.safernet.org.br/denuncie

---

## 8. REFERENCIAS MITRE ATT&CK

| Tecnica | ID | Descricao |
|---------|-----|-----------|
| Phishing for Information | T1598 | Coleta de dados via engenharia social |
| Automated Collection | T1119 | Scraping automatizado de dados |
| Data from Information Repositories | T1213 | Acesso a bases de dados vazadas |
| Exfiltration Over Web Service | T1567 | Distribuicao via Telegram/Discord |
| Proxy | T1090 | Uso de Cloudflare para anonimato |

---

## 9. ASSINATURAS E HASHES

### 9.1 Artefato Original (PDF)

```
Arquivo:  relatorio.pdf
SHA256:   101539157caf03acc709baee0f8e60f4d994f623173b99fc3bff7f747681c8b3
Fonte:    Servico "Consulta [BOT]"
Copyright: 2024 Consulta [BOT]
```

---

## 10. TIMELINE DA INVESTIGACAO

| Data/Hora | Evento |
|-----------|--------|
| 25/11/2024 19:25 | Artefato recebido via monitoramento |
| 25/11/2024 19:26 | Inicio da analise IR |
| 25/11/2024 19:29 | OSINT threat intel iniciado |
| 25/11/2024 19:32 | Paineis de dados identificados |
| 25/11/2024 19:36 | Scan de portas botconsulta.com |
| 25/11/2024 19:36 | IOCs compilados |

---

**CLASSIFICACAO:** CONFIDENCIAL - THREAT INTELLIGENCE
**DISTRIBUICAO:** Equipe IR, SOC, Legal
**RETENCAO:** Conforme politica de retencao de incidentes
**AUTOR:** Neural OffSec IR Team
