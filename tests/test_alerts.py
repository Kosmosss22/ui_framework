from faker import Faker
from actions.page_actions import PageActions
from pages.alerts_page import AlertsPage
from logger import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)


def test_alert(page):
    logger.info("TEST: Starting alerts test")
    alerts_page = AlertsPage(page)
    fake = Faker()
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    actions = PageActions(page)

    page.goto(url)

    alert_message = actions.run_and_accept_alert(
        lambda: alerts_page.trigger_alert()
    )
    assert alert_message == "I am a JS Alert"

    result = alerts_page.get_result_text()
    assert result == "You successfully clicked an alert"

    confirm_message = actions.run_and_accept_alert(
        lambda: alerts_page.trigger_confirm()
    )
    assert confirm_message == "I am a JS Confirm"

    result = alerts_page.get_result_text()
    assert result == "You clicked: Ok"

    random_word = fake.word()

    prompt_message = actions.run_and_accept_prompt(
        lambda: alerts_page.trigger_prompt(),
        prompt_text=random_word
    )
    assert prompt_message == "I am a JS prompt"

    result = alerts_page.get_result_text()
    assert result == f"You entered: {random_word}"

    logger.info("TEST: All alert scenarios passed")
