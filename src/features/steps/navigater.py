from behave import __all__

from playwright.sync_api import sync_playwright, Browser, Page

from pathlib import Path
import os
from datetime import datetime


# Utility
def now_str() -> str:
    return datetime.now().strftime("%Y_%m_%d_%H_%M_%S")


# Constants
_snapshots_parent_path = os.environ.get("SNAPSHOTS_PARENT_PATH", None)
if _snapshots_parent_path is None:
    raise Exception("SNAPSHOTS_PATH is not set")
snapshots_path = _snapshots_parent_path + "/snapshots"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
locale = "ja-JP"

# Set start datetime
start_datetime_str = now_str()


def save_reservation_capture(page: Page, additional_path: str | None = None) -> None:
    file_name = start_datetime_str + ".png"
    path = (
        Path(snapshots_path + "/" + additional_path)
        if additional_path is not None
        else Path(snapshots_path)
    )
    path.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=path / file_name, full_page=True)


def save_reservation_html_snapshot(
    page: Page, additional_path: str | None = None
) -> None:
    file_name = start_datetime_str + ".html"
    path = (
        Path(snapshots_path + "/" + additional_path)
        if additional_path is not None
        else Path(snapshots_path)
    )
    path.mkdir(parents=True, exist_ok=True)
    content = page.content()
    with open(path / file_name, "w") as f:
        f.write(content)


# Setup Playwright
global_p = sync_playwright().start()
context_browser: Browser | None = None
context_page: Page | None = None


@given('I open "{url}"')
def step_open_url(context, url):
    global context_browser, context_page, user_agent, locale
    context_browser = global_p.chromium.launch(headless=True)
    context_page = context_browser.new_page(user_agent=user_agent, locale=locale)
    context_page.goto(url)


@then('I click the "{selector}"')
def step_click_button(context, selector: str):
    if context_page is None:
        raise Exception("No page has been opened")
    button = context_page.locator(selector).nth(0)
    button.click()


@then('I goto "{url}"')
def step_goto_url(context, url: str):
    if context_page is None:
        raise Exception("No page has been opened")
    context_page.goto(url)


@then("I wait for {seconds:d} seconds")
def step_wait(context, seconds: int):
    if context_page is None:
        raise Exception("No page has been opened")
    context_page.wait_for_timeout(seconds * 1000)


@then('I save a capture to "{additional_path}"')
def save_capture(context, additional_path: str):
    if context_page is None:
        raise Exception("No page has been opened")
    if context_browser is None:
        raise Exception("No browser has been opened")
    save_reservation_capture(context_page, additional_path)


@then('I save a HTML snapshot to "{additional_path}"')
def save_snapshot(context, additional_path: str):
    if context_page is None:
        raise Exception("No page has been opened")
    if context_browser is None:
        raise Exception("No browser has been opened")
    save_reservation_html_snapshot(context_page, additional_path)


@then("end")
def end(context):
    if context_browser is None:
        raise Exception("No browser has been opened")
    context_browser.close()
