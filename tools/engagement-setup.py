#!/usr/bin/env python3
"""
Engagement Setup Script
Automatiza a criação de estrutura de diretórios para novos pentests.

Usage:
    python tools/engagement-setup.py \
        --client "ACME-Corp" \
        --type "web-pentest" \
        --scope "*.acme.com" \
        --start-date "2025-11-09"
"""

import argparse
import os
import shutil
from datetime import datetime
from pathlib import Path
import pytz

# Timezone Brasil
BRT = pytz.timezone('America/Sao_Paulo')

def get_timestamp_brt():
    """Retorna timestamp formatado em BRT."""
    return datetime.now(BRT).strftime('%Y-%m-%d %H:%M:%S BRT')

def create_engagement_structure(client, eng_type, scope, start_date):
    """
    Cria estrutura completa de diretórios para um novo engagement.

    Args:
        client: Nome do cliente (ex: "ACME-Corp")
        eng_type: Tipo de pentest (ex: "web-pentest", "network-pentest")
        scope: Escopo resumido (ex: "portal", "full-infrastructure")
        start_date: Data de início no formato YYYY-MM-DD
    """

    # Construir nome do engagement: YYYY-MM-DD-ClientName-type-scope
    eng_name = f"{start_date}-{client}-{eng_type}-{scope}"

    # Diretório base do cliente
    client_dir = Path(f"clients/{client}")
    client_dir.mkdir(parents=True, exist_ok=True)

    # Diretório do engagement
    eng_dir = client_dir / eng_name

    if eng_dir.exists():
        print(f"⚠️  Engagement já existe: {eng_dir}")
        response = input("Sobrescrever? (y/N): ")
        if response.lower() != 'y':
            print("❌ Operação cancelada.")
            return None
        shutil.rmtree(eng_dir)

    # Criar estrutura de diretórios
    directories = [
        "00-engagement",
        "01-reconnaissance/passive",
        "01-reconnaissance/active",
        "02-vulnerability-assessment/web",
        "02-vulnerability-assessment/network",
        "03-exploitation/successful-exploits",
        "03-exploitation/failed-attempts",
        "03-exploitation/post-exploitation",
        "04-evidence/screenshots",
        "04-evidence/packet-captures",
        "04-evidence/logs",
        "04-evidence/videos",
        "05-notes/daily-notes",
        "05-notes/findings",
        "05-notes/scratchpad/test-scripts",
        "06-reports/drafts",
        "06-reports/final",
        "06-reports/remediation",
    ]

    print(f"\n📁 Criando estrutura para: {eng_name}")
    print(f"   Diretório: {eng_dir}\n")

    for dir_path in directories:
        full_path = eng_dir / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"   ✓ {dir_path}")

    # Copiar templates
    print(f"\n📋 Copiando templates...")

    templates_dir = Path("templates/engagement")

    # Scope template
    scope_template = templates_dir / "scope-template.md"
    if scope_template.exists():
        scope_dest = eng_dir / "00-engagement" / "scope.md"
        shutil.copy(scope_template, scope_dest)

        # Substituir placeholders
        content = scope_dest.read_text()
        content = content.replace("{{CLIENT_NAME}}", client)
        content = content.replace("{{ENGAGEMENT_NAME}}", eng_name)
        content = content.replace("{{START_DATE}}", start_date)
        content = content.replace("{{TYPE}}", eng_type)
        scope_dest.write_text(content)
        print(f"   ✓ scope.md")

    # RoE template
    roe_template = templates_dir / "roe-template.md"
    if roe_template.exists():
        roe_dest = eng_dir / "00-engagement" / "rules-of-engagement.md"
        shutil.copy(roe_template, roe_dest)

        content = roe_dest.read_text()
        content = content.replace("{{CLIENT_NAME}}", client)
        content = content.replace("{{ENGAGEMENT_NAME}}", eng_name)
        content = content.replace("{{ROE_DATE}}", start_date)
        roe_dest.write_text(content)
        print(f"   ✓ rules-of-engagement.md")

    # Copiar checklists apropriados
    checklists_dir = templates_dir / "checklists"
    if checklists_dir.exists():
        if "web" in eng_type.lower():
            web_checklist = checklists_dir / "web-pentest-checklist.md"
            if web_checklist.exists():
                dest = eng_dir / "02-vulnerability-assessment" / "web" / "checklist.md"
                shutil.copy(web_checklist, dest)
                print(f"   ✓ web-pentest-checklist.md")

            owasp_checklist = checklists_dir / "owasp-top10-2021.md"
            if owasp_checklist.exists():
                dest = eng_dir / "02-vulnerability-assessment" / "web" / "owasp-top10-checklist.md"
                shutil.copy(owasp_checklist, dest)
                print(f"   ✓ owasp-top10-checklist.md")

    # Criar arquivos iniciais
    print(f"\n📝 Criando arquivos iniciais...")

    # Chain of custody
    chain_file = eng_dir / "04-evidence" / "chain-of-custody.md"
    chain_content = f"""# Chain of Custody Log

**Engagement:** {eng_name}
**Created:** {get_timestamp_brt()}

## Evidence Log

| Timestamp | Finding ID | Evidence Type | File Path | SHA256 Hash | Operator |
|-----------|-----------|---------------|-----------|-------------|----------|
| | | | | | |

## Notes

- All timestamps in BRT (America/Sao_Paulo)
- Hash all evidence files with SHA256
- Update this log IMMEDIATELY when collecting evidence
"""
    chain_file.write_text(chain_content)
    print(f"   ✓ chain-of-custody.md")

    # Daily notes para hoje
    today = datetime.now(BRT).strftime('%Y-%m-%d')
    daily_note = eng_dir / "05-notes" / "daily-notes" / f"{today}-notes.md"
    note_content = f"""# Daily Notes - {today}

**Engagement:** {eng_name}
**Date:** {get_timestamp_brt()}

## Activities

### Morning
- [ ]

### Afternoon
- [ ]

### Evening
- [ ]

## Findings Discovered

-

## Next Steps

-

## Notes

-
"""
    daily_note.write_text(note_content)
    print(f"   ✓ {today}-notes.md")

    # Methodology checklist
    methodology_file = eng_dir / "01-reconnaissance" / "methodology-checklist.md"
    methodology_content = """# Reconnaissance Methodology Checklist

## Passive OSINT
- [ ] WHOIS lookup
- [ ] DNS enumeration (dns_lookup)
- [ ] Subdomain discovery (sublist3r_enum)
- [ ] Certificate transparency logs
- [ ] OSINT gathering (theharvester_osint)

## Active Scanning
- [ ] Port scanning (nmap_scan - quick)
- [ ] Port scanning (nmap_scan - full)
- [ ] Service enumeration
- [ ] Technology stack identification

## Analysis
- [ ] Attack surface mapping
- [ ] Identify high-value targets
- [ ] Document findings
"""
    methodology_file.write_text(methodology_content)
    print(f"   ✓ methodology-checklist.md")

    # README do engagement
    readme_file = eng_dir / "README.md"
    readme_content = f"""# {eng_name}

**Cliente:** {client}
**Tipo:** {eng_type}
**Escopo:** {scope}
**Data Início:** {start_date}
**Criado:** {get_timestamp_brt()}

## Quick Links

- [Scope](00-engagement/scope.md)
- [Rules of Engagement](00-engagement/rules-of-engagement.md)
- [Chain of Custody](04-evidence/chain-of-custody.md)
- [Daily Notes](05-notes/daily-notes/)

## Engagement Phases

1. ✅ Pre-Engagement (Setup concluído)
2. ⏳ Reconnaissance
3. ⏳ Vulnerability Assessment
4. ⏳ Exploitation
5. ⏳ Post-Exploitation
6. ⏳ Reporting

## MCP Security Toolkit Available

Use Claude Code com MCP Security Toolkit (25+ ferramentas):
- Reconnaissance: dns_lookup, nmap_scan, sublist3r_enum, theharvester_osint
- Web Testing: sqlmap_test, nikto_scan, gobuster_scan, wpscan
- Exploitation: metasploit_search, john_crack_hash, hydra_bruteforce
- Analysis: hash_analyzer, jwt_decoder, sslyze_scan

## Workspace Hygiene Reminders

⚠️ **Lembre-se:**
- Timestamps em BRT em TODOS os arquivos
- Scripts de teste: MAX 3 em test-scripts/, DELETE após uso
- Logs brutos: Parse e DELETE
- Documentar findings IMEDIATAMENTE quando descobertos
"""
    readme_file.write_text(readme_content)
    print(f"   ✓ README.md")

    # .gitignore para o engagement
    gitignore_file = eng_dir / ".gitignore"
    gitignore_content = """# Temporary files
*.tmp
*.bak
*.swp
*.log

# Raw scanner outputs (deve ser parseado e deletado)
*.xml.raw
*.json.raw

# Test scripts temporários
05-notes/scratchpad/test-scripts/*.py
05-notes/scratchpad/test-scripts/*.sh

# Large evidence files (commit hashes apenas)
04-evidence/videos/*.mp4
04-evidence/packet-captures/*.pcap
"""
    gitignore_file.write_text(gitignore_content)
    print(f"   ✓ .gitignore")

    print(f"\n✅ Engagement criado com sucesso!\n")
    print(f"📂 Diretório: {eng_dir}")
    print(f"\n🚀 Próximos passos:")
    print(f"   1. Colocar carta de autorização em: {eng_dir}/00-engagement/authorization-letter.pdf")
    print(f"   2. Revisar e customizar: {eng_dir}/00-engagement/scope.md")
    print(f"   3. Revisar e customizar: {eng_dir}/00-engagement/rules-of-engagement.md")
    print(f"   4. Iniciar reconnaissance: cd {eng_dir} && code README.md")

    return eng_dir

def main():
    parser = argparse.ArgumentParser(
        description="Cria estrutura de diretórios para novo pentest engagement"
    )
    parser.add_argument(
        "--client",
        required=True,
        help="Nome do cliente (ex: ACME-Corp)"
    )
    parser.add_argument(
        "--type",
        required=True,
        help="Tipo de pentest (ex: web-pentest, network-pentest, full-stack)"
    )
    parser.add_argument(
        "--scope",
        required=True,
        help="Escopo resumido (ex: portal, api, full-infrastructure)"
    )
    parser.add_argument(
        "--start-date",
        help="Data de início (YYYY-MM-DD). Default: hoje",
        default=datetime.now(BRT).strftime('%Y-%m-%d')
    )

    args = parser.parse_args()

    # Validar data
    try:
        datetime.strptime(args.start_date, '%Y-%m-%d')
    except ValueError:
        print("❌ Formato de data inválido. Use YYYY-MM-DD")
        return 1

    # Criar engagement
    create_engagement_structure(
        client=args.client,
        eng_type=args.type,
        scope=args.scope,
        start_date=args.start_date
    )

    return 0

if __name__ == "__main__":
    exit(main())
