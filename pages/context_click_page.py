import logging

from actions.page_actions import PageActions
from logger import LOGGER_NAME
from components.webelement import WebElement

logger = logging.getLogger(LOGGER_NAME)


class ContextClick:
    def __init__(self, page):
        self.page = page

        self.actions = PageActions(page)

        self.hot_spot_div = WebElement(
            locator=page.locator("#hot-spot"),
            page=page,
            description="div for right click"
        )

    def __str__(self):
        return "ContextClickPage"

    def perform_right_click_and_get_alert(self):
        logger.info(f"{self} right click and get alert")

        return self.actions.run_and_accept_alert(
            action=lambda: self.hot_spot_div.right_click()
        )
