import logging
from logger import LOGGER_NAME
from components.webelement import WebElement


logger = logging.getLogger(LOGGER_NAME)


class ContextClick:
    def __init__(self, page):
        self.page = page

        self.hot_spot_div = WebElement(
            locator=page.locator("#hot-spot"),
            page=page,
            description="div for right click"
        )

    def __str__(self):
        return "ContextClickPage"

    def perform_right_click_and_get_alert(self):
        logger.info(f"{self} right click and get alert")

        dialog_message = None

        def handle_dialog(dialog):
            nonlocal dialog_message

            dialog_message = dialog.message
            dialog.accept()

        self.page.on("dialog", handle_dialog)

        try:
            self.hot_spot_div.right_click()
        finally:
            self.page.remove_listener("dialog", handle_dialog)

        return dialog_message