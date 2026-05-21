import logging
from playwright.sync_api import FrameLocator, Page
from logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class FrameElement:
    def __init__(self, frame_locator: FrameLocator, page: Page, description: str):
        self.page = page
        self.frame_locator = frame_locator
        self.description = description

    def __str__(self):
        return "FrameElement"

    def get_text_from_body(self):
        logger.info(f"{self} get text from frame")
        result = self.frame_locator.locator("body").inner_text().strip()
        return result
