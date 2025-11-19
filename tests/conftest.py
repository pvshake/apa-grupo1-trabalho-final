"""
Configuração do pytest para melhorar a exibição dos testes.
"""

import pytest
from _pytest.terminal import TerminalReporter


def pytest_runtest_logstart(nodeid, location):
    """Exibe informações quando um teste começa."""
    print(f"\n{'='*80}")
    print(f"🧪 Executando: {nodeid.split('::')[-1]}")
    print(f"{'='*80}")


def pytest_runtest_logreport(report):
    """Exibe informações detalhadas sobre cada teste."""
    if report.when == "call":  # Apenas quando o teste é executado
        if report.outcome == "passed":
            print(f"✅ PASSOU: {report.nodeid.split('::')[-1]}")
            if hasattr(report, 'duration'):
                print(f"   ⏱️  Tempo: {report.duration:.4f}s")
        elif report.outcome == "failed":
            print(f"❌ FALHOU: {report.nodeid.split('::')[-1]}")
            print(f"   {report.longreprtext}")
        elif report.outcome == "skipped":
            print(f"⏭️  PULADO: {report.nodeid.split('::')[-1]}")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """Exibe informações antes de cada teste."""
    test_name = item.name
    docstring = item.function.__doc__
    if docstring:
        print(f"📝 {docstring.strip()}")


@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item, nextitem):
    """Exibe informações após cada teste."""
    print(f"{'-'*80}\n")

