from pages.download_page import DownloadPage
from logger import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)


def test_download(page):
    logger.info("TEST: Starting download test")
    download_page = DownloadPage(page)
    url = "https://the-internet.herokuapp.com/download"

    page.goto(url)

    expected_name = download_page.get_file_name(2)
    download = download_page.download_file(2)
    actual_name = download.suggested_filename

    assert expected_name == actual_name, (
        f"Download filename mismatch:\n"
        f"  Expected: '{expected_name}'\n"
        f"  Actual:   '{actual_name}'"
    )
