from pages.upload_page import UploadPage
from logger import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)

def test_upload_file(page):
    logger.info("TEST: Starting upload file test")
    upload_page = UploadPage(page)
    url = "https://the-internet.herokuapp.com/upload"
    file_path = "test_files/test"

    page.goto(url)

    upload_page.upload_file(file_path)
    result_text = upload_page.get_result_text()

    assert "File Uploaded!" in result_text