import behave

from playwright.sync_api import sync_playwright, Browser, Page
from src.modules.scraper import save_capture, save_html_snapshot
from dataclasses import dataclass


from src.modules.util import now_str
from src.modules.constants import user_agent, locale


# Set global variables
@dataclass
class Context:
    start_datetime_str: str = ""
    browser: Browser | None = None
    page: Page | None = None


@behave.given('I open "{url}"')
def step_open_url(context: Context, url):
    global_p = sync_playwright().start()
    context.start_datetime_str = now_str()
    context.browser = global_p.chromium.launch(headless=True)
    context.page = context.browser.new_page(user_agent=user_agent, locale=locale)
    context.page.goto(url)


@behave.then('I click the "{selector}"')
def step_click_button(context: Context, selector: str):
    if context.page is None:
        raise Exception("No page has been opened")
    button = context.page.locator(selector).nth(0)
    button.click()


@behave.then('I goto "{url}"')
def step_goto_url(context: Context, url: str):
    if context.page is None:
        raise Exception("No page has been opened")
    context.page.goto(url)


@behave.then("I wait for {seconds:d} seconds")
def step_wait(context: Context, seconds: int):
    if context.page is None:
        raise Exception("No page has been opened")
    context.page.wait_for_timeout(seconds * 1000)


@behave.then('I save a capture to "{additional_path}"')
def step_save_capture(context: Context, additional_path: str):
    if context.page is None:
        raise Exception("No page has been opened")
    if context.browser is None:
        raise Exception("No browser has been opened")
    save_capture(
        context.page, additional_path, start_datetime_str=context.start_datetime_str
    )


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
    save_capture(
        context.page,
        additional_path,
        file_suffix=file_suffix,
        start_datetime_str=context.start_datetime_str,
    )


@behave.then('I save a HTML snapshot to "{additional_path}"')
def step_save_snapshot(context: Context, additional_path: str):
    if context.page is None:
        raise Exception("No page has been opened")
    if context.browser is None:
        raise Exception("No browser has been opened")
    save_html_snapshot(
        context.page, additional_path, start_datetime_str=context.start_datetime_str
    )


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
    save_html_snapshot(
        context.page,
        additional_path,
        file_suffix=file_suffix,
        start_datetime_str=context.start_datetime_str,
    )


@behave.then("end")
def step_end(context: Context):
    if context.browser is None:
        raise Exception("No browser has been opened")
    context.browser.close()
