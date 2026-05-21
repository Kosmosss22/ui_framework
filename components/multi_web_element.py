from playwright.sync_api import Locator, Page
from typing_extensions import Self
from .webelement import WebElement

class MultiWebElement:
    def __init__(
            self,
            page: Page,
            locator: Locator,
            description: str,
    ) -> None:
        self.page = page
        self.locator = locator
        self.description = description
        self.index = 0

    def _make_element(self, locator: Locator, suffix: str) -> WebElement:
        return WebElement(
            locator=locator,
            page=self.page,
            description=f"{self.description}[{suffix}]",
        )

    def __iter__(self) -> Self:
        self.index = 0
        return self

    def __next__(self) -> WebElement:
        if self.index >= self.locator.count():
            raise StopIteration

        element = WebElement(
            locator=self.locator.nth(self.index),
            page=self.page,
            description=f"{self.description}[{self.index}]",
        )

        self.index += 1
        return element

    def nth(self, index: int) -> WebElement:
        return self._make_element(
            locator=self.locator.nth(index),
            suffix=str(index)
        )

    def first(self) -> WebElement:
        return self._make_element(
            locator=self.locator.first,
            suffix="first"
        )

    def last(self) -> WebElement:
        return self._make_element(
            locator=self.locator.last,
            suffix="last"
        )

    def count(self) -> int:
        return self.locator.count()

    def all(self) -> list[WebElement]:
        return [
            self._make_element(locator=loc, suffix=str(i))
            for i, loc in enumerate(self.locator.all())
        ]

    def __str__(self) -> str:
        return f"MultiWebElement[{self.description}]"