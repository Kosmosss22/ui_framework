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
    assert alert_message == "I am a JS Alert", (
        f"Unexpected alert text.\n"
        f"Expected: 'I am a JS Alert'\n"
        f"Actual:   '{alert_message}'"
    )

    result = alerts_page.get_result_text()
    assert result == "You successfully clicked an alert", (
        f"Unexpected result after alert.\n"
        f"Expected: 'You successfully clicked an alert'\n"
        f"Actual:   '{result}'"
    )

    confirm_message = actions.run_and_accept_alert(
        lambda: alerts_page.trigger_confirm()
    )
    assert confirm_message == "I am a JS Confirm", (
        f"Unexpected confirm text.\n"
        f"Expected: 'I am a JS Confirm'\n"
        f"Actual:   '{confirm_message}'"
    )

    result = alerts_page.get_result_text()
    assert result == "You clicked: Ok", (
        f"Unexpected result after confirm.\n"
        f"Expected: 'You clicked: Ok'\n"
        f"Actual:   '{result}'"
    )

    random_word = fake.word()

    prompt_message = actions.run_and_accept_prompt(
        lambda: alerts_page.trigger_prompt(),
        prompt_text=random_word
    )
    assert prompt_message == "I am a JS prompt", (
        f"Unexpected prompt text.\n"
        f"Expected: 'I am a JS prompt'\n"
        f"Actual:   '{prompt_message}'"
    )

    result = alerts_page.get_result_text()
    assert result == f"You entered: {random_word}", (
        f"Unexpected result after prompt.\n"
        f"Expected: 'You entered: {random_word}'\n"
        f"Actual:   '{result}'"
    )

    logger.info("TEST: All alert scenarios passed")