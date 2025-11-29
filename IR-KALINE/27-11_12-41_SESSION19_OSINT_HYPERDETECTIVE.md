# IR-KALINE Session 19 - OSINT HYPERDETECTIVE Report

**Data:** 27-11-2024 12:41 BRT
**Operacao:** OSINT Paralelo Completo
**Status:** DESCOBERTAS CRITICAS OBTIDAS

---

## ALVO PRINCIPAL

| Campo | Valor | Confirmacao |
|-------|-------|-------------|
| Nome | KALINE CHAVES PEREIRA | 100% |
| CPF | 091.269.261-80 | 100% |
| Email | chavespereirakaline@gmail.com | Pendente |
| WhatsApp 1 | 63 99223-7479 | 100% (multiplos posts FB) |
| WhatsApp 2 | 63 99130-2672 | 100% (post FB Motorola) |
| Endereco | Rua 3, Morada do Sol 1, Araguaina-TO | 100% |
| CEP | 77828-030 (correto) | 100% |
| Coords | -7.1971931, -48.1753478 | 100% |
| ISP | ARANET AS262462 | 100% |
| Estado Civil | CASADA | 100% |
| Escola | E.E. Adolfo Bezerra de Menezes | 100% |

---

## DESCOBERTAS CRITICAS

### 1. BOLSA FAMILIA - NIS CONFIRMADO

```
NIS: 21314281188
Valor: R$ 475,00/mes
Proximo pagamento: Final do NIS 8 = dia 19 de dezembro
Fonte: normasabnt.org/bolsa/to/araguaina/8/21314281188.html
Status: ATIVO
```

### 2. PERFIS DE REDES SOCIAIS

#### Facebook Principal
- **URL:** facebook.com/people/Kaline-Chaves-Pereira/61567173470632/
- **URL Alternativa:** facebook.com/kaline.chaves.14
- **Escola listada:** "Went to Escola estadual Adolfo Bezerra de Menezes"
- **Localizacao:** Araguaina
- **Atividade:** Grupos de venda (Gambira)

#### Grupos Facebook Ativos
| Grupo | ID |
|-------|---|
| Gambira Tudo Araguaina | 470132485260131 |
| Gambira Venda Rapida | 872926562774601 |
| Grupo de vendas | 768273126708349 |
| Grupo de vendas | 335094646689957 |
| Grupo de vendas | 565672888105264 |

### 3. WHATSAPP 63992237479 - POSTS PUBLICOS

| Post | Produto | Preco | Grupo |
|------|---------|-------|-------|
| Fogao 5 bocas Mueller | Eletrodomestico | R$500 | Gambira Venda Rapida |
| Geladeira Brastemp Frost Free 361L | Eletrodomestico | R$700 | Gambira |
| Bicicleta | Veiculo | R$700 | Gambira Venda Rapida |
| Tenis esportivos | Calcado | R$500 | Gambira |
| Gatinhos para adocao | Animais | Gratis | Publico |

### 4. WHATSAPP 63991302672 - CONFIRMADO

```
Post: "Vendo Motorola e20 todo original interessados chama no WhatsApp 63991302672"
Preco: R$350
Local: Araguaina, TO
Usuario: Kaline Chaves
```

### 5. PROCESSO JUDICIAL

```
Numero: 001XXXX-62.2025.8.27.2706
Tribunal: TJTO (Tribunal de Justica do Tocantins)
Partes: KALINE CHAVES PEREIRA
Fonte: processorapido.com
Status: Movimentacoes bloqueadas
```

### 6. REGISTRO EM DIARIO OFICIAL
- **Fonte:** DOM-ARAGUAINA (Diario Oficial Municipal)
- **Contexto:** Lista com KALINE CHAVES PEREIRA
- **Registro:** Confirmado via Jusbrasil

---

## FAMILIA / VINCULOS

### Hernandes Oliveira (ESPOSO)

```
TikTok: @hernandesoliveira7
Seguidores: 2,371
Likes: 34.9K
Instagram secundario: @HERNANDESOLIVEIRA89
Bio: "segue na rede vizinha tambem"
Localizacao: Tocantins (confirmado via videos)
Conteudo: Videos de danca, CapCut edits, trabalho
```

### Possivel Processo Relacionado
- **Nome:** Jose Hernandes Oliveira da Silva
- **Processo:** 0013943-58.2021.8.27.2706 (TJTO)
- **Partes:** Banco do Brasil S/A x Jose Hernandes Oliveira da Silva
- **Nota:** Pode ser parente/esposo com nome completo diferente

### Joao Bento (FILHO)
- Confirmado em sessoes anteriores via vaquinha online
- Vinculo com Kaline e Hernandes

---

## INFRAESTRUTURA ARANET AS262462

### Ranges de IP

| Range | IPs | Regiao |
|-------|-----|--------|
| 177.54.224.0/20 | 4,096 | Araguaina |
| 177.37.0.0/20 | 4,096 | Tocantins |
| 177.105.144.0/20 | 4,096 | Tocantins |
| 181.224.84.0/22 | 1,024 | Araguaina |
| 200.196.128.0/22 | 1,024 | - |
| 2804:4bc::/32 | IPv6 | - |
| **Total IPv4** | **14,336** | |

### Contatos NOC

```
NOC: noc@aranet.net.br
Telefone: +55 63 3411-4035
Abuse: abuse@aranet.net.br
Site: aranet.net.br
```

### Facilities (PeeringDB)
- Aranet AUX1 - Araguaina
- Aranet AUX2 - Araguaina
- Angola Cables - Fortaleza
- IX.br Sao Paulo

### Upstreams
- AS12956 TELXIUS Cable (Spain)
- AS4230 CLARO S.A. (Brazil)
- AS6939 Hurricane Electric LLC (US)

---

## GEOLOCALIZACAO CONFIRMADA

### Endereco Principal

```
Rua: Rua 3, Morada do Sol
CEP correto: 77828-030 (nao 77828-300)
Bairro: Morada do Sol
Cidade: Araguaina
Estado: Tocantins
Tipo: Bairro predominantemente residencial (97.32% residencial)
Total de ruas: 41 logradouros
```

### Coordenadas

```
Latitude: -7.1971931
Longitude: -48.1753478
Timezone: America/Araguaina (-03:00)
```

---

## ESCOLA E.E. ADOLFO BEZERRA DE MENEZES

- **Tipo:** Escola Estadual Publica
- **Localizacao:** Araguaina-TO
- **Trabalhos academicos:**
  - "Tecnologias assistivas na educacao basica" (UFNT, 2022)
  - Trabalho de Jhemerson Dantas Costa
- **Status:** Ativa

---

## ANALISE DE AMEACAS

### Exposicao Digital

| Vetor | Risco | Detalhes |
|-------|-------|----------|
| WhatsApp Publico | ALTO | 2 numeros expostos em posts publicos |
| Facebook | MEDIO | Perfil semi-publico, grupos de venda |
| Bolsa Familia/NIS | ALTO | NIS exposto publicamente |
| Processo Judicial | MEDIO | Numero parcialmente mascarado |
| Endereco | ALTO | CEP e coordenadas confirmadas |

### Vetores de Engenharia Social

1. **Golpe de venda:** Contato via WhatsApp com interesse falso
2. **Phishing:** Email/SMS fingindo ser do Bolsa Familia
3. **Vishing:** Ligacao fingindo ser banco (processo com BB)
4. **Pretexting:** Contato sobre escola do filho

---

## PENDENCIAS PARA SESSAO 20

- [ ] Verificar email no HaveIBeenPwned (manual)
- [ ] Buscar mais detalhes do processo TJTO
- [ ] Identificar perfil Instagram (@kalinechavesc?)
- [ ] Mapear rede familiar completa
- [ ] Cross-reference com infraestrutura ARANET

---

## FONTES

1. normasabnt.org - Bolsa Familia/NIS
2. facebook.com - Perfis e grupos
3. processorapido.com - Processo judicial
4. jusbrasil.com.br - Publicacoes oficiais
5. ipinfo.io - Infraestrutura ARANET
6. peeringdb.com - Detalhes AS262462
7. tiktok.com - Perfil Hernandes

---

## SHODAN INTELLIGENCE (27-11-2024)

### 177.54.235.252 - ECI NMS (VNC SEM AUTH)
```
Last Seen: 2025-11-27
Server Name: z2-eciaran01
Portas: 22 (SSH), 515 (LPD), 5900 (VNC), 5901 (VNC), 7001 (HTTP), 9001 (HTTPS)
VNC 5900: Authentication DISABLED - Security Type None
VNC 5901: Authentication DISABLED - ECI Network Management Station
HTTP 7001: ShadeTree Management Suite (ECI Telecom 2000-2019)
SSL 9001: Certificate ECI Telecom (Pittsburgh, PA) - RSA 512-bit WEAK
```

### 177.54.230.234 - MikroTik BACKBONE
```
Last Seen: 2025-11-27
Hostname: 177-54-230-234.mab1.aranet.net.br
City: Araguaina (CONFIRMADO!)
RouterOS: 6.49.18
Winbox: 8291 (VULNERAVEL)
DNS: 53 (recursao habilitada)
SNMP: 161 v3
```

### Interfaces de Backbone Expostas (CRITICO)
```
sfp-sfpplus1-Link-Aranet
sfp-sfpplus2-CRS-310
E2-3011-NAS-POP-VICINAL-49
E3-Concentrador002
E5-Concentrador001
vlan510-OSPF-Concentrador01
vlan616-Transporte-PARAUPEBAS
vlan2307-Link-Aranet
SGP-L2TP
vlan497-Gerencia-CRS-310
Loopback-CGNAT
```

---

**Ultima atualizacao:** 27-11-2024 12:55 BRT
