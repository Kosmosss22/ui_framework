import logging
from logger import LOGGER_NAME
from components.frame_element import FrameElement
logger = logging.getLogger(LOGGER_NAME)


class FramePage:
    def __init__(self, page):
        self.page = page

        top_frame = page.frame_locator('frame[name="frame-top"]')

        self.left_frame = FrameElement(
            frame_locator=top_frame.frame_locator('frame[name="frame-left"]'),
            page=page,
            description="left frame"
        )

        self.right_frame = FrameElement(
            frame_locator=top_frame.frame_locator('frame[name="frame-right"]'),
            page=page,
            description="right frame"
        )

        self.middle_frame = FrameElement(
            frame_locator=top_frame.frame_locator('frame[name="frame-middle"]'),
            page=page,
            description="middle frame"
        )

        self.bottom_frame = FrameElement(
            frame_locator=page.frame_locator('frame[name="frame-bottom"]'),
            page=page,
            description="bottom frame"
        )

        self._frames_map = {
            "left": self.left_frame,
            "right": self.right_frame,
            "middle": self.middle_frame,
            "bottom": self.bottom_frame,
        }

    def __str__(self):
        return "FramePage"

    def get_text_from_frame(self, frame_key):
        frame_element = self._frames_map[frame_key]
        return frame_element.get_text_from_body()
