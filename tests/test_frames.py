from pages.frames_page import FramePage
from logger import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)


def test_frames(page):
    logger.info("TEST: Starting frames test")
    frames_page = FramePage(page)
    url = "https://the-internet.herokuapp.com/nested_frames"
    page.goto(url)

    frames_data = {
        frames_page.LEFT_FRAME: "LEFT",
        frames_page.RIGHT_FRAME: "RIGHT",
        frames_page.MIDDLE_FRAME: "MIDDLE",
        frames_page.BOTTOM_FRAME: "BOTTOM",
    }

    for frame_name, expected_text in frames_data.items():
        text = frames_page.get_text_from_frame(frame_name)
        assert text == expected_text