#!/usr/bin/env python3
"""
Workspace Cleanup Script
Limpa arquivos temporários e outputs brutos de acordo com regras de hygiene.

Usage:
    # Dry-run (mostra o que seria deletado)
    python tools/cleanup-workspace.py --engagement clients/ACME/2025-11-09-web-portal --dry-run

    # Executar limpeza
    python tools/cleanup-workspace.py --engagement clients/ACME/2025-11-09-web-portal

    # Limpeza agressiva (inclui logs > 5 dias)
    python tools/cleanup-workspace.py --engagement clients/ACME/2025-11-09-web-portal --aggressive
"""

import argparse
import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path
import pytz

BRT = pytz.timezone('America/Sao_Paulo')

class WorkspaceCleanup:
    def __init__(self, engagement_path, dry_run=True, aggressive=False):
        self.engagement_path = Path(engagement_path)
        self.dry_run = dry_run
        self.aggressive = aggressive
        self.stats = {
            'files_deleted': 0,
            'dirs_deleted': 0,
            'space_freed': 0
        }

    def get_file_size(self, file_path):
        """Retorna tamanho do arquivo em bytes."""
        try:
            return file_path.stat().st_size
        except:
            return 0

    def delete_file(self, file_path, reason):
        """Deleta arquivo ou registra para dry-run."""
        size = self.get_file_size(file_path)

        if self.dry_run:
            print(f"   [DRY-RUN] DELETE: {file_path} ({size/1024:.2f} KB) - {reason}")
        else:
            try:
                file_path.unlink()
                print(f"   ✓ DELETED: {file_path} ({size/1024:.2f} KB) - {reason}")
                self.stats['files_deleted'] += 1
                self.stats['space_freed'] += size
            except Exception as e:
                print(f"   ✗ ERRO ao deletar {file_path}: {e}")

    def delete_directory(self, dir_path, reason):
        """Deleta diretório vazio ou registra para dry-run."""
        if self.dry_run:
            print(f"   [DRY-RUN] RMDIR: {dir_path} - {reason}")
        else:
            try:
                dir_path.rmdir()  # Remove apenas se vazio
                print(f"   ✓ RMDIR: {dir_path} - {reason}")
                self.stats['dirs_deleted'] += 1
            except OSError:
                pass  # Diretório não vazio, ok

    def cleanup_temp_files(self):
        """Remove arquivos temporários (.tmp, .bak, .swp)."""
        print("\n🧹 Limpando arquivos temporários...")

        temp_extensions = ['.tmp', '.bak', '.swp', '.temp', '~']

        for ext in temp_extensions:
            for file_path in self.engagement_path.rglob(f'*{ext}'):
                if file_path.is_file():
                    self.delete_file(file_path, f"Arquivo temporário ({ext})")

    def cleanup_raw_outputs(self):
        """Remove outputs brutos de scanners que devem ser parseados."""
        print("\n🧹 Limpando outputs brutos de scanners...")

        raw_patterns = ['*.xml.raw', '*.json.raw', '*.nmap.raw']

        for pattern in raw_patterns:
            for file_path in self.engagement_path.rglob(pattern):
                if file_path.is_file():
                    self.delete_file(file_path, "Output bruto de scanner")

    def cleanup_test_scripts(self):
        """Limpa scripts de teste em scratchpad."""
        print("\n🧹 Verificando scripts de teste...")

        test_scripts_dir = self.engagement_path / "05-notes" / "scratchpad" / "test-scripts"

        if not test_scripts_dir.exists():
            return

        scripts = list(test_scripts_dir.glob('*'))
        script_count = len([s for s in scripts if s.is_file()])

        if script_count > 3:
            print(f"   ⚠️  ALERTA: {script_count} scripts em test-scripts/ (MAX recomendado: 3)")
            print(f"   Revisar e manter apenas PoCs funcionais.")

            # Listar scripts por idade
            scripts_by_age = sorted(
                [s for s in scripts if s.is_file()],
                key=lambda x: x.stat().st_mtime,
                reverse=True
            )

            print(f"\n   Scripts (mais recente → mais antigo):")
            for i, script in enumerate(scripts_by_age, 1):
                age = datetime.now() - datetime.fromtimestamp(script.stat().st_mtime)
                print(f"     {i}. {script.name} (idade: {age.days} dias)")

    def cleanup_old_logs(self):
        """Remove logs com mais de 5 dias."""
        if not self.aggressive:
            print("\n⏭️  Pulando limpeza de logs (use --aggressive para habilitar)")
            return

        print("\n🧹 Limpando logs antigos (> 5 dias)...")

        logs_dir = self.engagement_path / "04-evidence" / "logs"

        if not logs_dir.exists():
            return

        cutoff_date = datetime.now(BRT) - timedelta(days=5)

        for log_file in logs_dir.rglob('*.log'):
            if log_file.is_file():
                mod_time = datetime.fromtimestamp(log_file.stat().st_mtime, tz=BRT)
                if mod_time < cutoff_date:
                    age_days = (datetime.now(BRT) - mod_time).days
                    self.delete_file(log_file, f"Log com {age_days} dias (> 5 dias)")

    def check_evidence_size(self):
        """Verifica tamanho de evidências e alerta se necessário."""
        print("\n📊 Verificando tamanho de evidências...")

        evidence_dir = self.engagement_path / "04-evidence"

        if not evidence_dir.exists():
            return

        # Contar screenshots
        screenshots_dir = evidence_dir / "screenshots"
        if screenshots_dir.exists():
            screenshot_count = len(list(screenshots_dir.glob('*')))
            if screenshot_count > 500:
                print(f"   ⚠️  ALERTA: {screenshot_count} screenshots (> 500)")
                print(f"   Considerar arquivar screenshots antigas ou organizar melhor.")

        # Calcular tamanho total
        total_size = sum(
            self.get_file_size(f)
            for f in evidence_dir.rglob('*')
            if f.is_file()
        )

        total_mb = total_size / (1024 * 1024)
        total_gb = total_mb / 1024

        print(f"   Tamanho total de evidências: {total_mb:.2f} MB ({total_gb:.2f} GB)")

        if total_gb > 5:
            print(f"   ⚠️  ALERTA: Workspace > 5GB")
            print(f"   Considerar mover para storage externo ou comprimir.")

    def cleanup_empty_directories(self):
        """Remove diretórios vazios."""
        print("\n🧹 Limpando diretórios vazios...")

        # Listar todos os diretórios, mais profundos primeiro
        all_dirs = sorted(
            [d for d in self.engagement_path.rglob('*') if d.is_dir()],
            key=lambda x: len(x.parts),
            reverse=True
        )

        for dir_path in all_dirs:
            if not any(dir_path.iterdir()):  # Vazio
                self.delete_directory(dir_path, "Diretório vazio")

    def run(self):
        """Executa todas as rotinas de limpeza."""
        if not self.engagement_path.exists():
            print(f"❌ Engagement não encontrado: {self.engagement_path}")
            return 1

        mode = "DRY-RUN MODE" if self.dry_run else "EXECUTION MODE"
        aggressive_mode = " (AGGRESSIVE)" if self.aggressive else ""
        print(f"\n{'='*60}")
        print(f"🧹 WORKSPACE CLEANUP - {mode}{aggressive_mode}")
        print(f"{'='*60}")
        print(f"Engagement: {self.engagement_path}")
        print(f"Timestamp: {datetime.now(BRT).strftime('%Y-%m-%d %H:%M:%S BRT')}")

        # Executar rotinas
        self.cleanup_temp_files()
        self.cleanup_raw_outputs()
        self.cleanup_test_scripts()
        self.cleanup_old_logs()
        self.check_evidence_size()
        self.cleanup_empty_directories()

        # Estatísticas finais
        print(f"\n{'='*60}")
        print(f"📊 ESTATÍSTICAS")
        print(f"{'='*60}")
        print(f"Arquivos deletados: {self.stats['files_deleted']}")
        print(f"Diretórios deletados: {self.stats['dirs_deleted']}")
        print(f"Espaço liberado: {self.stats['space_freed'] / (1024*1024):.2f} MB")

        if self.dry_run:
            print(f"\n⚠️  Nenhuma alteração foi feita (DRY-RUN)")
            print(f"   Execute sem --dry-run para aplicar mudanças.")

        return 0

def main():
    parser = argparse.ArgumentParser(
        description="Limpa workspace de engagement conforme regras de hygiene"
    )
    parser.add_argument(
        "--engagement",
        required=True,
        help="Caminho do engagement (ex: clients/ACME/2025-11-09-web-portal)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Mostra o que seria deletado sem executar"
    )
    parser.add_argument(
        "--aggressive",
        action="store_true",
        help="Habilita limpeza agressiva (logs > 5 dias)"
    )

    args = parser.parse_args()

    cleanup = WorkspaceCleanup(
        engagement_path=args.engagement,
        dry_run=args.dry_run,
        aggressive=args.aggressive
    )

    return cleanup.run()

if __name__ == "__main__":
    exit(main())
