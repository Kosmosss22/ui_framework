from pages.frames_page import FramePage, FrameType  # ← Импортируем Enum
from logger import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)


def test_frames(page):
    logger.info("TEST: Starting frames test")

    frames_page = FramePage(page)
    page.goto("https://the-internet.herokuapp.com/nested_frames")

    frames_data = {
        FrameType.LEFT: "LEFT",
        FrameType.RIGHT: "RIGHT",
        FrameType.MIDDLE: "MIDDLE",
        FrameType.BOTTOM: "BOTTOM",
    }

    for frame_type, expected_text in frames_data.items():
        text = frames_page.get_text_from_frame(frame_type)
        assert expected_text in text, (
            f"Text mismatch in frame '{frame_type.value}':\n"
            f"  Expected: '{expected_text}'\n"
            f"  Actual:   '{text}'"
        )
