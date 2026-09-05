import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class DashboardPage(BasePage):

    profile_section = ".oxd-userdropdown-tab"

    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Verify dashboard is visible")
    def is_dashboard_visible(self):
        self.expect_is_visible(self.profile_section)
        self.attach_screenshot()