#!/bin/bash
(python3 -m venv .venv || python -m venv .venv) && . .venv/bin/activate

# Python 3.13対応のための環境変数設定
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1

pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# playwrightを直接実行ではなく、python -mで実行
python -m playwright install
python -m playwright install-deps

cp .env.sample .env
echo '.env is created. please set env.'
