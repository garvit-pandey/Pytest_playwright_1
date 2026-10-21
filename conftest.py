import os
import pytest
from playwright.sync_api import Page
from dotenv import load_dotenv


# Load environment variables from .env or tests/.env
load_dotenv()


@pytest.fixture
def login_creds():
    return {
        "username": os.getenv("APP_USERNAME", "Test_User"),
        "password": os.getenv("APP_PASSWORD", "123"),
        "base_url": os.getenv("base_URL"),
        "timeout": int(os.getenv("TIMEOUT", "30")),
    }


@pytest.fixture
def home_page(page: Page, login_creds):
    page.set_default_timeout(login_creds["timeout"] * 1000)
    page.goto(login_creds["base_url"])
    return page


@pytest.fixture
def logged_in_page(home_page: Page, login_creds):
    home_page.fill("#email", login_creds["username"])        # replace with your real selectors
    home_page.fill("#password", login_creds["password"])
    home_page.click("#login")
    home_page.wait_for_url("**/dashboard")                   # wait until login really finishes
    return home_page


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "args": ["--start-maximized"],
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "no_viewport": True}
