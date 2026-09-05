import random

import allure
from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def go_to_url(self, url: str) -> None:
        self.page.goto(url, wait_until="domcontentloaded")


    def enter_value(self, locator: str, value: str) -> None:
        self.page.locator(locator).clear()
        self.page.locator(locator).fill(value)


    def click_button(self, locator: str) -> None:
        self.page.locator(locator).click()


    def expect_is_visible(self, locator: str):
        expect(self.page.locator(locator)).to_be_visible()


    def wait_for_visible(self, locator: str):
        self.page.locator(locator).wait_for()


    def attach_screenshot(self):
        allure.attach(
            self.page.screenshot(full_page=True),
            name="step_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
