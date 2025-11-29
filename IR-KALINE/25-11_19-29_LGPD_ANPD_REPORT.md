# RELATORIO PARA ANPD - INCIDENTE DE SEGURANCA
## Lei Geral de Protecao de Dados (Lei 13.709/2018)
## Case: IR-KALINE-2024-001

---

## 1. IDENTIFICACAO DO COMUNICANTE

| Campo | Valor |
|-------|-------|
| **Organizacao** | [NOME DA ORGANIZACAO] |
| **CNPJ** | [CNPJ] |
| **Responsavel** | [NOME DO DPO/RESPONSAVEL] |
| **Email** | [EMAIL] |
| **Telefone** | [TELEFONE] |
| **Endereco** | [ENDERECO] |

---

## 2. DESCRICAO DO INCIDENTE

### 2.1 Resumo
Foi detectado, via monitoramento ativo de ameacas, um documento contendo dados pessoais de cidada brasileira oriundo de servico ilegal de consulta de dados ("Consulta BOT") que opera via Telegram.

### 2.2 Data de Deteccao
**25 de novembro de 2024, 19:26 (UTC-3)**

### 2.3 Natureza do Incidente
- [x] Vazamento de dados
- [x] Acesso nao autorizado
- [ ] Alteracao de dados
- [ ] Destruicao de dados
- [x] Compartilhamento indevido

### 2.4 Fonte Identificada
| Campo | Valor |
|-------|-------|
| **Nome do Servico** | Consulta [BOT] |
| **Plataforma** | Telegram |
| **Tipo** | Bot/Painel de dados ilegais |
| **Status** | ATIVO |

---

## 3. DADOS PESSOAIS AFETADOS

### 3.1 Categorias de Dados Expostos
| Categoria | Dados | Status |
|-----------|-------|--------|
| Identificacao | Nome completo | EXPOSTO |
| Identificacao | CPF | EXPOSTO |
| Identificacao | Data de nascimento | EXPOSTO |
| Identificacao | Sexo | EXPOSTO |
| Contato | Telefone | NAO ENCONTRADO |
| Contato | Email | NAO ENCONTRADO |
| Contato | Endereco | NAO ENCONTRADO |
| Financeiro | Score de credito | NAO ENCONTRADO |
| Credenciais | Senhas | NAO ENCONTRADO |

### 3.2 Titulares Afetados
| Campo | Valor |
|-------|-------|
| **Quantidade** | 1 (uma) pessoa |
| **Perfil** | Pessoa fisica, 22 anos |
| **Localizacao** | Brasil |

### 3.3 Dados do Titular
```
NOME: KALINE CHAVES PEREIRA
CPF: 09126926180
NASCIMENTO: 18/09/2002
SEXO: Feminino
```

---

## 4. ORIGEM PROVAVEL DO VAZAMENTO

### 4.1 Analise de Threat Intelligence
Com base em investigacao OSINT, identificamos que o servico "Consulta BOT" compila dados de multiplos vazamentos brasileiros, incluindo potencialmente:

1. **Mega Breach Brasil 2021**
   - 223 milhoes de pessoas afetadas
   - Descoberto em 20/01/2021 pela PSafe
   - Dados: CPF, nome, endereco, foto, score, salario

2. **Vazamentos de bases governamentais**
   - TSE (fotos eleitorais)
   - INSS
   - RAIS
   - Detran (veiculos)

3. **Vazamentos corporativos**
   - Suspeita de origem: Serasa Experian (nao confirmado)
   - Diversas empresas brasileiras

### 4.2 Modus Operandi do Servico Criminoso
```
Vazamentos originais -> Dark Web -> Compiladores -> Bots Telegram -> Usuarios finais (criminosos)
```

---

## 5. MEDIDAS ADOTADAS

### 5.1 Imediatas
- [x] Deteccao e analise do incidente
- [x] Documentacao forense (hash SHA256)
- [x] Avaliacao de impacto ao titular
- [x] Pesquisa de threat intelligence
- [ ] Notificacao ao titular afetado

### 5.2 Planejadas
- [ ] Monitoramento continuo do servico criminoso
- [ ] Denuncia a plataforma Telegram
- [ ] Articulacao com autoridades competentes
- [ ] Auxilio ao titular para mitigacao de riscos

---

## 6. AVALIACAO DE RISCO AOS TITULARES

### 6.1 Riscos Identificados
| Risco | Probabilidade | Impacto | Justificativa |
|-------|---------------|---------|---------------|
| Fraude de identidade | Alta | Critico | CPF exposto permite abertura de contas/emprestimos |
| Phishing direcionado | Media | Alto | Nome + CPF + idade facilitam engenharia social |
| Assedio/Stalking | Baixa | Medio | Dados basicos sem endereco/telefone |

### 6.2 Fatores Atenuantes
- Ausencia de dados de contato (telefone, email, endereco)
- Ausencia de credenciais (senhas)
- Ausencia de dados financeiros detalhados
- Perfil jovem com provavel menor exposicao financeira

---

## 7. RECOMENDACOES AO TITULAR

Conforme Art. 48 da LGPD, recomendamos ao titular:

1. **Monitoramento de CPF**
   - Consultar regularmente: Serasa, SPC Brasil, Boa Vista
   - Ativar alertas de movimentacao

2. **Registrato do Banco Central**
   - Acessar: https://registrato.bcb.gov.br
   - Verificar contas e emprestimos em seu nome

3. **Registro de Boletim de Ocorrencia**
   - Delegacia de Crimes Ciberneticos
   - Preservar numero do B.O. para contestacoes

4. **Comunicacao a Instituicoes Financeiras**
   - Informar bancos sobre possivel uso indevido de dados
   - Solicitar camadas extras de verificacao

5. **Verificacao de Vazamentos Anteriores**
   - Have I Been Pwned: https://haveibeenpwned.com
   - Dehashed: https://dehashed.com

---

## 8. EVIDENCIAS ANEXAS

### 8.1 Artefato Principal
| Campo | Valor |
|-------|-------|
| Arquivo | relatorio.pdf |
| Hash SHA256 | 101539157caf03acc709baee0f8e60f4d994f623173b99fc3bff7f747681c8b3 |
| Timestamp | 25/11/2024 19:25:47 |

### 8.2 Documentacao Complementar
- Relatorio de Incident Response completo
- Cadeia de custodia do artefato
- Screenshots do servico (se disponiveis)

---

## 9. FUNDAMENTACAO LEGAL

### 9.1 Dispositivos Aplicaveis
- **Art. 48 LGPD** - Comunicacao de incidente de seguranca
- **Art. 52 LGPD** - Sancoes administrativas
- **Art. 154-A CP** - Invasao de dispositivo informatico
- **Art. 307 CP** - Falsa identidade
- **Art. 171 CP** - Estelionato

### 9.2 Competencia
- **ANPD** - Fiscalizacao e sancoes LGPD
- **Policia Civil** - Investigacao criminal
- **Ministerio Publico** - Acao civil/criminal

---

## 10. DECLARACAO

Declaro que as informacoes prestadas neste documento sao verdadeiras e que a organizacao esta comprometida com a protecao dos dados pessoais conforme a LGPD.

**Local e Data:** [CIDADE], 25 de novembro de 2024

**Assinatura:** _______________________________

**Nome:** [NOME DO DPO/RESPONSAVEL]

**Cargo:** [CARGO]

---

**CLASSIFICACAO:** CONFIDENCIAL
**PROTOCOLO ANPD:** [A PREENCHER APOS ENVIO]
