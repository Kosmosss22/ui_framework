from pages.context_click_page import ContextClick
from logger import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)

def test_context_click(page):
    logger.info("TEST: Starting context click test")
    context_page = ContextClick(page)
    url = "https://the-internet.herokuapp.com/context_menu"
    page.goto(url)

    alert_text = context_page.perform_right_click_and_get_alert()
    expected_text = "You selected a context menu"
    assert alert_text == expected_text, (
        f"Alert text mismatch:\n"
        f"  Expected: '{expected_text}'\n"
        f"  Actual:   '{alert_text}'"
    )