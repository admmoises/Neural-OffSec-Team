# IR-KALINE Session 17 - Critical Access Checkpoint
**Data:** 26-11-2025 04:54 (GMT-3)

## DESCOBERTAS CRÍTICAS

### VNC SEM AUTENTICAÇÃO
- **IP:** 177.54.235.252
- **Status:** ACESSO DIRETO DISPONÍVEL
- **Portas:** 515, 5900, 5901, 9000, 9001, 7001, 22
- **Cidade:** São Paulo

### HOSTS VULNERÁVEIS
- 12 VNC hosts expostos na ARANET
- 150 MikroTik routers com Winbox (CVE-2025-10948)
- RouterOS 7.15.3 confirmado vulnerável

### ALVOS IDENTIFICADOS
- TP-LINK EX220V2 (177.54.238.248) - lockout triggered
- MikroTik 177.54.229.179 - RouterOS 7.15.3

### CVE CONFIRMADO
- CVE-2025-10948: Buffer Overflow em MikroTik RouterOS 7
- Endpoint: /rest/ip/address/print
- Fix: 7.20.1+ (target tem 7.15.3)

## PRÓXIMOS PASSOS
1. Conectar VNC 177.54.235.252 (NO-AUTH)
2. Explorar 150 MikroTik via CVE-2025-10948
3. Retry TP-LINK após lockout (586s)
