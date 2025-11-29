# CHAIN OF CUSTODY - CADEIA DE CUSTODIA
## Case: IR-KALINE-2024-001

---

## IDENTIFICACAO DO ARTEFATO

| Campo | Valor |
|-------|-------|
| **Arquivo** | relatorio.pdf |
| **Localizacao Original** | /Users/th3_w6rst/Downloads/relatorio.pdf |
| **Tipo** | PDF Document |
| **Tamanho** | 1.4MB |
| **Hash SHA256** | 101539157caf03acc709baee0f8e60f4d994f623173b99fc3bff7f747681c8b3 |
| **Descricao** | Output do servico "Consulta [BOT]" contendo dados pessoais vazados |

---

## REGISTRO DE CUSTODIA

| # | Data/Hora | Acao | Responsavel | Notas |
|---|-----------|------|-------------|-------|
| 1 | 25/11/2024 19:26 | Recepcao via monitoramento ativo | IR Team | Artefato detectado em operacao de threat intel |
| 2 | 25/11/2024 19:29 | Analise inicial e extracao de IOCs | IR Team | Identificados dados de 1 vitima |
| 3 | 25/11/2024 19:29 | Calculo de hash SHA256 | IR Team | Integridade preservada |
| 4 | 25/11/2024 19:29 | Copia para repositorio IR | IR Team | IR-KALINE/ |

---

## INTEGRIDADE DO ARTEFATO

### Verificacao de Hash
```bash
# Comando utilizado
shasum -a 256 /Users/th3_w6rst/Downloads/relatorio.pdf

# Resultado
101539157caf03acc709baee0f8e60f4d994f623173b99fc3bff7f747681c8b3  relatorio.pdf
```

### Status de Integridade
- [x] Artefato original preservado
- [x] Hash calculado e registrado
- [x] Copia de trabalho criada
- [ ] Backup em armazenamento seguro

---

## DADOS EXTRAIDOS DO ARTEFATO

### Informacoes da Vitima
```
NOME: KALINE CHAVES PEREIRA
CPF: 09126926180
SEXO: F
NASCIMENTO: 18/09/2002
```

### Fonte do Vazamento
```
SERVICO: Consulta [BOT]
TIPO: Bot/Painel de dados Telegram
COPYRIGHT: 2024 Consulta [BOT]
```

### Campos Consultados (Sem Resultados)
- Parentes, Conjuge
- Certidao de Nascimento
- CNS, CNH, RG
- Gestao Cadastral, TSE, Documento
- NIS, PIS
- Poder aquisitivo
- Historico de Telefone, Ultimo Telefone
- Emails, Endereco
- Covid
- Empresas Associadas (SOCIO), CNPJ MEI
- Dividas Ativas (SIDA)
- Auxilio Emergencial
- RAIS - Historico de Emprego
- INSS
- Senhas Vazadas no Email
- Senhas Vazadas do CPF

---

## PRESERVACAO DE EVIDENCIAS

### Copia Digital
```
Localizacao: /Users/th3_w6rst/Neural-OffSec-Team/IR-KALINE/
Hash verificado: [SIM/NAO]
```

### Metadados PDF
```
Ferramenta de extracao: [A EXECUTAR]
Data criacao PDF: [A EXTRAIR]
Software gerador: [A EXTRAIR]
```

---

## DECLARACAO DE AUTENTICIDADE

Eu, membro da equipe de Incident Response, declaro que:

1. Este artefato foi obtido via monitoramento legitimo de ameacas
2. A integridade foi preservada desde a aquisicao
3. O hash criptografico foi calculado imediatamente apos recepcao
4. Nenhuma modificacao foi feita no artefato original

**Data:** 25/11/2024
**Responsavel:** IR Team - Neural OffSec

---

## ANEXOS

- [ ] Screenshot do artefato
- [ ] Log de aquisicao
- [ ] Certificado de timestamp (se aplicavel)

---

**CLASSIFICACAO:** CONFIDENCIAL - EVIDENCIA FORENSE
**RETENCAO:** Conforme politica de retencao de incidentes
