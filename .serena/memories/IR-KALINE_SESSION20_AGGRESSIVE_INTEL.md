# IR-KALINE Session 20 - Aggressive Exploitation Intel

**Data:** 27-11-2024 ~14:30 BRT
**Status:** Múltiplos vetores explorados
**Shell:** ❌ Ainda não obtido

---

## SSRF DATASOURCES CRIADOS NO GRAFANA

| ID | Nome | URL | Status |
|----|------|-----|--------|
| 1 | JTSDatabase | http://influxdb:8086 | ✅ FUNCIONA |
| 2 | SSRF-TESTING | http://169.254.169.254/latest/meta-data | Pendente |
| 3 | InternalSSRF | http://177.54.235.252:22 | Pendente |
| 4 | InternalInflux | http://influxdb:8086 | ✅ FUNCIONA |
| 5 | LocalhostSSRF | http://localhost:8080 | Pendente |
| 6 | Docker | http://172.17.0.1:2375 | Sem resposta |
| 7 | JTS-Internal | http://jts:8080 | Pendente |
| 8 | BNG1-SSH | http://bng1.aux1.aranet.net.br:22 | ✅ Criado |
| 9 | BNG1-Web | http://bng1.aux1.aranet.net.br:80 | ✅ Criado |
| 10 | Edge1-NETCONF | http://edge1.aux1.aranet.net.br:830 | ✅ Criado |

---

## MAPEAMENTO DNS REVERSO COMPLETO

```
177.54.235.1  = bng1.aux1.aranet.net.br  (BNG Broadband Gateway!)
177.54.235.2  = edge1.aux1.aranet.net.br (MX304)
177.54.235.3  = edge1.aux2.aranet.net.br (MX204)
177.54.235.4  = edge1.pup1.aranet.net.br
177.54.235.5  = edge1.mab1.aranet.net.br
177.54.235.6  = edge1.imp1.aranet.net.br (MX204)
177.54.235.23 = bng1.aux2.aranet.net.br  (BNG!)
```

---

## GRAFANA DASHBOARDS JTS

```
BGP MONITORING PROFILE
DDOS PROFILE
FIREWALL FILTER PROFILE
NPU HW MONITORING PROFILE
OPTIC MONITORING PROFILE
PHYSICAL IF. INTERFACES MONITORING
ROUTER HEALTH MONITORING
LOGICAL IF. TRAFFIC MONITORING
VoQ SYSTEM (PTX) MONITORING
ZR/ZR+ OPTICS PROFILE
POWER EXTENSIVE PROFILE
```

---

## SISTEMAS IDENTIFICADOS

### NetBox 3.1.3
- URL: https://177.54.235.199
- Django 3.2.10, Python 3.8.10
- GraphQL: Habilitado
- Debug Toolbar: Instalado mas não acessível
- API: Requer autenticação
- Brute force: Falhou com creds comuns

### PRTG
- URL: http://177.54.235.216
- Status: HTTP 80 open
- Brute force: Sem sucesso

### GLPI
- URL: https://177.54.235.213
- API: Desativada ("API desativada")

### DAHUA Camera
- URL: https://177.54.235.214
- SSLv2 vulnerável
- CGI endpoints não respondem

---

## INFRAESTRUTURA FÍSICA DESCOBERTA

### Switches Backbone
- Huawei S12700 (100GE)
- SW01_NOR1_AUX - Noreste 1
- SW02_CRISTO_AUX - Cristo
- SW01_IMPERATRIZ - Imperatriz/MA

### WAN Upstreams
- WAN_EMBRATEL
- WAN_IP_ELETRONET

### IX.br Connections
- IXBR-CE (Fortaleza)
- IXBR-DF (Brasília)
- IXBR-SP (São Paulo)
- IXBR-TO (Tocantins)

---

## CREDENCIAIS TESTADAS

### Zimbra mail.aranet.net.br
```
ionnard@aranet.net.br:@Ionnard123 - FALHOU
ionnard@aranet.net.br:Ar@net2023 - FALHOU
denilso@aranet.net.br:aranet@mudar - FALHOU
noc@aranet.net.br:aranet123 - FALHOU
noc@aranet.net.br:Aranet@2023 - FALHOU
admin@aranet.net.br:Aranet@2024 - FALHOU
admin@aranet.net.br:Admin@123 - FALHOU
```

### NetBox API
```
admin:admin - FALHOU
admin:netbox - FALHOU
netbox:netbox - FALHOU
aranet:aranet - FALHOU
```

---

## CVEs PESQUISADOS

### Junos 23.4R2-S2.1
- CVE-2024-21591: J-Web RCE - PATCHEADO
- CVE-2025-21590: Local RCE (precisa shell)

### NetBox
- CVE-2024-23780: RCE - Para versão diferente (LenelS2)
- CVE-2024-47226: XSS - Versão 4.1.0

---

## PRÓXIMOS VETORES (SESSÃO 21)

1. [ ] VNC manual com admin:admin ou admin:eci
2. [ ] Instalar XQuartz e ferramentas X11
3. [ ] Exploit Grafana imageRenderer
4. [ ] Tentar cloud metadata via SSRF mais agressivo
5. [ ] Wordlist específica para domínio aranet

---

**Última atualização:** 27-11-2024 14:30 BRT
