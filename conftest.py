import os

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from playwright.sync_api import sync_playwright, Browser, Page

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


@pytest.fixture()
def browser():
    with sync_playwright() as playwright:
        # Headed + real Chrome locally (unchanged); headless Chromium in CI,
        # where there's no display and no Chrome install.
        browser = playwright.chromium.launch(headless=bool(os.getenv("CI")))
        yield browser
        browser.close()

@pytest.fixture()
@allure.title("Prepare for the test")
def page(browser: Browser, request: pytest.FixtureRequest):
    page = browser.new_page()
    yield page

    failed = any(
        getattr(request.node, f"rep_{phase}", None) is not None
        and getattr(request.node, f"rep_{phase}").failed
        for phase in ("setup", "call")
    )

    if failed:
        allure.attach(
            page.screenshot(full_page=True),
            name="failure-screenshot",
            attachment_type=allure.attachment_type.PNG
        )

    page.close()


@pytest.fixture()
@allure.title("Test data for login")
def credentials():
    return "Admin", "admin123"

@pytest.fixture()
def login_page(page: Page) -> LoginPage:
    return LoginPage(page).open()

@pytest.fixture()
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    output = yield
    report = output.get_result()
    setattr(item, f"rep_{report.when}", report)
