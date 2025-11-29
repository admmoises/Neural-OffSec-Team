# IR-KALINE - Session 6 Aranet Recon
## Data: 25/11/2024 23:55 BRT
## Alvo: ixc.aranet.net.br
## Status: RECONHECIMENTO COMPLETO

---

## ALVO

- IP: 177.54.235.226
- Framework: IXCSoft Provedor ERP
- Versão: 5_5_vangogh
- Server: nginx

## SUBDOMÍNIOS CRÍTICOS

- ixc.aranet.net.br - Painel IXCSoft
- gerenet.aranet.net.br - Gerenciamento rede
- comercial.aranet.net.br - Portal comercial
- integra.aranet.net.br - Integrações
- 30 subdomínios total

## API

- Endpoint: /webservice/v1/
- Auth: Token-based (Basic Auth)
- Status: 401 (requer credenciais)

## SEGURANÇA

- Headers: X-Frame-Options, X-XSS-Protection OK
- Faltando: CSP, HSTS
- CVEs: Nenhum específico encontrado
- SSL: Válido até 09/2026

## CONTATO ARANET

- Tel: (63) 3411-4000
- Email: contato@aranet.net.br
- Endereço: RUA P, 500, Araguaína-TO

## CONCLUSÃO

Superfície mapeada, sem vulns críticas.
Acesso à API requer credenciais válidas.
Recomendação: Usar Canary Token para captura direta.
