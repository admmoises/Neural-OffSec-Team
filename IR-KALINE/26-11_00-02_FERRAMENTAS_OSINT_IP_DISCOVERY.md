# Relatorio de Pesquisa Tecnica - Ferramentas OSINT para IR-KALINE

**Data/Hora da Pesquisa:** 26-11-2025 00:02 (Sao Paulo)
**Escopo:** Ferramentas para IP Discovery, Breach Databases, Canary Tokens, ISP Intelligence e OSINT Brasil
**Metodologia:** Pesquisa exaustiva web com multiplas ondas de busca
**Sessao IR:** Session 7 - Hunting IP Real do Alvo

---

## Resumo Executivo

Este relatorio compila **100+ ferramentas** organizadas em 5 categorias principais para auxiliar na investigacao IR-KALINE. O objetivo central eh identificar o IP real do alvo atraves de tecnicas combinadas de OSINT, breach databases e canary tokens.

As descobertas mais relevantes para o caso incluem:
1. **Ferramentas de IP Search Engines** alternativas ao Shodan com cobertura especifica para America Latina
2. **Stealer Logs no Telegram** que podem conter IP + credenciais da vitima
3. **Vazamento massivo brasileiro de 223M CPFs** com dados associados
4. **Canary token services** para captura ativa de IP
5. **BGP Tools** para mapeamento da infraestrutura do ISP Aranet

---

## CATEGORIA 1: OSINT Tools para IP Discovery

### 1.1 IP Search Engines (Alternativas ao Shodan)

| Ferramenta | URL | Funcionalidade | Custo | Relevancia |
|------------|-----|----------------|-------|------------|
| **Criminal IP** | https://www.criminalip.io/ | Scanner + CTI, analise de phishing, risk assessment de IP | Freemium | ALTA |
| **FOFA** | https://fofa.info/ | Ampla cobertura de portas, forte no segmento asiatico | Pago | MEDIA |
| **Netlas** | https://netlas.io/ | EASM, 146 portas, dados uniformes e frescos | Free tier + Pago | ALTA |
| **BinaryEdge** | https://www.binaryedge.io/ | Portas abertas, alertas real-time | Freemium | MEDIA |
| **Censys** | https://search.censys.io/ | Detalhes completos de hosts, certificados | Free tier + Pago | ALTA |
| **ZoomEye** | https://www.zoomeye.org/ | Forte em alvos raros/long-exposed | Free tier | MEDIA |
| **LeakIX** | https://leakix.net/ | Deteccao de breaches em tempo real | Gratuito | ALTA |
| **FullHunt** | https://fullhunt.io/ | EASM completo, descoberta de ativos | Pago | MEDIA |
| **GreyNoise** | https://www.greynoise.io/ | Tracking de scanners maliciosos | Freemium | BAIXA |
| **ONYPHE** | https://www.onyphe.io/ | ASM + CTI, scanning desde 2017 | Pago | ALTA |
| **Pulsedive** | https://pulsedive.com/ | 40+ feeds OSINT agregados | Freemium | MEDIA |

### 1.2 Email/Phone to IP Correlation

| Ferramenta | URL | Funcionalidade | Custo | Relevancia |
|------------|-----|----------------|-------|------------|
| **Epieos** | https://epieos.com/ | Reverse email, 140+ services, Google + Skype | $32/mes | ALTA |
| **Holehe** | https://github.com/megadose/holehe | Check email em 120+ plataformas | Gratuito (Python) | ALTA |
| **EmailSherlock** | https://www.emailsherlock.com/ | Lookup de origem + perfis sociais | Gratuito | MEDIA |
| **Phonebook.cz** | https://phonebook.cz/ | Email + telefone search em datasets massivos | Gratuito | ALTA |
| **OSINT.email** | https://osint.email/ | Suite de analise de email + MX records | Gratuito | MEDIA |

### 1.3 Email Header Analysis (IP Extraction)

| Ferramenta | URL | Funcionalidade | Custo | Relevancia |
|------------|-----|----------------|-------|------------|
| **MxToolbox Header Analyzer** | https://mxtoolbox.com/EmailHeaders.aspx | Parse de headers, trace de IP | Gratuito | ALTA |
| **Google Messageheader** | https://toolbox.googleapps.com/apps/messageheader/ | Breakdown detalhado | Gratuito | ALTA |
| **CyberChef** | https://gchq.github.io/CyberChef/ | Parse + Extract URLs de headers | Gratuito | MEDIA |
| **EspySys Header Analyzer** | https://espysys.com/tools/email-header-analyzer | SMTP analysis avancado | Gratuito | MEDIA |

---

## CATEGORIA 2: Breach Database Tools

### 2.1 Servicos de Lookup de Credenciais Vazadas

| Ferramenta | URL | Funcionalidade | Custo | Relevancia |
|------------|-----|----------------|-------|------------|
| **DeHashed** | https://dehashed.com/ | Busca em bilhoes de registros, IPs + usernames | Pago (~$5.49/mes) | ALTA |
| **Snusbase** | https://snusbase.com/ | Interface intuitiva, filtros avancados | Pago | ALTA |
| **LeakCheck** | https://leakcheck.io/ | Clear text passwords de usernames/emails | Pago | ALTA |
| **Intelligence X** | https://intelx.io/ | Dark web archives, breach databases | Freemium | ALTA |
| **Have I Been Pwned** | https://haveibeenpwned.com/ | Check de breach por email | Gratuito | MEDIA |
| **Leak-Lookup** | https://leak-lookup.com/ | Username, email, IP search | Pago | ALTA |
| **BreachDirectory** | https://breachdirectory.com/ | Motor de busca de breaches | Freemium | MEDIA |
| **LeakPeek** | https://leakpeek.com/ | Busca simplificada de leaks | Pago | MEDIA |
| **WeLeakInfo** | https://weleakinfo.io/ | Database de credenciais | Pago | MEDIA |
| **ScatteredSecrets** | https://scatteredsecrets.com/ | Verificacao de comprometimento | Freemium | BAIXA |
| **Mozilla Monitor** | https://monitor.mozilla.org/ | Monitoramento gratuito de breaches | Gratuito | BAIXA |

### 2.2 Stealer Logs & Infostealer Intelligence

| Ferramenta | URL | Funcionalidade | Custo | Relevancia |
|------------|-----|----------------|-------|------------|
| **Hudson Rock Cavalier** | https://www.hudsonrock.com/ | API de 30M+ computadores comprometidos | Enterprise | ALTA |
| **Russian Market** (Dark Web) | Tor Only | 30k+ bots/mes, dominante pos-Genesis | Crypto | ALTA |
| **Telegram Stealer Channels** | Telegram App | Moon Cloud, Daisy Cloud - logs gratis | Gratuito | ALTA |
| **Flare.io** | https://flare.io/ | Monitoramento de stealer logs | Enterprise | MEDIA |
| **BreachSense** | https://www.breachsense.com/ | Tracker diario de ransomware leaks | Pago | MEDIA |

### 2.3 Vazamentos Brasileiros Especificos

| Fonte | Dados | Tamanho | Relevancia |
|-------|-------|---------|------------|
| **Megabreach 2021** | CPF, nome, DOB, genero, endereco, score credito | 223M registros | CRITICA |
| **SUS Breach 2024** | CPF, cartao SUS, nomes dos pais, enderecos, telefones | 177M rows | CRITICA |
| **DataBreach.com SUS** | https://databreach.com/breach/sus-brazil-2024 | Lookup disponivel | ALTA |

---

## CATEGORIA 3: Social Engineering / Canary Tools

### 3.1 IP Grabber / Logger Services

| Ferramenta | URL | Funcionalidade | Custo | Relevancia |
|------------|-----|----------------|-------|------------|
| **Grabify** | https://grabify.link/ | Smart Logger: IP, browser, OS, bateria, orientacao | Gratuito | ALTA |
| **IP Logger** | https://iplogger.org/ | Multi-URL types, export de IPs, metricas | Gratuito | ALTA |
| **Grabify.org** | https://grabify.org/ | Clone alternativo | Gratuito | MEDIA |
| **IPLogger.site** | https://iplogger.site/ | Logger basico | Gratuito | MEDIA |
| **Detectico** | https://detectico.com/ip-tracker/ | Requer conta, geolocalizacao | Freemium | MEDIA |
| **Bit.ly** | https://bitly.com/ | URL shortener com analytics | Freemium | BAIXA |

### 3.2 Canary Token Services

| Ferramenta | URL | Funcionalidade | Custo | Relevancia |
|------------|-----|----------------|-------|------------|
| **CanaryTokens.org** | https://canarytokens.org/ | Web bugs, docs, API keys, QR codes, VPN profiles | Gratuito | ALTA |
| **CanaryTokens (Self-hosted)** | https://github.com/thinkst/canarytokens | Controle total, dominio customizado | Gratuito (OSS) | ALTA |
| **Trapster** | https://trapster.io/ | Honeytokens + honeypots, 15+ protocolos | Pago | MEDIA |
| **OpenCanary** | https://github.com/thinkst/opencanary | Honeypot modular, alertas de abuso | Gratuito (OSS) | MEDIA |
| **HoneyLambda** | https://github.com/0x4D31/honeylambda | URL honeytokens serverless (AWS Lambda) | Gratuito (OSS) | MEDIA |
| **Honeybits** | https://github.com/0x4D31/honeybits | Breadcrumbs em servidores de producao | Gratuito (OSS) | BAIXA |

### 3.3 Webhook/Request Catchers (IP Capture)

| Ferramenta | URL | Funcionalidade | Custo | Relevancia |
|------------|-----|----------------|-------|------------|
| **Webhook.site** | https://webhook.site/ | Captura HTTP requests, inspeccao completa | Freemium | ALTA |
| **Beeceptor** | https://beeceptor.com/ | Sem signup, respostas customizadas | Freemium | ALTA |
| **RequestBin (Pipedream)** | https://pipedream.com/requestbin | Integracao com workflow automation | Gratuito | MEDIA |
| **DevToolLab** | https://devtoollab.com/webhook | URLs permanentes, storage ilimitado | Gratuito | MEDIA |
| **Hookdeck** | https://hookdeck.com/ | Enterprise-grade, debug avancado | Pago | BAIXA |

### 3.4 Device Fingerprinting

| Ferramenta | URL | Funcionalidade | Custo | Relevancia |
|------------|-----|----------------|-------|------------|
| **IPQualityScore** | https://www.ipqualityscore.com/device-fingerprinting | 300+ data points, anti-spoofing | Free tier (5k/mes) | ALTA |
| **FingerprintJS** | https://github.com/fingerprintjs/fingerprintjs | Browser fingerprint open-source | Gratuito (BSL) | ALTA |
| **ThumbmarkJS** | https://github.com/thumbmarkjs/thumbmarkjs | MIT license, 60k+ websites | Gratuito (OSS) | ALTA |
| **AmIUnique** | https://amiunique.org/ | Teste de unicidade de fingerprint | Gratuito | BAIXA |

---

## CATEGORIA 4: ISP/Network Intelligence

### 4.1 BGP/ASN Lookup Tools

| Ferramenta | URL | Funcionalidade | Custo | Relevancia |
|------------|-----|----------------|-------|------------|
| **BGP.Tools** | https://bgp.tools/ | Debug BGP, rankings Brasil | Gratuito | ALTA |
| **Hurricane Electric BGP** | https://bgp.he.net/ | Prefix/Peer reports, traceroute | Gratuito | ALTA |
| **BGPView** | https://bgpview.io/ | ASN summary, IP allocations Brasil | Gratuito (shutdown 26/11/2025) | ALTA |
| **RIPEstat** | https://stat.ripe.net/ | BGPlay, analytics de routing | Gratuito | MEDIA |
| **Gcore Looking Glass** | https://lg.gcore.lu/ | Teste de conectividade global | Gratuito | MEDIA |

**Para Aranet (AS262462):**
- https://bgp.he.net/AS262462
- https://bgp.tools/as/262462

### 4.2 TR-069/CWMP Tools & Vulnerabilities

| Recurso | URL/Referencia | Tipo | Relevancia |
|---------|----------------|------|------------|
| **TR-069 NewNTPServer Exploits** | SANS ISC Diary #21763 | Documentacao | ALTA |
| **Mirai TR-069 Exploitation** | QA Cafe Research | Analise | ALTA |
| **TP-Link 0-day (May 2024)** | CVE pendente, buffer overflow em CWMP | Vuln ativa | ALTA |
| **Porta 7547/TCP** | Porta padrao TR-069 | Target | ALTA |
| **Misfortune Cookie** | Checkpoint Whitepaper | Vuln historica | MEDIA |

**Nota:** A exploracao de TR-069 sem autorizacao eh crime (Art. 154-A CP). Use apenas para reconhecimento passivo.

### 4.3 ISP Customer Enumeration

| Metodo | Descricao | Risco Legal |
|--------|-----------|-------------|
| Shodan/Censys scan por ASN | Listar hosts de AS262462 | Baixo |
| Sublist3r em aranet.net.br | 30+ subdominios ja encontrados | Baixo |
| IXCSoft API (requer token) | Dados de clientes se comprometido | ALTO |
| Social Engineering telefone | Ligar como "cliente" | Medio |

---

## CATEGORIA 5: Brazilian OSINT Especifico

### 5.1 Plataformas e Repositorios

| Ferramenta | URL | Funcionalidade | Custo | Relevancia |
|------------|-----|----------------|-------|------------|
| **OSINT-Brazuca** | https://github.com/osintbrazuca/osint-brazuca | Repositorio de 1500+ links organizados | Gratuito | ALTA |
| **Caipora Pro** | https://caipora.pro/ | 1589 links, 44 categorias, CPF/CNPJ tools | Freemium | ALTA |
| **OSINT Brasil** | https://osintbrasil.app.br/ | Tecnicas e recursos OSINT Brasil | Gratuito | MEDIA |
| **OSINT-Tools-Brazil** | https://github.com/bgmello/OSINT-Tools-Brazil | Lista curada de recursos | Gratuito | MEDIA |
| **Investiga OSINT** | https://investigaosint.com.br/ | Ferramentas e tutoriais | Gratuito | MEDIA |

### 5.2 Consultas CPF/CNPJ

| Recurso | Funcionalidade | Acesso |
|---------|----------------|--------|
| **Receita Federal CNPJ** | Consulta publica de empresas | Gratuito |
| **QSA (Quadro Socios)** | Vinculo CPF-CNPJ | Gratuito |
| **DadosJusBr** | Salarios de orgaos do Judiciario 2018-2025 | Gratuito |
| **Cadastro MEI** | Lookup por CPF + DOB | Gratuito |
| **Selenium CPF Bots** | Scripts automatizados OSINT-Brazuca | OSS |

### 5.3 Telefonia Brasil

| Ferramenta | URL | Funcionalidade | Custo | Relevancia |
|------------|-----|----------------|-------|------------|
| **PhoneInfoga** | https://github.com/sundowndev/phoneinfoga | Carrier, geolocalizacao, social links | Gratuito (OSS) | ALTA |
| **NumVerify** | https://numverify.com/ | API de validacao + carrier | Freemium | MEDIA |
| **Truecaller** | https://www.truecaller.com/ | Reverse lookup (adiciona ao dataset) | Freemium | MEDIA |
| **FreeCarrierLookup** | https://freecarrierlookup.com/ | Landline vs wireless | Gratuito | BAIXA |

### 5.4 Username Enumeration

| Ferramenta | URL | Funcionalidade | Custo | Relevancia |
|------------|-----|----------------|-------|------------|
| **Maigret** | https://github.com/soxoj/maigret | 3000+ sites, reports PDF/HTML com fotos | Gratuito (Python) | ALTA |
| **Sherlock** | https://github.com/sherlock-project/sherlock | 400+ sites, output CSV/XLSX | Gratuito (Python) | ALTA |
| **Blackbird** | https://github.com/p1ngul1n0/blackbird | Busca rapida por username/email | Gratuito (Python) | MEDIA |
| **WhatsMyName** | https://whatsmyname.app/ | Web-based username check | Gratuito | MEDIA |

---

## CATEGORIA BONUS: Frameworks OSINT Completos

| Ferramenta | URL | Funcionalidade | Custo | Relevancia |
|------------|-----|----------------|-------|------------|
| **SpiderFoot** | https://github.com/smicallef/spiderfoot | 200+ modulos, automacao OSINT, web UI | Gratuito (OSS) | ALTA |
| **Maltego CE** | https://www.maltego.com/ | Visualizacao de links, transforms | Gratuito (Community) | ALTA |
| **Recon-ng** | https://github.com/lanmaster53/recon-ng | Framework modular CLI | Gratuito (OSS) | MEDIA |
| **theHarvester** | https://github.com/laramies/theHarvester | Emails, subdomains, portas | Gratuito (OSS) | MEDIA |
| **Lampyre** | https://lampyre.io/ | Similar ao Maltego, 100+ fontes | Pago (~) | MEDIA |

---

## Recomendacoes Especificas para IR-KALINE

### PRIORIDADE ALTA (Executar Imediatamente)

1. **Canary Token via WhatsApp**
   - Alvo confirmado com telefone 63992237479
   - Criar link Grabify/CanaryToken
   - Enviar via mensagem social engineered

2. **Stealer Logs Search**
   - Buscar email/telefone da vitima em:
     - Have I Been Pwned
     - DeHashed/Snusbase (se budget disponivel)
     - Telegram channels (Moon Cloud, Daisy Cloud)
   - IPs de login podem estar nos logs

3. **BGP Mapping Aranet**
   - Enumerar range de IPs de AS262462
   - Cross-reference com Shodan para identificar CPEs residenciais

4. **Vazamento SUS 2024**
   - Verificar se CPF 09126926180 esta no leak
   - Dados podem incluir endereco atualizado + telefone

### PRIORIDADE MEDIA

5. **Username Enumeration**
   - Rodar Maigret em "kaline.chaves", "kalinechaves", variantes
   - Perfis adicionais podem ter IP leaks

6. **Email Header Analysis**
   - Se conseguir email enviado pela vitima, extrair IP de origem

7. **Device Fingerprint Canary**
   - Criar pagina com ThumbmarkJS + webhook
   - Capturar fingerprint completo alem do IP

### PRIORIDADE BAIXA (Background)

8. **Monitoramento Continuo**
   - Configurar alertas em Mozilla Monitor para email da vitima
   - Monitorar novos breaches brasileiros

---

## Riscos e Consideracoes Legais

| Acao | Risco Legal | Mitigacao |
|------|-------------|-----------|
| Uso de CanaryTokens | Baixo (reconhecimento) | Nao usar para coercao |
| Consulta breach DBs | Baixo | Uso para investigacao legitima |
| Exploracao TR-069 | ALTO (Art. 154-A) | Apenas reconhecimento passivo |
| Acesso a IXCSoft API | ALTO (invasao) | NAO EXECUTAR sem autorizacao |
| Social Engineering | Medio | Depende da jurisdicao |

---

## Fontes da Pesquisa

### IP Discovery
- https://alternativeto.net/software/shodan/
- https://cybersecuritynews.com/cyber-security-search-engines/
- https://www.securityvision.ru/en/blog/sravnitelnyy-obzor-shodan-zoomeye-netlas-censys-fofa-i-criminal-ip-chast-1/

### Breach Databases
- https://dehashed.com/
- https://alternativeto.net/software/dehashed/
- https://socradar.io/top-stealer-log-telegram-channels/
- https://www.infostealers.com/article/alien-txtbase-data-leak-a-deep-analysis-of-the-breach/

### Canary/IP Grabbers
- https://grabify.link/
- https://iplogger.org/
- https://canarytokens.org/
- https://github.com/thinkst/canarytokens

### Brazilian OSINT
- https://github.com/osintbrazuca/osint-brazuca
- https://caipora.pro/
- https://databreach.com/breach/sus-brazil-2024
- https://www.lexology.com/library/detail.aspx?g=f8cba4de-b585-4716-8684-9cb7cdf71024

### BGP/ISP Tools
- https://bgp.tools/
- https://bgp.he.net/
- https://www.qacafe.com/resources/home-router-attack-tr-069-vulnerability/

### Device Fingerprinting
- https://www.ipqualityscore.com/device-fingerprinting
- https://github.com/thumbmarkjs/thumbmarkjs
- https://amiunique.org/

### Username OSINT
- https://github.com/soxoj/maigret
- https://github.com/sherlock-project/sherlock
- https://epieos.com/

---

**AUTOR:** Neural OffSec IR Team - Web Research Analyst
**CLASSIFICACAO:** CONFIDENCIAL - INVESTIGACAO
**TOTAL DE FERRAMENTAS:** 100+
**PROXIMA ACAO:** Implementar Canary Token Strategy
