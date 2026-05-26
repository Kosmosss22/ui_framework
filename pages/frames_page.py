from enum import Enum
import logging
from logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)

class FrameType(Enum):
    LEFT = "left"
    RIGHT = "right"
    MIDDLE = "middle"
    BOTTOM = "bottom"

class FramePage:
    def __init__(self, page):
        self.page = page

        top_frame = page.frame_locator('frame[name="frame-top"]')

        self.left_frame = top_frame.frame_locator('frame[name="frame-left"]')
        self.right_frame = top_frame.frame_locator('frame[name="frame-right"]')
        self.middle_frame = top_frame.frame_locator('frame[name="frame-middle"]')
        self.bottom_frame = page.frame_locator('frame[name="frame-bottom"]')

        self._frames_map = {
            FrameType.LEFT: self.left_frame,
            FrameType.RIGHT: self.right_frame,
            FrameType.MIDDLE: self.middle_frame,
            FrameType.BOTTOM: self.bottom_frame,
        }

    def __str__(self):
        return "FramePage"

    def get_text_from_frame(self, frame_type: FrameType) -> str:
        frame_locator = self._frames_map[frame_type]
        logger.info(f"{self} get text from frame '{frame_type.value}'")
        return frame_locator.locator("body").inner_text().strip()