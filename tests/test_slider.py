import random
from pages.slider_page import SliderPage
from logger import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)


def test_slider(page):
    logger.info("Test: Starting slider test")
    slider_page = SliderPage(page)
    url = "https://the-internet.herokuapp.com/horizontal_slider"

    page.goto(url)

    min_val, max_val = slider_page.get_slider_min_max()
    step = slider_page.get_step()

    steps_count = int((max_val - min_val) / step)
    random_step = random.randint(1, steps_count - 1)

    target_value = min_val + random_step * step
    target_value = round(target_value, 1)

    slider_page.set_value_keyboard(target_value)
    display_value = slider_page.get_displayed_value()

    assert float(display_value) == target_value, (
        f"Slider value mismatch:\n"
        f"  Expected: {target_value}\n"
        f"  Actual:   {float(display_value)}"
    )
