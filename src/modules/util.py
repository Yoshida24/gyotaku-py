from datetime import datetime
import os
import time
from pathlib import Path


# Utility
def now_str() -> str:
    return datetime.now().strftime("%Y%m%d%H%M%S%f")[:17]


def log_message(message: str) -> None:
    """
    ログメッセージをプロジェクトルートのlogs/log.txtに保存する
    形式: timestamp:::メッセージ
    """
    # プロジェクトルートのlogsディレクトリに保存
    # スクリプト実行時のカレントディレクトリがプロジェクトルートになっている前提
    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "log.txt"

    # タイムスタンプを生成
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ログエントリを作成
    log_entry = f"{timestamp}:::{message}\n"

    # ファイルに追記
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)


def log_step_start(step_name: str) -> float:
    """
    ステップ開始をログに記録し、開始時刻を返す
    """
    start_time = time.time()
    log_message(f"[STEP START] {step_name}")
    return start_time


def log_step_end(step_name: str, start_time: float) -> None:
    """
    ステップ終了をログに記録し、実行時間を計算
    """
    end_time = time.time()
    duration = end_time - start_time
    log_message(f"[STEP END] {step_name} (実行時間: {duration:.3f}秒)")


def log_with_timing(step_name: str):
    """
    デコレータ：ステップの実行時間を自動計測してログに記録
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = log_step_start(step_name)
            try:
                result = func(*args, **kwargs)
                log_step_end(step_name, start_time)
                return result
            except Exception as e:
                log_message(f"[STEP ERROR] {step_name} - エラー: {str(e)}")
                raise

        return wrapper

    return decorator
