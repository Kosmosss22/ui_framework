from actions.page_actions import PageActions
from components.webelement import WebElement

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
        return self.actions.run_and_accept_alert(
            action=lambda: self.hot_spot_div.right_click()
        )
