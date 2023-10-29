from datetime import datetime


# Utility
def now_str() -> str:
    return datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
