from logger import LOGGER_NAME
import logging
from components.webelement import WebElement

logger = logging.getLogger(LOGGER_NAME)

class NewWindowPage:
    def __init__(self, page):
        self.page = page
        self.heading = WebElement(
            locator=page.locator("h3"),
            page= page,
            description="heading"
        )

    def __str__(self):
        return "NewWindowPage"

    def get_heading_text(self):
        return self.heading.get_inner_text()