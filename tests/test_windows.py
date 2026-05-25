from actions.page_actions import PageActions
from pages.windows_page import WindowsPage
from pages.new_window_page import NewWindowPage
from logger import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)

def test_windows(page):
    logger.info("TEST: Starting windows test")
    windows_page = WindowsPage(page)
    url = "https://the-internet.herokuapp.com/windows"

    page.goto(url)

    actions = PageActions(page)

    with actions.expect_new_page() as event_1:
        windows_page.click_here()

    page_1 = event_1.value
    win_1 = WindowsPage(page_1)
    text_1 = win_1.get_new_window_text()
    expected_text = "New Window"

    assert expected_text in text_1, (
        f"Text in first new window mismatch:\n"
        f"  Expected: '{expected_text}'\n"
        f"  Actual:   '{text_1}'"
    )

    with actions.expect_new_page() as event_2:
        windows_page.click_here()

    page_2 = event_2.value
    win_2 = NewWindowPage(page_2)
    text_2 = win_2.get_heading_text()

    assert expected_text in text_2, (
        f"Text in second new window mismatch:\n"
        f"  Expected: '{expected_text}'\n"
        f"  Actual:   '{text_2}'"
    )

    page_1.close()
    page_2.close()

    open_pages = actions.get_open_pages_count()
    assert open_pages == 1, f"Expected 1 open page, but got {open_pages}"