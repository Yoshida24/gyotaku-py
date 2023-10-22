#!/bin/bash
. .venv/bin/activate
set -a && . ./.env && set +a
behave src/features/sample.feature
