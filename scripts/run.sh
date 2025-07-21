#!/bin/bash
. .venv/bin/activate
set -a && . ./.env && set +a

# Create logs directory in project root
mkdir -p logs

# Extract feature file name without extension
FEATURE_FILE="src/features/sample.feature"
FEATURE_NAME=$(basename "$FEATURE_FILE" .feature)

# Generate timestamp for execution directory
EXECUTION_TIMESTAMP=$(date '+%Y_%m_%d_%H_%M_%S')

# Create execution directory structure
EXECUTION_DIR="$SNAPSHOTS_PARENT_PATH/artifacts/$FEATURE_NAME/executions/$EXECUTION_TIMESTAMP"
mkdir -p "$EXECUTION_DIR/captures"
mkdir -p "$EXECUTION_DIR/html"

# Export variables for use in Python scripts
export EXECUTION_DIR
export FEATURE_NAME
export EXECUTION_TIMESTAMP

echo "実行開始: $(date)" | tee "$EXECUTION_DIR/behave_execution.log"
echo "Feature: $FEATURE_NAME" | tee -a "$EXECUTION_DIR/behave_execution.log"
echo "Execution ID: $EXECUTION_TIMESTAMP" | tee -a "$EXECUTION_DIR/behave_execution.log"
echo "========================================" | tee -a "$EXECUTION_DIR/behave_execution.log"

# Run behave and output to both console and log file
behave "$FEATURE_FILE" --format=plain --no-capture 2>&1 | tee -a "$EXECUTION_DIR/behave_execution.log"

echo "========================================" | tee -a "$EXECUTION_DIR/behave_execution.log"
echo "実行終了: $(date)" | tee -a "$EXECUTION_DIR/behave_execution.log"
echo "出力ディレクトリ: $EXECUTION_DIR" | tee -a "$EXECUTION_DIR/behave_execution.log"
echo "ログファイル: logs/log.txt" | tee -a "$EXECUTION_DIR/behave_execution.log"
echo "" | tee -a "$EXECUTION_DIR/behave_execution.log"
