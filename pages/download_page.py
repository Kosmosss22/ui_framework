import logging
from logger import LOGGER_NAME
from components.multi_web_element import MultiWebElement

logger = logging.getLogger(LOGGER_NAME)

class DownloadPage:
    def __init__(self, page):
        self.page = page

        self.list_files = MultiWebElement(
            locator=page.locator("a[href^='download/']"),
            page=page,
            description="list files"
        )

    def __str__(self):
        return "DownloadPage"

    def get_file_name(self, index):
        file_element = self.list_files.nth(index)
        return file_element.get_inner_text()

    def download_file(self, index):
        logger.info(f"{self} download file at index {index}")
        file_element = self.list_files.nth(index)

        with self.page.expect_download() as download:
            file_element.click()

        return download.value

