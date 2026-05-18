import logging
from logger import LOGGER_NAME
from components.webelement import WebElement


logger = logging.getLogger(LOGGER_NAME)


class BasicAuthPage:
    def __init__(self, page):
        self.page = page
        self.success_message = WebElement(
            locator=page.locator(".example p"),
            page=page,
            description="Congratulations! You must have the proper credentials."
        )

    def __str__(self):
        return "BasicAuthPage"

    def get_success_message(self):
        logger.info(f"{self} get text content")
        return self.success_message.get_text_content()