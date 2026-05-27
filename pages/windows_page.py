from components.webelement import WebElement


class WindowsPage:
    def __init__(self, page):
        self.page = page

        self.click_here_link = WebElement(
            locator=page.locator('.example a'),
            page=page,
            description="Link: 'Click Here'"
        )

        self.new_window_text = WebElement(
            locator=page.locator('.example h3'),
            page=page,
            description="New Window"
        )

    def __str__(self):
        return "WindowsPage"

    def click_here(self):
        self.click_here_link.click()

    def get_new_window_text(self):
        return self.new_window_text.get_inner_text()