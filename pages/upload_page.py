import logging
from logger import LOGGER_NAME
from components.webelement import WebElement

logger = logging.getLogger(LOGGER_NAME)


class UploadPage:
    def __init__(self, page):
        self.page = page

        self.file_upload = WebElement(
            locator=page.locator("#file-upload"),
            page=page,
            description="file_upload"
        )

        self.submit_button = WebElement(
            locator=page.locator("#file-submit"),
            page=page,
            description="submit button"
        )

        self.result_message = WebElement(
            locator=page.locator("h3"),
            page=page,
            description="Result message"
        )


    def __str__(self):
        return "UploadPage"

    def upload_file(self, file_path):
        logger.info(f"{self} upload and submit file")
        self.file_upload.set_input_files(file_path)
        self.submit_button.click()

    def get_result_text(self):
        logger.info(f"{self} get result text")
        return self.result_message.get_inner_text()