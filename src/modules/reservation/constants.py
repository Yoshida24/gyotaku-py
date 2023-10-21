from pathlib import Path
from ..conatants.constants import snapshots_path

if snapshots_path is None:
    raise Exception("SNAPSHOTS_PATH is not set")
RESERVATION_DATA_PATH = Path(snapshots_path) / "reservations"
RESERVATION_CAPTURE_PATH = RESERVATION_DATA_PATH / "captures"
RESERVATION_HTML_PATH = RESERVATION_DATA_PATH / "html"
