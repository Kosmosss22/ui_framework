from components.webelement import WebElement


class SliderPage:
    def __init__(self, page):
        self.page = page

        self.slider = WebElement(
            locator=page.locator(".sliderContainer input"),
            page=page,
            description="slider"
        )

        self.slider_value = WebElement(
            locator=page.locator("#range"),
            page=page,
            description="slider value"
        )

    def __str__(self):
        return "SliderPage"

    def get_slider_min_max(self):
        get_min = self.slider.get_attribute("min")
        get_max = self.slider.get_attribute("max")

        return float(get_min), float(get_max)

    def get_step(self):
        step = self.slider.get_attribute("step")
        return float(step) if step else 0.5

    def set_value_keyboard(self, target_value):
        self.slider.focus()
        self.slider.press("Home")

        get_min = float(self.slider.get_attribute("min"))
        steps = self.get_step()

        presses_count = (target_value - get_min) / steps

        for _ in range(int(presses_count)):
            self.slider.press("ArrowRight")

    def get_displayed_value(self):
        return self.slider_value.get_text_content()
