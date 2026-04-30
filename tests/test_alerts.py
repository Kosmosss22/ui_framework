from faker import Faker
from pages.alerts_page import AlertsPage
from logger import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)

def test_alert(page):
    logger.info("TEST: Starting alerts test")
    alerts_page = AlertsPage(page)
    fake = Faker()
    url = "https://the-internet.herokuapp.com/javascript_alerts"

    page.goto(url)

    # тест для кнопки Click for JS Alert
    alert_text = alerts_page.trigger_alert()
    assert alert_text == "I am a JS Alert"
    result = alerts_page.get_result_text()
    assert result == "You successfully clicked an alert"

    # тест для кнопки Click for JS Confirm
    alert_text = alerts_page.trigger_confirm()
    assert alert_text == "I am a JS Confirm"
    result = alerts_page.get_result_text()
    assert result == "You clicked: Ok"

    #тест для кнопки Click for JS Prompt
    random_word = fake.word()
    alert_text = alerts_page.trigger_prompt(random_word)
    assert alert_text == "I am a JS prompt"
    result = alerts_page.get_result_text()
    assert  result == f"You entered: {random_word}"

    logger.info("TEST: All alert scenarios passed")
