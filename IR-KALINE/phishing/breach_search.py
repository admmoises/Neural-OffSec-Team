#!/usr/bin/env python3
"""
IR-KALINE - Breach Database Search
==================================
Pesquisa automatizada em múltiplas breach databases

Uso: python3 breach_search.py

DADOS ALVO:
- CPF: 09126926180
- Email: chavespereirakaline@gmail.com
- Telefone: +5563992237479
- Nome: KALINE CHAVES PEREIRA
"""

import requests
import json
import time
from datetime import datetime
import os
from urllib.parse import quote

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
# DADOS DO ALVO
# ============================================
TARGET = {
    'nome': 'KALINE CHAVES PEREIRA',
    'cpf': '09126926180',
    'cpf_formatted': '091.269.261-80',
    'email': 'chavespereirakaline@gmail.com',
    'telefone': '+5563992237479',
    'telefone_local': '63992237479',
    'cidade': 'Araguaina',
    'estado': 'TO'
}

# ============================================
# RESULTADOS
# ============================================
results = {
    'timestamp': datetime.now().isoformat(),
    'target': TARGET,
    'findings': []
}

# ============================================
# HEADERS PADRÃO
# ============================================
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
}

# ============================================
# BREACH DATABASES - PESQUISA MANUAL
# ============================================

def print_banner():
    print(f"""
{Colors.RED}
 ██████╗ ██████╗ ███████╗ █████╗  ██████╗██╗  ██╗
 ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝██║  ██║
 ██████╔╝██████╔╝█████╗  ███████║██║     ███████║
 ██╔══██╗██╔══██╗██╔══╝  ██╔══██║██║     ██╔══██║
 ██████╔╝██║  ██║███████╗██║  ██║╚██████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
{Colors.RESET}
{Colors.CYAN}       [ BREACH DATABASE SEARCH ]{Colors.RESET}
{Colors.YELLOW}       Neural OffSec Team - IR-KALINE{Colors.RESET}
    """)

def search_databreach_sus():
    """
    DataBreach.com - SUS Brazil 2024
    177 milhões de registros
    """
    print(f"\n{Colors.CYAN}[1/6] DataBreach.com - SUS Brazil 2024{Colors.RESET}")
    print(f"     URL: https://databreach.com/breach/sus-brazil-2024")
    print(f"     {Colors.YELLOW}⚠ PESQUISA MANUAL NECESSÁRIA{Colors.RESET}")
    print(f"     Campos de busca:")
    print(f"       - CPF: {TARGET['cpf']}")
    print(f"       - Nome: {TARGET['nome']}")
    print(f"       - Telefone: {TARGET['telefone_local']}")
    print(f"     {Colors.GREEN}→ Dados esperados: CPF, Nome, Endereço, Cartão SUS, Telefone{Colors.RESET}")

    results['findings'].append({
        'source': 'databreach.com/sus-brazil-2024',
        'status': 'MANUAL_SEARCH_REQUIRED',
        'search_terms': [TARGET['cpf'], TARGET['nome'], TARGET['telefone_local']],
        'expected_data': ['CPF', 'Nome', 'Endereço', 'Cartão SUS', 'Telefone']
    })

def search_snusbase():
    """
    SnusBase - Múltiplos breaches
    Requer API key (paga)
    """
    print(f"\n{Colors.CYAN}[2/6] SnusBase.com{Colors.RESET}")
    print(f"     URL: https://snusbase.com/")
    print(f"     {Colors.YELLOW}⚠ REQUER CONTA/API KEY{Colors.RESET}")
    print(f"     Buscar por:")
    print(f"       - Email: {TARGET['email']}")
    print(f"       - Username: kaline.chaves.14")
    print(f"     {Colors.GREEN}→ Dados esperados: Senhas, Hashes, IPs históricos{Colors.RESET}")

    results['findings'].append({
        'source': 'snusbase.com',
        'status': 'REQUIRES_API_KEY',
        'search_terms': [TARGET['email'], 'kaline.chaves.14'],
        'pricing': '$2.99/day ou $9.99/month'
    })

def search_leakcheck():
    """
    LeakCheck.io - Credenciais vazadas
    """
    print(f"\n{Colors.CYAN}[3/6] LeakCheck.io{Colors.RESET}")
    print(f"     URL: https://leakcheck.io/")
    print(f"     {Colors.YELLOW}⚠ REQUER CONTA{Colors.RESET}")
    print(f"     Buscar por:")
    print(f"       - Email: {TARGET['email']}")
    print(f"     {Colors.GREEN}→ Dados esperados: Senhas em texto claro, fontes do vazamento{Colors.RESET}")

    results['findings'].append({
        'source': 'leakcheck.io',
        'status': 'REQUIRES_ACCOUNT',
        'search_terms': [TARGET['email']],
        'pricing': '$2.99/day'
    })

def search_intelx():
    """
    Intelligence X - Deep web indexing
    """
    print(f"\n{Colors.CYAN}[4/6] Intelligence X (IntelX.io){Colors.RESET}")
    print(f"     URL: https://intelx.io/")
    print(f"     Buscar por:")
    print(f"       - Email: {TARGET['email']}")
    print(f"       - CPF: {TARGET['cpf']}")
    print(f"       - Telefone: {TARGET['telefone']}")
    print(f"     {Colors.GREEN}→ Dados esperados: Pastes, documentos, deep web mentions{Colors.RESET}")

    # IntelX tem busca gratuita limitada
    try:
        url = f"https://2.intelx.io/phonebook/search?term={quote(TARGET['email'])}&maxresults=10&media=0&target=1&terminate=[]"
        print(f"     {Colors.YELLOW}Tentando API pública...{Colors.RESET}")
        # Nota: API requer autenticação para resultados reais
    except Exception as e:
        pass

    results['findings'].append({
        'source': 'intelx.io',
        'status': 'PARTIAL_FREE_SEARCH',
        'search_terms': [TARGET['email'], TARGET['cpf'], TARGET['telefone']],
        'expected_data': ['Pastes', 'Documents', 'Deep web']
    })

def search_hibp():
    """
    Have I Been Pwned - Verificação de email
    """
    print(f"\n{Colors.CYAN}[5/6] Have I Been Pwned{Colors.RESET}")
    print(f"     URL: https://haveibeenpwned.com/")
    print(f"     Buscar por:")
    print(f"       - Email: {TARGET['email']}")

    try:
        # HIBP API v3 requer API key
        url = f"https://haveibeenpwned.com/unifiedsearch/{quote(TARGET['email'])}"
        response = requests.get(url, headers={
            **HEADERS,
            'hibp-api-key': 'YOUR_API_KEY'  # Substituir
        }, timeout=10)

        if response.status_code == 200:
            data = response.json()
            print(f"     {Colors.RED}⚠ EMAIL ENCONTRADO EM BREACHES!{Colors.RESET}")
            results['findings'].append({
                'source': 'haveibeenpwned.com',
                'status': 'FOUND',
                'data': data
            })
        elif response.status_code == 404:
            print(f"     {Colors.GREEN}✓ Email não encontrado em breaches conhecidos{Colors.RESET}")
            results['findings'].append({
                'source': 'haveibeenpwned.com',
                'status': 'NOT_FOUND'
            })
        else:
            print(f"     {Colors.YELLOW}⚠ API bloqueada (Cloudflare) - verificar manualmente{Colors.RESET}")

    except Exception as e:
        print(f"     {Colors.RED}✗ Erro: {e}{Colors.RESET}")
        results['findings'].append({
            'source': 'haveibeenpwned.com',
            'status': 'ERROR',
            'error': str(e)
        })

def search_dehashed():
    """
    DeHashed - Breach database
    """
    print(f"\n{Colors.CYAN}[6/6] DeHashed.com{Colors.RESET}")
    print(f"     URL: https://dehashed.com/")
    print(f"     {Colors.YELLOW}⚠ REQUER CONTA PAGA{Colors.RESET}")
    print(f"     Buscar por:")
    print(f"       - Email: {TARGET['email']}")
    print(f"       - Nome: {TARGET['nome']}")
    print(f"     {Colors.GREEN}→ Dados esperados: Senhas, IPs, usernames associados{Colors.RESET}")

    results['findings'].append({
        'source': 'dehashed.com',
        'status': 'REQUIRES_SUBSCRIPTION',
        'search_terms': [TARGET['email'], TARGET['nome']],
        'pricing': '$5.99/month'
    })

def google_dorks():
    """
    Google Dorks para busca passiva
    """
    print(f"\n{Colors.CYAN}[BONUS] Google Dorks{Colors.RESET}")

    dorks = [
        f'"{TARGET["email"]}"',
        f'"{TARGET["cpf_formatted"]}" OR "{TARGET["cpf"]}"',
        f'"{TARGET["telefone_local"]}" OR "{TARGET["telefone"]}"',
        f'"{TARGET["nome"]}"',
        f'site:facebook.com "kaline chaves"',
        f'site:olx.com.br "kaline" araguaina',
        f'intext:"{TARGET["email"]}" filetype:txt',
        f'intext:"{TARGET["cpf"]}" filetype:sql OR filetype:csv',
    ]

    print(f"     Execute manualmente no Google:")
    for i, dork in enumerate(dorks, 1):
        print(f"     {i}. {dork}")
        results['findings'].append({
            'source': 'google_dork',
            'dork': dork
        })

def generate_report():
    """
    Gera relatório final
    """
    print(f"\n{Colors.GREEN}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}RELATÓRIO FINAL{Colors.RESET}")
    print(f"{Colors.GREEN}{'='*60}{Colors.RESET}")

    print(f"""
{Colors.YELLOW}ALVO:{Colors.RESET}
  Nome:     {TARGET['nome']}
  CPF:      {TARGET['cpf_formatted']}
  Email:    {TARGET['email']}
  Telefone: {TARGET['telefone']}

{Colors.YELLOW}PRÓXIMOS PASSOS:{Colors.RESET}
  1. Acessar databreach.com/breach/sus-brazil-2024 e buscar CPF
  2. Criar conta em snusbase.com ou leakcheck.io
  3. Executar Google dorks manualmente
  4. Verificar HIBP manualmente (Cloudflare blocking)

{Colors.YELLOW}LINKS DIRETOS:{Colors.RESET}
  • https://databreach.com/breach/sus-brazil-2024
  • https://snusbase.com/
  • https://leakcheck.io/
  • https://intelx.io/
  • https://haveibeenpwned.com/
  • https://dehashed.com/
    """)

    # Salvar resultados
    output_file = f"breach_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"{Colors.GREEN}[+] Resultados salvos em: {output_file}{Colors.RESET}")

# ============================================
# MAIN
# ============================================
def main():
    print_banner()

    print(f"{Colors.BOLD}Iniciando pesquisa em breach databases...{Colors.RESET}")
    print(f"{Colors.YELLOW}Alvo: {TARGET['nome']} ({TARGET['email']}){Colors.RESET}")

    search_databreach_sus()
    time.sleep(1)

    search_snusbase()
    time.sleep(1)

    search_leakcheck()
    time.sleep(1)

    search_intelx()
    time.sleep(1)

    search_hibp()
    time.sleep(1)

    search_dehashed()
    time.sleep(1)

    google_dorks()

    generate_report()

if __name__ == '__main__':
    main()
