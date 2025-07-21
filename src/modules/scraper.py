from playwright.sync_api import Page


from pathlib import Path
from src.modules.constants import snapshots_path


def save_capture(
    page: Page,
    additional_path: str | None = None,
    file_prefix: str = "",
    file_suffix: str = "",
    start_datetime_str: str = "",
) -> None:
    file_name = file_prefix + start_datetime_str + file_suffix + ".png"

    # 新しいディレクトリ構造では、additional_pathの最後の部分のみを使用
    if additional_path is not None:
        # "welcome/captures" -> "captures" のように最後の部分のみ取得
        subdir = Path(additional_path).name
        path = Path(snapshots_path) / subdir
    else:
        path = Path(snapshots_path)

    path.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=path / file_name, full_page=True)


def save_html_snapshot(
    page: Page,
    additional_path: str | None = None,
    file_prefix: str = "",
    file_suffix: str = "",
    start_datetime_str: str = "",
) -> None:
    file_name = file_prefix + start_datetime_str + file_suffix + ".html"

    # 新しいディレクトリ構造では、additional_pathの最後の部分のみを使用
    if additional_path is not None:
        # "welcome/html" -> "html" のように最後の部分のみ取得
        subdir = Path(additional_path).name
        path = Path(snapshots_path) / subdir
    else:
        path = Path(snapshots_path)

    path.mkdir(parents=True, exist_ok=True)
    content = page.content()
    with open(path / file_name, "w") as f:
        f.write(content)
