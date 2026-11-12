import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from tests.test_login import VALID_EMAIL, VALID_PASSWORD


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://telranedu.web.app/home")

    yield driver

    driver.quit()


@pytest.fixture
def authentication(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(VALID_EMAIL)
    login_page.fill_password_field(VALID_PASSWORD)
    login_page.click_on_login_button()

    return driver