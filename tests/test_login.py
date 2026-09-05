import allure

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


@allure.epic("OrangeHRM")
@allure.feature("Authentication")
class TestLogin:

    @allure.title("Verify valid login")
    @allure.description("Test to verify that a user can log in with valid credentials")
    def test_login_with_valid_credentials(self, credentials, login_page: LoginPage, dashboard_page: DashboardPage):
        username, password = credentials
        login_page.login(username, password)
        dashboard_page.is_dashboard_visible()

    @allure.title("Verify invalid login")
    @allure.description("Test to verify that a user can log in with invalid credentials")
    def test_login_with_invalid_credentials(self, credentials, login_page: LoginPage, dashboard_page: DashboardPage):
        login_page.login('abc', 'xyz')
        dashboard_page.is_dashboard_visible()