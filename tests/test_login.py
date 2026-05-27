from pages.basic_auth_page import BasicAuthPage
from logger import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)


def test_basic_auth(page):
    logger.info("TEST: Starting basic auth test")

    auth_page = BasicAuthPage(page)
    login = "admin"
    password = "admin"
    url = f"https://{login}:{password}@the-internet.herokuapp.com/basic_auth"

    page.goto(url)
    message = auth_page.get_success_message()
    expected_text = "Congratulations! You must have the proper credentials."

    assert expected_text in message, (
        f"Success message mismatch:\n"
        f"  Expected substring: '{expected_text}'\n"
        f"  Actual message:     '{message}'"
    )

    logger.info("TEST: basic auth scenarios passed")
