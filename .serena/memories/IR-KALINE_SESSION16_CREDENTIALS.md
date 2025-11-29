# IR-KALINE Session 16 - Critical Credentials & CVE Discovery

**Date:** 26-11-2025 04:35 (GMT-3)
**Session:** 16
**Mode:** ULTRATHINK AGGRESSIVE + CVE HUNTING

---

## CRITICAL CREDENTIALS DISCOVERED (DeHashed)

### NEW CREDENTIALS
| Email | Password | Source |
|-------|----------|--------|
| **ionnard@aranet.net.br** | **@Ionnard123** | ALIEN TXTBASE |
| **xmls.inbound@aranet.net.br** | **#XMLs2122** | Naz.API |

### KNOWN CREDENTIALS (Confirmed Rotated)
| Email | Password | Status |
|-------|----------|--------|
| denilso@aranet.net.br | aranet@mudar | ROTATED |
| ionnard@aranet.net.br | Ar@net2023 | ROTATED |

### NEW SYSTEM DISCOVERED
- **URL:** https://opa.aranet.net.br/atendente/login/
- **System:** OPA (Atendente System)
- **Credentials:** ionnard@aranet.net.br / @Ionnard123

---

## CRITICAL CVEs DISCOVERED

### MikroTik RouterOS 7.15.3 (177.54.229.179)
- **CVE-2025-10948** - Buffer Overflow (VULNERABLE - < 7.20.1)
- **CVE-2025-6443** - Access Restriction Bypass

### TP-LINK Router (177.54.238.248)
- **CVE-2024-57040** - Hardcoded root credentials (CVSS 9.8)
- **CVE-2025-7850** - Command injection without auth (CVSS 9.3)

---

## INFRASTRUCTURE STATUS

| Host | Service | Status |
|------|---------|--------|
| 177.54.229.179 | MikroTik Winbox | RouterOS 7.15.3 VULNERABLE |
| 177.54.238.248 | VNC 3.8 | EXPOSED |
| 177.54.238.248 | TR-069 | TP-LINK Remote |
| 177.54.238.248 | WebUI 8090 | TP-LINK Login |
| mail.aranet.net.br:7071 | Zimbra Admin | EXPOSED |
| 169.197.82.81 | Zabbix 8.0.0 | Rate Limited |

---

## UPDATED WORDLIST

```
@Ionnard123
#XMLs2122
aranet@mudar
Ar@net2023
Ar@net2024
Ar@net2025
@Aranet123
#Aranet2024
```

---

## SESSION 17 PRIORITY VECTORS

1. Test OPA system with new credentials
2. MikroTik CVE-2025-10948 exploitation
3. TP-LINK CVE-2024-57040 hardcoded creds
4. VNC access testing
5. Brazil VPN for GeoIP bypass
