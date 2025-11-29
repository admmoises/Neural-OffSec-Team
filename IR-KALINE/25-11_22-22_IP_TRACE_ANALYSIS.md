# IR-KALINE - IP TRACE ANALYSIS (ULTRATHINK BLACK)
## Data: 25/11/2024 22:22 (Sessao 4 - Parte 2)
## Status: ANALISE DE VAZAMENTO DE IP

---

## DESCOBERTA CRITICA

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  MEGABREACH BRASIL 2021 NAO CONTEM IPs DE ACESSO                              ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  O que o Megabreach CONTEM:                                                   ║
║  • Latitude/Longitude (geolocalizacao do ENDERECO FISICO)                    ║
║  • NAO sao IPs de acesso a internet                                           ║
║                                                                               ║
║  Se KALINE teve IP vazado, a fonte e OUTRA:                                   ║
║  • Stealer Logs (malware como RedLine, Raccoon, Vidar)                       ║
║  • Logs de sessao de aplicativos/servicos web                                ║
║  • Vazamento de operadora/ISP                                                 ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## 1. CAMPOS DO MEGABREACH 2021 (Esclarecimento)

### O que ESTA no Megabreach:

| Campo | Conteudo | Tipo |
|-------|----------|------|
| **Endereco** | Logradouro, numero, bairro, cidade, UF, CEP | Texto |
| **Latitude** | Coordenada geografica do endereco | Float |
| **Longitude** | Coordenada geografica do endereco | Float |
| Telefone | DDD + Numero + Operadora + Tipo linha | Texto |
| CPF | Identificacao fiscal | Texto |
| Nome | Nome completo | Texto |

### O que NAO ESTA no Megabreach:

| Campo | Status |
|-------|--------|
| **IP de acesso** | NAO INCLUIDO |
| **IP de sessao** | NAO INCLUIDO |
| **Logs de navegacao** | NAO INCLUIDO |
| **User-Agent** | NAO INCLUIDO |
| **Cookies** | NAO INCLUIDO |
| **Senhas** | PARCIALMENTE (bases separadas) |

**CONCLUSAO**: Se voce viu um IP associado a KALINE em algum painel, NAO veio do Megabreach 2021.

---

## 2. FONTES PROVAVEIS DE VAZAMENTO DE IP

### 2.1 Stealer Logs (MAIS PROVAVEL)

```
┌─────────────────────────────────────────────────────────────────┐
│  STEALER LOGS - COMO FUNCIONAM                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Vitima instala malware (via phishing, crack, etc.)          │
│  2. Malware coleta:                                              │
│     • IP do dispositivo                                          │
│     • Senhas salvas no navegador                                │
│     • Cookies de sessao                                          │
│     • Historico de navegacao                                     │
│     • Dados de cartao de credito                                │
│     • Dados do sistema (OS, hardware)                           │
│  3. Dados enviados para C2 do atacante                          │
│  4. Logs vendidos em mercados underground                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Principais Infostealers:**

| Malware | Status 2024 | Dados Coletados |
|---------|-------------|-----------------|
| **RedLine** | Desativado (Out/2024) | IP, senhas, cookies, CC |
| **Raccoon** | Ativo | IP, senhas, cookies, wallet |
| **Lumma** | Dominante 2024 | IP, senhas, cookies, 2FA |
| **Vidar** | Ativo | IP, senhas, historico |
| **RisePro** | Crescendo | IP, senhas, dados OS |

### 2.2 Vazamentos de Operadoras/ISPs

**Vazamento Operadoras SET/2022:**
- Oi, TIM, Claro, Vivo
- 1.5 milhoes de registros
- Campos: Nome, CPF, endereco, telefone, data instalacao
- **NAO INCLUIA IPs de navegacao**

**Vazamento SUS SET/2024:**
- 177.9 milhoes de registros
- Campos: CPF, nome, endereco, telefone, CNS
- **NAO INCLUIA IPs de navegacao**

### 2.3 Logs de Aplicativos/Servicos

Se KALINE usou algum servico que foi comprometido, o IP pode ter vazado:

| Tipo de Servico | Dados que Logam |
|-----------------|-----------------|
| Redes Sociais | IP de login, device fingerprint |
| E-commerce | IP de compra, IP de sessao |
| Bancos | IP de acesso (raramente vazam) |
| Jogos Online | IP de sessao |
| Apps de Namoro | IP de login, geolocalizacao |

---

## 3. COMO VERIFICAR SE KALINE TEM IP VAZADO

### 3.1 Ferramentas Legitimas

| Ferramenta | URL | Busca Por |
|------------|-----|-----------|
| **Have I Been Pwned** | haveibeenpwned.com | Email |
| **DeHashed** | dehashed.com | Email, telefone, IP, nome |
| **BreachDirectory** | breachdirectory.com | Email, username |
| **LeakCheck** | leakcheck.io | Email |
| **Snusbase** | snusbase.com | Email, username, IP |

### 3.2 Dados para Consulta

Para verificar vazamentos associados a KALINE:

```
EMAIL: chavespereirakaline@gmail.com
TELEFONE 1: +5563992237479
TELEFONE 2: +5563991302672
CPF: 09126926180
NOME: KALINE CHAVES PEREIRA
```

### 3.3 Consulta HIBP (Gratuita)

```bash
# Verificar email em Have I Been Pwned
curl "https://haveibeenpwned.com/unifiedsearch/chavespereirakaline@gmail.com"
```

### 3.4 Consulta DeHashed (Paga)

DeHashed permite buscar por:
- Email → Retorna IPs associados (se em stealer logs)
- Telefone → Retorna credenciais associadas
- IP → Retorna emails/usuarios associados

---

## 4. BREACHES QUE INCLUEM IPs

### 4.1 Data Troll Stealer Logs (Jun/2025)

| Metrica | Valor |
|---------|-------|
| Registros | 2.7 bilhoes de linhas |
| Emails unicos | 109 milhoes |
| Tamanho | 775 GB (10 arquivos JSON) |
| Novos emails | 4.4 milhoes |
| Dados | Email, senha, IP, cookies |

**Status**: Adicionado ao HIBP em Ago/2025

### 4.2 ALIEN TXTBASE (Jan/2024)

| Metrica | Valor |
|---------|-------|
| Registros | 23 bilhoes de linhas |
| Conteudo | Credenciais, cookies, IPs, dados pessoais |
| Origem | Compilacao de stealer logs |

### 4.3 Outros Breaches com IPs

- Collection #1-5 (2019)
- Compilation of Many Breaches (COMB)
- Facebook 533M (2021) - sem IPs
- LinkedIn 700M (2021) - sem IPs

---

## 5. CENARIO: COMO IP DE KALINE PODERIA TER VAZADO

### Cenario 1: Infeccao por Stealer

```
┌─────────────────────────────────────────────────────────────────┐
│  CENARIO: KALINE INFECTADA POR REDLINE/RACCOON                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. KALINE baixa programa pirata / crack / mod de jogo          │
│  2. Programa contem RedLine/Raccoon embutido                    │
│  3. Malware coleta:                                              │
│     • IP: 191.x.x.x (Tocantins - Vivo/OI)                       │
│     • Senhas do Chrome: Facebook, Gmail, etc.                   │
│     • Cookies de sessao                                          │
│  4. Dados enviados para C2                                       │
│  5. Log vendido em mercado underground                          │
│  6. Dado agregado em compilacoes (Data Troll, ALIEN TXTBASE)    │
│  7. Painel de dados (botconsulta, etc.) acessa via API          │
│                                                                  │
│  PROBABILIDADE: MEDIA-ALTA                                       │
│  (Perfil de revenda de eletronicos pode indicar familiaridade   │
│   com downloads de origens questionaveis)                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Cenario 2: Vazamento de Servico Web

```
┌─────────────────────────────────────────────────────────────────┐
│  CENARIO: SERVICO USADO POR KALINE FOI COMPROMETIDO             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Servicos que KALINE provavelmente usa:                         │
│  • Facebook (confirmado)                                         │
│  • WhatsApp (confirmado)                                         │
│  • TikTok (provavel)                                            │
│  • Instagram (familia)                                           │
│  • Vakinha.com.br (crowdfunding - confirmado)                   │
│  • Marketplace/OLX (revenda)                                     │
│  • Bancos (provavel)                                             │
│                                                                  │
│  Se algum desses vazou logs com IPs → IP de KALINE exposto      │
│                                                                  │
│  PROBABILIDADE: MEDIA                                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Cenario 3: Logs de ISP/Operadora

```
┌─────────────────────────────────────────────────────────────────┐
│  CENARIO: VAZAMENTO INTERNO DE OPERADORA                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Operadoras em Araguaina-TO:                                     │
│  • Vivo                                                          │
│  • Claro                                                         │
│  • OI (historico de problemas de seguranca)                     │
│  • TIM                                                           │
│                                                                  │
│  O vazamento de SET/2022 das operadoras NAO incluia IPs,        │
│  mas vazamentos internos nao documentados podem existir.         │
│                                                                  │
│  PROBABILIDADE: BAIXA                                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. PROXIMOS PASSOS PARA RASTREAR IP

### 6.1 Verificacao Imediata (Gratuita)

1. **Have I Been Pwned**
   - Consultar: `chavespereirakaline@gmail.com`
   - Verificar em quais breaches aparece
   - Se aparecer em "stealer logs" → IP provavelmente vazado

2. **Mozilla Monitor**
   - URL: monitor.mozilla.org
   - Mesma funcionalidade do HIBP

### 6.2 Verificacao Paga (Recomendada)

1. **DeHashed** (~$15/mes)
   - Buscar por email → ver IPs associados
   - Buscar por telefone → ver credenciais
   - Permite download dos dados brutos

2. **Snusbase** (~$29/mes)
   - Foco em stealer logs
   - Retorna IPs se disponiveis

3. **IntelX** (intelligence.x)
   - Busca em dark web
   - Inclui pastes, leaks, stealer logs

### 6.3 Acesso ao Megabreach (Contexto)

**RaidForums** (fonte original):
- Fechado em Abril/2022 pela FBI
- Dominio apreendido

**BreachForums** (sucessor):
- Atualmente ativo
- Dados do Megabreach 2021 ainda circulam
- Requer registro e creditos para download

**AVISO**: Download de dados vazados e ilegal na maioria das jurisdicoes. Para fins de threat intelligence, use ferramentas como DeHashed que indexam os dados de forma pesquisavel.

---

## 7. CONCLUSAO

### Resposta a Pergunta "Onde vazou o IP?"

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  STATUS: IP DE KALINE NAO CONFIRMADO EM VAZAMENTOS                            ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  O que sabemos:                                                               ║
║  • Megabreach 2021 NAO contem IPs (apenas lat/long de endereco)              ║
║  • Se o IP de KALINE vazou, foi de STEALER LOGS ou outro breach              ║
║  • Para confirmar, necessario consultar DeHashed/Snusbase com o email        ║
║                                                                               ║
║  Fontes mais provaveis (se IP vazou):                                         ║
║  1. Stealer logs (RedLine, Raccoon, Lumma) → Infeccao por malware            ║
║  2. Data Troll compilation (Jun/2025) → Se email em HIBP                     ║
║  3. ALIEN TXTBASE (Jan/2024) → 23B linhas de stealer logs                    ║
║                                                                               ║
║  ACAO NECESSARIA:                                                             ║
║  • Consultar email em HIBP para ver breaches                                  ║
║  • Se quiser IPs especificos: DeHashed ou Snusbase                           ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## 8. FONTES

- [Tecnoblog - Megavazamento](https://tecnoblog.net/noticias/exclusivo-vazamento-que-expos-220-milhoes-de-brasileiros-e-pior-do-que-se-pensava/)
- [Syhunt - Brazil Data Leak](https://www.syhunt.com/pt/index.php?n=Articles.BrazilDataLeak2021)
- [Have I Been Pwned - Data Troll](https://haveibeenpwned.com/breach/DataTrollStealerLogs)
- [Troy Hunt - Data Troll Analysis](https://www.troyhunt.com/that-16-billion-password-story-aka-data-troll/)
- [Flare - RedLine Stealer](https://flare.io/learn/resources/blog/redline-stealer-malware/)
- [SOCRadar - Stealer Logs](https://socradar.io/stealer-logs-everything-you-need-to-know/)
- [DeHashed](https://dehashed.com/)
- [TecMundo - Vazamento Operadoras 2022](https://www.tecmundo.com.br/seguranca/246302-oi-vivo-tim-claro-envolvidas-novo-vazamento-dados.htm)

---

**AUTOR:** Neural OffSec IR Team
**METODOLOGIA:** ULTRATHINK BLACK - IP Trace Analysis
**CLASSIFICACAO:** CONFIDENCIAL
