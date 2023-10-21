from playwright.async_api import async_playwright, Page
from ..conatants.constants import user_agent, locale
from .constants import RESERVATION_CAPTURE_PATH, RESERVATION_HTML_PATH
import time
from pathlib import Path
from ..util.dateutil import now_str


async def get_reservation_calender_page(page: Page) -> Page:
    await page.goto("https://beauty.hotpepper.jp/kr/slnH000651465/")
    time.sleep(2)

    await page.goto("https://beauty.hotpepper.jp/CSP/kr/reserve/?storeId=H000651465")
    time.sleep(2)

    await page.goto(
        "https://beauty.hotpepper.jp/CSP/kr/reserve/afterCoupon?storeId=H000651465&couponId=CP00000008901705&add=0"
    )

    # // <input type="radio" name="offMenu" value="OFF_NONE_VALUE" id="menuMC000" class="rsvSelectMenuRdobox cbF">
    off_radio = page.locator('input[type="radio"][value="OFF_NONE_VALUE"]').nth(0)
    await off_radio.click()
    time.sleep(2)

    # <input type="submit" name="afterNailOff" value="この内容で次へ" class="btn btn1H34 btnKr mHA w160" title="この内容で次へ">
    off_radio = page.locator('input[type="submit"][name="afterNailOff"]').nth(0)
    await off_radio.click()
    time.sleep(5)

    return page


async def save_reservation_capture(page: Page, path: Path) -> None:
    await page.screenshot(path=path, full_page=True)


async def save_reservation_html_snapshot(page: Page, path: Path) -> None:
    content = await page.content()
    with open(path, "w") as f:
        f.write(content)


async def post():
    async with async_playwright() as p:
        # init
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(user_agent=user_agent, locale=locale)

        # navigate
        reservation_calender_page = await get_reservation_calender_page(page)

        # save capture
        RESERVATION_CAPTURE_PATH.mkdir(parents=True, exist_ok=True)
        path_capture = RESERVATION_CAPTURE_PATH / Path(now_str() + ".png")
        await save_reservation_capture(
            page=reservation_calender_page, path=path_capture
        )

        # save html snapshot
        RESERVATION_HTML_PATH.mkdir(parents=True, exist_ok=True)
        path_html = RESERVATION_HTML_PATH / Path(now_str() + ".html")
        await save_reservation_html_snapshot(
            page=reservation_calender_page, path=path_html
        )
