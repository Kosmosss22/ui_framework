from pages.dynamic_content_page import DynamicContent
from logger import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)


def test_dynamic_content(page):
    logger.info("TEST: Starting dynamic content test")
    dynamic_content_page = DynamicContent(page)
    url = "https://the-internet.herokuapp.com/dynamic_content"

    page.goto(url)

    dynamic_content_page.wait_for_matching_images()