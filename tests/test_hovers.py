from pages.hovers_page import HoversPage
from logger import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)

def test_hovers(page):
    logger.info("TEST: Starting hovers test")
    hovers_page = HoversPage(page)
    url = "https://the-internet.herokuapp.com/hovers"

    page.goto(url)

    cnt = hovers_page.get_users_cnt()
    assert cnt > 0

    for i in range(cnt):
        logger.info(f"Checking the user №{i}")
        hovers_page.hover_over_user(i)
        name = hovers_page.get_user_name(i)
        assert "name: user" in name
