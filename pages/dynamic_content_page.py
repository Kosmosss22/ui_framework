import logging
from logger import LOGGER_NAME
from components.multi_web_element import MultiWebElement

logger = logging.getLogger(LOGGER_NAME)


class DynamicContent:
    def __init__(self, page):
        self.page = page

        self.images = MultiWebElement(
            locator=page.locator(".large-2 img"),
            page=page,
            description="Dynamic content images"
        )

        self.MAX_RETRIES = 10

    def __str__(self):
        return "DynamicContent page"

    def get_images_src(self):
        logger.info(f"{self} get all src")
        return [element.get_attribute("src") for element in self.images.all()]

    def has_matching_pair(self):
        logger.info(f"{self} try to get pair")
        all_src = self.get_images_src()
        has_matching = len(all_src) != len(set(all_src))

        return has_matching

    def wait_for_matching_images(self):
        logger.info(f"{self} waiting for matching img")

        for try_cnt in range(self.MAX_RETRIES):

            if try_cnt > 0:
                self.page.reload()
                self.page.wait_for_load_state("networkidle")

            if self.has_matching_pair():
                logger.info(f"{self} matching pair found")
                return True

            logger.info(f"{self} not mtching pair yeat")

        raise RuntimeError(f"no matching pair after {self.MAX_RETRIES}")