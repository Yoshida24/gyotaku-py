import os

# Constants
_snapshots_parent_path = os.environ.get("SNAPSHOTS_PARENT_PATH", None)
if _snapshots_parent_path is None:
    raise Exception("SNAPSHOTS_PATH is not set")

# New directory structure: artifacts/feature_name/executions/timestamp/
execution_dir = os.environ.get("EXECUTION_DIR", None)
if execution_dir is None:
    # Fallback to old structure for backward compatibility
    snapshots_path = _snapshots_parent_path + "/artifacts/snapshots"
else:
    snapshots_path = execution_dir

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
locale = "ja-JP"
