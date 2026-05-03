import logging
from logger import LOGGER_NAME


logger = logging.getLogger(LOGGER_NAME)


class FramePage:
    def __init__(self, page):
        self.page = page

        self.LEFT_FRAME = "frame-left"
        self.MIDDLE_FRAME = "frame-middle"
        self.RIGHT_FRAME = "frame-right"
        self.BOTTOM_FRAME = "frame-bottom"

    def __str__(self):
        return "FramePage"

    def get_text_from_frame(self, frame_name):
        logger.info(f"{self} get text from frame {frame_name}")
        frame = self.page.frame(name= frame_name)
        text = frame.inner_text("body")

        return text