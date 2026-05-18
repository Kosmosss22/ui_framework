import logging
from logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class FramePage:
    TOP_FRAME = 'frame[name="frame-top"]'
    LEFT_FRAME = 'frame[name="frame-left"]'
    MIDDLE_FRAME = 'frame[name="frame-middle"]'
    RIGHT_FRAME = 'frame[name="frame-right"]'
    BOTTOM_FRAME = 'frame[name="frame-bottom"]'

    def __init__(self, page):
        self.page = page

        top_frame = page.frame_locator(self.TOP_FRAME)

        self.left_frame = top_frame.frame_locator(self.LEFT_FRAME)
        self.middle_frame = top_frame.frame_locator(self.MIDDLE_FRAME)
        self.right_frame = top_frame.frame_locator(self.RIGHT_FRAME)
        self.bottom_frame = page.frame_locator(self.BOTTOM_FRAME)

    def __str__(self):
        return "FramePage"

    def get_text_from_frame(self, frame_locator):
        logger.info(f"{self} get text from frame")
        return frame_locator.locator("body").inner_text().strip()