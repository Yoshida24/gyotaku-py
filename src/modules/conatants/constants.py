import os

_snapshots_parent_path = os.environ.get("SNAPSHOTS_PARENT_PATH", "")
if _snapshots_parent_path is None:
    raise Exception("SNAPSHOTS_PATH is not set")

snapshots_path = _snapshots_parent_path + "/snapshots"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
locale = "ja-JP"
