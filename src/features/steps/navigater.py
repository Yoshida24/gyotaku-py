import behave
import os

from playwright.sync_api import sync_playwright, Browser, Page
from src.modules.scraper import save_capture, save_html_snapshot
from dataclasses import dataclass


from src.modules.util import now_str, log_message
from src.modules.constants import user_agent, locale


# Set global variables
@dataclass
class Context:
    start_datetime_str: str = ""
    browser: Browser | None = None
    page: Page | None = None


@behave.given('I open "{url}"')
def step_open_url(context: Context, url):
    # 実行ディレクトリ情報をログに記録
    execution_dir = os.environ.get("EXECUTION_DIR", "不明")
    feature_name = os.environ.get("FEATURE_NAME", "不明")
    execution_timestamp = os.environ.get("EXECUTION_TIMESTAMP", "不明")

    log_message(f"=== 実行開始 ===")
    log_message(f"Feature: {feature_name}")
    log_message(f"実行ID: {execution_timestamp}")
    log_message(f"出力ディレクトリ: {execution_dir}")
    log_message(f"ブラウザを開いてURL {url} に移動しています")

    global_p = sync_playwright().start()
    context.start_datetime_str = now_str()
    context.browser = global_p.chromium.launch(headless=True)
    context.page = context.browser.new_page(user_agent=user_agent, locale=locale)
    context.page.goto(url)
    log_message(f"URL {url} への移動が完了しました")


@behave.then("I wait for {seconds} seconds")
def step_wait(context: Context, seconds):
    if context.page is None:
        raise Exception("No page has been opened")
    log_message(f"{seconds}秒待機しています")
    context.page.wait_for_timeout(int(seconds) * 1000)
    log_message(f"{seconds}秒の待機が完了しました")


@behave.then('I click the "{selector}"')
def step_click(context: Context, selector):
    if context.page is None:
        raise Exception("No page has been opened")
    log_message(f"要素 {selector} をクリックしています")
    context.page.click(selector)
    log_message(f"要素 {selector} のクリックが完了しました")


@behave.then('I save a capture to "{additional_path}"')
def step_save_capture(context: Context, additional_path: str):
    if context.page is None:
        raise Exception("No page has been opened")
    if context.browser is None:
        raise Exception("No browser has been opened")
    log_message(f"スクリーンショットを {additional_path} に保存しています")
    save_capture(
        context.page, additional_path, start_datetime_str=context.start_datetime_str
    )
    log_message(f"スクリーンショットの保存が完了しました: {additional_path}")


@behave.then(
    'I save a capture with suffix to "{additional_path}", file suffix is "{file_suffix}"'
)
def step_save_capture_with_fixture(
    context: Context, additional_path: str, file_suffix: str
):
    if context.page is None:
        raise Exception("No page has been opened")
    if context.browser is None:
        raise Exception("No browser has been opened")
    log_message(
        f"スクリーンショット（サフィックス: {file_suffix}）を {additional_path} に保存しています"
    )
    save_capture(
        context.page,
        additional_path,
        file_suffix=file_suffix,
        start_datetime_str=context.start_datetime_str,
    )
    log_message(
        f"スクリーンショットの保存が完了しました: {additional_path}/{file_suffix}"
    )


@behave.then('I save a HTML snapshot to "{additional_path}"')
def step_save_snapshot(context: Context, additional_path: str):
    if context.page is None:
        raise Exception("No page has been opened")
    if context.browser is None:
        raise Exception("No browser has been opened")
    log_message(f"HTMLスナップショットを {additional_path} に保存しています")
    save_html_snapshot(
        context.page, additional_path, start_datetime_str=context.start_datetime_str
    )
    log_message(f"HTMLスナップショットの保存が完了しました: {additional_path}")


@behave.then(
    'I save a HTML snapshot with suffix to "{additional_path}", file suffix is "{file_suffix}"'
)
def step_save_snapshot_with_fixture(
    context: Context, additional_path: str, file_suffix: str
):
    if context.page is None:
        raise Exception("No page has been opened")
    if context.browser is None:
        raise Exception("No browser has been opened")
    log_message(
        f"HTMLスナップショット（サフィックス: {file_suffix}）を {additional_path} に保存しています"
    )
    save_html_snapshot(
        context.page,
        additional_path,
        file_suffix=file_suffix,
        start_datetime_str=context.start_datetime_str,
    )
    log_message(
        f"HTMLスナップショットの保存が完了しました: {additional_path}/{file_suffix}"
    )


@behave.then("end")
def step_end(context: Context):
    if context.browser is None:
        raise Exception("No browser has been opened")
    log_message("ブラウザを終了しています")
    context.browser.close()
    log_message("ブラウザの終了が完了しました")
    log_message("=== 実行完了 ===")
