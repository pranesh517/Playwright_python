import allure
from playwright.sync_api import Page

from pages.base_page import BasePage

class LoginPage(BasePage):

    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    user_name = "input[placeholder='Username']"
    password = "input[placeholder='Password']"
    login_button = "button[type='submit']"

    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Launch OrangeHRM application")
    def open(self) -> "LoginPage":
        self.go_to_url(self.URL)
        return self

    @allure.step("Enter username: {username}")
    def enter_username(self, username: str) -> None:
        self.enter_value(self.user_name, username)

    @allure.step("Enter password: {password}")
    def enter_password(self, password: str) -> None:
        self.enter_value(self.password, password)

    @allure.step("Click on Login button")
    def click_login_button(self) -> None:
        self.click_button(self.login_button)

    @allure.step("Login to Orange HRM with username: {username}")
    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
