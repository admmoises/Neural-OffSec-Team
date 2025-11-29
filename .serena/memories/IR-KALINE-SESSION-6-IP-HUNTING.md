# IR-KALINE - Session 6 IP Hunting
## Data: 25/11/2024 23:15 BRT
## Status: IPs CANDIDATOS IDENTIFICADOS

---

## DESCOBERTA PRINCIPAL

**MIDIX FIBRA tem torre no bairro MORADA DO SOL** (endereco da vitima!)

### ISPs Provaveis
1. **MIDIX FIBRA** (60%) - Torre no bairro da vitima
2. **ARANET PLAY** (40%) - Maior cobertura em Araguaina

---

## IPs CANDIDATOS

### MIDIX (Alta Probabilidade)
- 131.221.228.91 (TP-LINK TR-069)
- 131.221.228.96 (TP-LINK TR-069)
- 131.221.228.18 (TP-LINK TR-069)

### ARANET (Media Probabilidade)
- 177.54.238.235 (TP-LINK TR-069)
- 177.54.238.89 (CWMP)
- 177.105.159.127 (CWMP)

---

## FERRAMENTAS UTILIZADAS

- Shodan API (EDU - 200K credits)
- MCP Security Toolkit (nmap_scan, metasploit_search)
- Tavily Search
- Nmap 7.98 (com sudo)

---

## LIMITACAO

IP exato NAO identificado porque:
1. CGNAT (NAT compartilhado)
2. iPhone nao expoe portas
3. Sem stealer logs encontrados

---

## PROXIMOS PASSOS

1. Canary Token (captura ativa)
2. DeHashed/Snusbase ($15-29)
3. Requisicao judicial ao ISP

---

## DOCUMENTOS GERADOS

- `/IR-KALINE/25-11_23-10_IP_HUNTING_FINAL_ULTRATHINK.md`
- `/IR-KALINE/canary/README.md`
- `/IR-KALINE/canary/fingerprint.html`
- `/IR-KALINE/canary/ip_candidates.md`

---

**CRITICIDADE:** 9/10
