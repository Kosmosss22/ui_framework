from pages.frames_page import FramePage
from logger import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)


def test_frames(page):
    logger.info("TEST: Starting frames test")

    frames_page = FramePage(page)
    page.goto("https://the-internet.herokuapp.com/nested_frames")

    frames_data = {
        frames_page.left_frame: "LEFT",
        frames_page.right_frame: "RIGHT",
        frames_page.middle_frame: "MIDDLE",
        frames_page.bottom_frame: "BOTTOM",
    }

    for frame_locator, expected_text in frames_data.items():
        text = frames_page.get_text_from_frame(frame_locator)

        assert text == expected_text