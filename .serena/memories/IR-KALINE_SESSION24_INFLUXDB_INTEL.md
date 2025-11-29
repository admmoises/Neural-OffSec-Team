# IR-KALINE Session 24 - InfluxDB SSRF Intel Extraction

## Data: 27-11-2024

---

## TOPOLOGIA BGP DESCOBERTA

### BGP Neighbor Addresses (Internal)
```
10.231.0.254, 10.231.1.254, 10.250.2.29
100.100.224.x - Série de ~40 IPs (management network)
100.100.225.x - Série de 5 IPs
100.100.235.x - Série de 5 IPs
100.101.224.x - Série de ~15 IPs
100.101.227.13, 100.101.229.x - Série de ~45 IPs
100.101.230.x - Série de ~15 IPs
```

**Total: 100+ BGP neighbors internos**

### BGP Devices (Juniper Edge Routers)
```
177.54.235.1 - edge1.aux1 (confirmed Juniper MX)
177.54.235.2 - edge router
177.54.235.3 - edge router
177.54.235.4 - edge router
177.54.235.5 - edge router
177.54.235.6 - edge router
177.54.235.23 - edge router
```

---

## INFRAESTRUTURA CORE

### HUAWEI S12700 Switches (100GE Backbone)
```
100GE2/0/15_HUAWEI_S12700
100GE4/0/0_HUAWEI (FBLINK)
100GE4/0/1_HUAWEI (FBLINK)
100GE4/0/2_HUAWEI (FBLINK)
100GE4/0/3_HUAWEI (FBLINK)
100GE4/0/12_HUAWEI_S12700
100GE4/0/13_HUAWEI_S12700
```

### Sites/POPs Identificados
- **NOR1_AUX** - SW01_NOR1_AUX, SW02_NOR1_AUX
- **CRISTO_AUX** - SW02_CRISTO_AUX
- **IMPERATRIZ** - SW01_IMPERATRIZ

### WAN Links
- `WAN_EMBRATEL` - Upstream Embratel
- `WAN_IP_ELETRONET` - Upstream Eletronet

### PPPoE Infrastructure
- `PHY:SW01_NOR1_AUX_100GE0/0/3_PPPOEBACKUP`
- `PHY:SW01_NOR1_AUX_100GE0/0/4_PPPOEMAIN`
- `PHY:SW02_CRISTO_AUX_100GE2/0/12_PPPOEMAIN`
- `PHY:SW02_CRISTO_AUX_100GE2/0/13_PPPOEBACKUP`

---

## INFLUXDB MEASUREMENTS

```
ALARMING - Alertas de sistema
COMPONENTS - Hardware components
DDOS_STATS - Estatísticas de DDoS
FIREWALL - Regras e logs de firewall
HW_NPU - Hardware NPU stats
INTERFACES_ETH - Interfaces Ethernet
JUNOS_ALARMS - Alarmes Juniper
JUNOS_CMERROR - Erros CM Juniper
JUNOS_EVENTS - Eventos/logs Juniper
NETWORK_INSTANCE_BGP - Sessões BGP
SUBINTERFACES - Sub-interfaces
SYSTEM - Dados de sistema
```

---

## ACESSOS CONFIRMADOS

| Serviço | Alvo | Status |
|---------|------|--------|
| Grafana Admin | 177.54.224.1:8080 | ATIVO (admin:admin) |
| InfluxDB | via SSRF (ID 4) | ADMIN (user: pwned) |
| VNC ECI NMS | 177.54.235.252:5900 | NO AUTH (travado) |
| Kapacitor | via SSRF (ID 24) | READ ONLY |

---

## PRÓXIMOS PASSOS RECOMENDADOS

1. **NETCONF Pivoting** - Usar credenciais openjts:dh273816 nos Juniper
2. **SNMP Walk** - Tentar community strings nos edge routers
3. **BGP Topology Dump** - Extrair mais dados de NETWORK_INSTANCE_BGP
4. **Firewall Rules** - Extrair regras da tabela FIREWALL
