# DeHashed OSINT Report - IR-KALINE
**Data:** 26-11-2025 02:16 (GMT-3)
**Plataforma:** DeHashed 4.0 (23,326,854,280 records)
**Sessão:** 9

---

## TARGET PRINCIPAL

| Campo | Valor |
|-------|-------|
| Nome | KALINE CHAVES PEREIRA |
| CPF | 091.269.261-80 |
| Email | chavespereirakaline@gmail.com |
| WhatsApp | 63 99223-7479 |
| ISP | ARANET AS262462, Araguaína-TO |

---

## BUSCAS REALIZADAS

### Buscas Diretas (0 resultados cada)

| Query | Campo | Resultado |
|-------|-------|-----------|
| chavespereirakaline@gmail.com | Email | 0 |
| 63992237479 | Phone | 0 |
| KALINE CHAVES PEREIRA | Name | 37,785 (genéricos) |
| 09126926180 | Password | 0 |
| 09126926180 | Username | 0 |

### Buscas Regex (0 resultados para target)

| Padrão | Campo | Resultado |
|--------|-------|-----------|
| `/chavespereira/` | All | 23,995 (nenhum KALINE) |
| `/kaline.*chaves\|chaves.*kaline/` | All | 0 |
| `/kaline.*pereira\|pereira.*kaline/` | All | 0 |
| `/chavespereira.*kaline\|kaline.*chavespereira/` | Username | 0 |

---

## ACHADOS COLATERAIS RELEVANTES

### 1. Senha "chavespereira" usada por terceiros
```
Email: juuliaachaves@gmail.com
Password: chavespereira
Sites: Netflix, Twitter
Database: ALIEN TXTBASE
Hash MD5: c6162272427ca618e302ffe2f65e8fdc
```

### 2. Família "Chaves Pereira" no Brasil

| Nome | Database | Email | Dados |
|------|----------|-------|-------|
| michel chavespereira | Neopets.com | michel113@bol.com.br | Senha: 300589, DOB: 1989-05-30 |
| Edson ChavesPereira | Hurb | naboka@bol.com.br | IP: 187.59.94.87, Tel: 4299442552 |
| Alexis Chaves Pereira | Canva.com | chavespereira@gmx.fr | Username: chavespereira |
| Joao Paulo Chavespereira | MGM Grand Hotels | - | - |
| Adelia Chavespereira Pereira | Promo | adeliachavesp@gmail.com | BR |
| Marinalva Batista ChavesPereira | Canva.com | mari24101@hotmail.com | - |
| chavespereira (username) | Wattpad.com | andranunes50@gmail.com | DOB: 1994-09-19 |

### 3. Telefone Similar na Região
```
Telefone: 63992237473 (diferença: último dígito)
Nome: RUBEM MOREIRA DIAS
Cidade: Palmas, Tocantins
```

---

## ANÁLISE

### Conclusão Principal
**KALINE CHAVES PEREIRA possui footprint digital LIMPO em breach databases conhecidas.**

### Interpretação
1. Target nunca teve credenciais vazadas em breaches indexados
2. Email chavespereirakaline@gmail.com pode ser recente ou pouco usado
3. Ausência em leaks brasileiros (Promo, Hurb, etc) sugere baixa atividade digital
4. Padrão de senha potencial: "chavespereira" (usado por família)

### Próximos Vetores Recomendados
1. **SnusBase** - Database alternativo de breaches
2. **databreach.com/sus-brazil-2024** - Leaks brasileiros recentes
3. **IntelX** - Pastes e dark web
4. **Social Engineering** - Phishing page já preparada em `IR-KALINE/phishing/`
5. **ARANET Recon** - Shodan/Censys no AS262462

---

## WORDLIST PARA CREDENTIAL STUFFING

Baseada nos achados, senhas potenciais para target:

```
chavespereira
chavespereirakaline
kalinechaves
kaline2024
kaline@2024
091269261
09126926180
kaline091269
63992237479
araguaina
araguaina2024
tocantins
```

---

## METADADOS

- **Ferramenta:** DeHashed 4.0
- **Records Pesquisados:** 23,326,854,280
- **Tempo médio por query:** 134-225ms
- **Assinatura expira:** 7 dias
