import behave

from playwright.sync_api import sync_playwright, Browser, Page
from src.modules.scraper import save_capture, save_html_snapshot


from src.modules.util import now_str
from src.modules.constants import user_agent, locale


# Set start datetime
start_datetime_str = now_str()


# Setup Playwright
global_p = sync_playwright().start()
context_browser: Browser | None = None
context_page: Page | None = None


@behave.given('I open "{url}"')
def step_open_url(context, url):
    global context_browser, context_page, user_agent, locale
    context_browser = global_p.chromium.launch(headless=True)
    context_page = context_browser.new_page(user_agent=user_agent, locale=locale)
    context_page.goto(url)


@behave.then('I click the "{selector}"')
def step_click_button(context, selector: str):
    if context_page is None:
        raise Exception("No page has been opened")
    button = context_page.locator(selector).nth(0)
    button.click()


@behave.then('I goto "{url}"')
def step_goto_url(context, url: str):
    if context_page is None:
        raise Exception("No page has been opened")
    context_page.goto(url)


@behave.then("I wait for {seconds:d} seconds")
def step_wait(context, seconds: int):
    if context_page is None:
        raise Exception("No page has been opened")
    context_page.wait_for_timeout(seconds * 1000)


@behave.then('I save a capture to "{additional_path}"')
def step_save_capture(context, additional_path: str):
    if context_page is None:
        raise Exception("No page has been opened")
    if context_browser is None:
        raise Exception("No browser has been opened")
    save_capture(context_page, additional_path, start_datetime_str=start_datetime_str)


@behave.then(
    'I save a capture with suffix to "{additional_path}", file suffix is "{file_suffix}"'
)
def step_save_capture_with_fixture(context, additional_path: str, file_suffix: str):
    if context_page is None:
        raise Exception("No page has been opened")
    if context_browser is None:
        raise Exception("No browser has been opened")
    save_capture(
        context_page,
        additional_path,
        file_suffix=file_suffix,
        start_datetime_str=start_datetime_str,
    )


@behave.then('I save a HTML snapshot to "{additional_path}"')
def step_save_snapshot(context, additional_path: str):
    if context_page is None:
        raise Exception("No page has been opened")
    if context_browser is None:
        raise Exception("No browser has been opened")
    save_html_snapshot(
        context_page, additional_path, start_datetime_str=start_datetime_str
    )


@behave.then(
    'I save a HTML snapshot with suffix to "{additional_path}", file suffix is "{file_suffix}"'
)
def step_save_snapshot_with_fixture(context, additional_path: str, file_suffix: str):
    if context_page is None:
        raise Exception("No page has been opened")
    if context_browser is None:
        raise Exception("No browser has been opened")
    save_html_snapshot(
        context_page,
        additional_path,
        file_suffix=file_suffix,
        start_datetime_str=start_datetime_str,
    )


@behave.then("end")
def step_end(context):
    if context_browser is None:
        raise Exception("No browser has been opened")
    context_browser.close()
