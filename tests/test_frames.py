from pages.frames_page import FramePage
from logger import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)


def test_frames(page):
    logger.info("TEST: Starting frames test")

    frames_page = FramePage(page)
    page.goto("https://the-internet.herokuapp.com/nested_frames")

    frames_data = {
        "left": "LEFT",
        "right": "RIGHT",
        "middle": "MIDDLE",
        "bottom": "BOTTOM",
    }

    for key, expected_text in frames_data.items():
        text = frames_page.get_text_from_frame(key)
        assert expected_text in text, (
            f"Text mismatch in frame '{frame_key}':\n"
            f"  Expected: '{expected_text}'\n"
            f"  Actual:   '{text}'"
        )