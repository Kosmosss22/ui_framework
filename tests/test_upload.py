from pages.upload_page import UploadPage
from logger import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)


def test_upload_file(page, temp_file):
    logger.info("TEST: Starting upload file test")
    upload_page = UploadPage(page)
    url = "https://the-internet.herokuapp.com/upload"

    page.goto(url)

    upload_page.upload_file(temp_file)
    result_text = upload_page.get_result_text()
    expected_text = "File Uploaded!"

    assert expected_text in result_text, (
        f"Upload result mismatch:\n"
        f"  Expected substring: '{expected_text}'\n"
        f"  Actual result:      '{result_text}'"
    )
