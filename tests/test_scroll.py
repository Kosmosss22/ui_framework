from pages.scroll_page import ScrollPage
from logger import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)

def test_scroll(page):
    logger.info("Test: Starting scroll test")
    scroll_page = ScrollPage(page)
    url = "https://the-internet.herokuapp.com/infinite_scroll"

    page.goto(url)

    scroll_page.wait_for_paragraphs()
    cnt_paragraphs = scroll_page.get_paragraphs_count()
    assert cnt_paragraphs >= 10