#!/usr/bin/env bash
# 在项目根目录执行：单元测试 + 覆盖率（目标 80%）
# 用法：bash scripts/run_tests.sh  或  ./scripts/run_tests.sh
set -e
cd "$(dirname "$0")/.."
ROOT=$(pwd)
export PYTHONPATH="${PYTHONPATH:-}:${ROOT}/src"
python -m pytest tests/ -v --cov=src --cov-report=term-missing --cov-report=html --cov-fail-under=80 "$@"
