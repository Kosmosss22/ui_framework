import logging
from components.multi_web_element import MultiWebElement
from logger import LOGGER_NAME


logger = logging.getLogger(LOGGER_NAME)

class HoversPage:
    def __init__(self, page):
        self.page = page

        self.user_imgs = MultiWebElement(
            locator=page.locator(".figure img"),
            page=page,
            description="user img"
        )

        self.user_names = MultiWebElement(
            locator=page.locator(".figcaption h5"),
            page=page,
            description="User names"
        )

    def __str__(self):
        return "Hovers page"

    def get_users_cnt(self):
        return self.user_imgs.count()

    def hover_over_user(self, index):
        user_img = self.user_imgs.nth(index)
        user_img.hover()
        self.user_names.nth(index).wait_for_visible()

    def get_user_name(self, index):
        get_name = self.user_names.nth(index)
        return get_name.get_inner_text()