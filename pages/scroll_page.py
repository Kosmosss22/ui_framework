import logging
from components.multi_web_element import MultiWebElement
from logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class ScrollPage:
    def __init__(self, page):
        self.page = page

        self.paragraphs = MultiWebElement(
            locator=page.locator(".jscroll-added"),
            page=page,
            description="all paragraphs"
        )

    def __str__(self):
        return "Scroll page"

    def get_paragraphs_count(self):
        logger.info(f"{self} get count paragraphs")
        cnt = self.paragraphs.count()
        return cnt

    def scroll_to_bottom(self):
        logger.info(f"{self} scroll to bottom")
        last_paragraph = self.paragraphs.last()
        last_paragraph.scroll_into_view_if_needed()

    def wait_for_paragraphs(self, target_count=10):
        logger.info(f"{self} waiting for paragraphs")
        max_attempts = 20
        for _ in range(max_attempts):
            current_paragraphs = self.get_paragraphs_count()
            if current_paragraphs >= target_count:
                return True

            self.scroll_to_bottom()
            self.page.wait_for_timeout(300)

        final_count = self.get_paragraphs_count()
        raise RuntimeError(f"Final count: {final_count}")
