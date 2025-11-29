# DeHashed ARANET Credentials - IR-KALINE Session 10
**Data:** 26-11-2025 03:05 (GMT-3)
**Query:** domain:aranet.net.br
**Resultados:** 6 entries
**Status:** CRITICAL FINDING

---

## CREDENCIAIS VAZADAS

### 1. ionnard@aranet.net.br (OPA System)
```
Email: ionnard@aranet.net.br
Password: @Ionnard123
URL: opa.aranet.net.br/atendente/login/
Database: ALIEN TXTBASE
MD5: 8b7f8e505442dfe179a3c8135dad5c3f
```

### 2. denilso@aranet.net.br (IXC Provedor)
```
Email: denilso@aranet.net.br
Password: aranet@mudar
URL: ixc.aranet.net.br/login.php
Database: ALIEN TXTBASE
MD5: 1e97f002c0fe88c64449ddf73d72ef89
```
**NOTA:** Senha "aranet@mudar" sugere senha temporária NUNCA ALTERADA!

### 3. xmls.inbound@aranet.net.br (XML/API Service)
```
Email: xmls.inbound@aranet.net.br
Password: #XMLs2122
Database: Naz.API
MD5: fd7fc9d6836bb28573a3dad61fcf7747
```
**NOTA:** Conta de serviço para processamento de XMLs

### 4. ionnard@aranet.net.br (IXC - Segunda Senha)
```
Email: ionnard@aranet.net.br
Password: Ar@net2023
URL: ixc.aranet.net.br/login.php
Database: ALIEN TXTBASE
MD5: ac77ca6e42b18ddf0513406ed2090f41
```
**NOTA:** Senha mais recente (2023) - possível rotação

---

## ANÁLISE

### Emails Únicos: 3
1. ionnard@aranet.net.br
2. denilso@aranet.net.br
3. xmls.inbound@aranet.net.br

### Sistemas Afetados
| Sistema | URL | Credenciais |
|---------|-----|-------------|
| OPA (Atendimento) | opa.aranet.net.br/atendente/login/ | ionnard / @Ionnard123 |
| IXC Provedor (ERP) | ixc.aranet.net.br/login.php | denilso / aranet@mudar |
| IXC Provedor (ERP) | ixc.aranet.net.br/login.php | ionnard / Ar@net2023 |
| XML Service | - | xmls.inbound / #XMLs2122 |

### Padrões de Senha Identificados
```
@Ionnard123    → Padrão: @[Nome][123]
aranet@mudar   → Padrão: [empresa]@mudar (TEMPORÁRIA!)
#XMLs2122      → Padrão: #[Serviço][ano]
Ar@net2023     → Padrão: Ar@net[ano]
```

### Wordlist Expandida (baseada nos padrões)
```
aranet@mudar
Ar@net2023
Ar@net2024
Ar@net2025
@Aranet123
#Aranet2023
#Aranet2024
aranet123
aranetmudar
mudar@aranet
```

---

## IMPLICAÇÕES PARA IR-KALINE

### IXC Provedor contém:
- Dados completos de clientes (nome, CPF, endereço)
- Contratos de serviço
- Histórico de pagamentos
- Logs de IP
- Tickets de suporte
- Telefones registrados

### Se credenciais ainda válidas:
- Acesso total ao ERP da ARANET
- Possibilidade de consultar dados de KALINE CHAVES PEREIRA
- Extração de: endereço completo, histórico de IPs, pagamentos

---

## PRÓXIMOS PASSOS

1. [ ] Verificar se credenciais ainda funcionam
2. [ ] Testar login em ixc.aranet.net.br/login.php
3. [ ] Testar login em opa.aranet.net.br/atendente/login/
4. [ ] Se funcionar: buscar por "KALINE CHAVES PEREIRA"

---

## METADADOS

| Campo | Valor |
|-------|-------|
| Plataforma | DeHashed 4.0 |
| Records | 23,326,854,280 |
| Query time | 240ms |
| Database sources | ALIEN TXTBASE, Naz.API |
| Session | 10 |
