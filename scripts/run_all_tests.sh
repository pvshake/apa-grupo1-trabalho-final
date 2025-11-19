#!/usr/bin/env bash

# Executa toda a suíte de testes do projeto.
# Uso:
#   ./scripts/run_all_tests.sh          # execução sequencial (default)
#   ./scripts/run_all_tests.sh --parallel  # tenta execução paralela (requer pytest-xdist)

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${PROJECT_ROOT}"

PYTEST_ARGS=("python3" "-m" "pytest" "tests" "-v")

if [[ "${1:-}" == "--parallel" ]]; then
  if python3 - <<'PY' >/dev/null 2>&1
import importlib
import sys

module = importlib.util.find_spec("xdist")
sys.exit(0 if module is not None else 1)
PY
  then
    PYTEST_ARGS+=("-n" "auto")
  else
    echo "⚠️  pytest-xdist não instalado. Executando em modo sequencial..."
  fi
fi

"${PYTEST_ARGS[@]}"


