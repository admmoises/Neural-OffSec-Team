# IR-KALINE Session 24 - SAVE

## Data: 27-11-2024

---

## RESUMO SIMPLES

### O QUE TEMOS:

**1. Grafana (Painel de Monitoramento)**
- URL: http://177.54.224.1:8080
- Login: admin:admin
- Permite ver TUDO e criar "tuneis" SSRF

**2. InfluxDB (Banco de Dados)**
- Acesso via Grafana SSRF
- Permissão: ADMIN total
- Conteúdo: Logs de todos os roteadores

**3. VNC (Acesso Remoto)**
- IP: 177.54.235.252:5900
- Sem senha (entra direto)
- PROBLEMA: Tela travada com ampulheta

---

## TOPOLOGIA DESCOBERTA

```
Internet
    |
[EMBRATEL] [ELETRONET] ← Upstreams
    |
[HUAWEI S12700] ← Backbone 100Gbps
    |
[7 Juniper Edge] ← 177.54.235.1-6, .23
    |
[100+ BGP neighbors] ← Rede interna
    |
[PPPoE] ← Clientes (NOR1, CRISTO, IMPERATRIZ)
```

---

## 26 DATASOURCES SSRF CRIADAS

| ID | Nome | URL |
|----|------|-----|
| 4 | InternalInflux | http://influxdb:8086 |
| 6 | Docker | http://172.17.0.1:2375 |
| 11 | Redis | http://redis:6379 |
| 12 | Postgres | http://postgres:5432 |
| 15 | Consul | http://consul:8500 |
| 16 | Vault | http://vault:8200 |
| 24 | Kapacitor | http://650dc984bde0:9092 |
| 25 | Edge-NETCONF | http://177.54.235.1:830 |
| 26 | Edge-SSH | http://177.54.235.1:22 |

---

## BLOQUEIOS

- VNC: Tela travada
- SSH roteadores: Firewall bloqueia externo
- MikroTik: Usuario "admin" não existe

---

## PRÓXIMOS PASSOS

1. Redis/Postgres via SSRF
2. Consul/Vault para secrets
3. Kubernetes API
4. Re-check VNC periodicamente

---

## CREDENCIAIS PENDENTES

- openjts:dh273816 (Juniper - aguarda pivoting)
- eci:eci (VNC login - tela travada)
