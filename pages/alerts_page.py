import logging
from logger import LOGGER_NAME
from components.webelement import WebElement


logger = logging.getLogger(LOGGER_NAME)


class AlertsPage:
    def __init__(self, page):
        self.page = page

        self.button_js_alert = WebElement(
            locator=page.locator('button:has-text("Click for JS Alert")'),
            page=page,
            description="Кнопка JS Alert"
        )

        self.button_js_confirm = WebElement(
            locator=page.locator('button:has-text("Click for JS Confirm")'),
            page=page,
            description="Кнопка JS Confirm"
        )

        self.button_js_prompt = WebElement(
            locator=page.locator('button:has-text("Click for JS Prompt")'),
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

    # Код повторяется, я это заметил, но пока не буду исправлять
    def trigger_alert(self):
        logger.info(f"{self} Click for JS Alert")

        dialog_message = None

        def handle_dialog(dialog):
            nonlocal dialog_message
            dialog_message = dialog.message
            dialog.accept()

        self.page.on("dialog", handle_dialog)
        self.button_js_alert.click()
        self.page.remove_listener("dialog", handle_dialog)

        return dialog_message

    def trigger_confirm(self):
        logger.info(f"{self} Click for JS Confirm")

        dialog_message = None

        def handle_dialog(dialog):
            nonlocal dialog_message
            dialog_message = dialog.message
            dialog.accept()

        self.page.on("dialog", handle_dialog)
        self.button_js_confirm.click()
        self.page.remove_listener("dialog", handle_dialog)

        return dialog_message

    def trigger_prompt(self, input_text):
        logger.info(f"{self} click and fill prompt")

        dialog_message = None

        def handle_dialog(dialog):
            nonlocal dialog_message
            dialog_message = dialog.message
            dialog.accept(input_text)

        self.page.on("dialog", handle_dialog)
        self.button_js_prompt.click()
        self.page.remove_listener("dialog", handle_dialog)

        return dialog_message

    def get_result_text(self):
        logger.info(f"{self} get result text")
        return self.result_message.get_text_content()