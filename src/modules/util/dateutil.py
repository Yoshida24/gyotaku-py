from datetime import datetime


def now_str() -> str:
    return datetime.now().strftime("%Y%m%d%H:%M:%S")