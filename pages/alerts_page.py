import logging
from logger import LOGGER_NAME
from components.webelement import WebElement

logger = logging.getLogger(LOGGER_NAME)


class AlertsPage:
    def __init__(self, page):
        self.page = page

        self.button_js_alert = WebElement(
            locator=page.getByRole("button", name="Click for JS Alert"),
            page=page,
            description="Кнопка JS Alert"
        )

        self.button_js_confirm = WebElement(
            locator=page.getByRole("button", name="Click for JS Confirm"),
            page=page,
            description="Кнопка JS Confirm"
        )

        self.button_js_prompt = WebElement(
            locator=page.getByRole("button", name="Click for JS Prompt"),
            page=page,
            description="Кнопка JS Prompt"
        )

        self.result_message = WebElement(
            locator=page.locator('p#result'),
            page=page,
            description="Секция Result"
        )

    def __str__(self):
        return "AlertsPage"

    def trigger_alert(self):
        logger.info(f"{self} Click for JS Alert")
        self.button_js_alert.click()

    def trigger_confirm(self):
        logger.info(f"{self} Click for JS Confirm")
        self.button_js_confirm.click()

    def trigger_prompt(self):
        logger.info(f"{self} click and fill prompt")
        self.button_js_prompt.click()

    def get_result_text(self):
        return self.result_message.get_text_content()
