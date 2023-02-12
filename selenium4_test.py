from selenium import webdriver
from selenium4 import LoginPage
import datetime
import time


def make_screenshot(d):
    teraz = datetime.datetime.now()
    screenshot = 'screenshot' + teraz.strftime('_%H%M%S') + '.png'
    d.get_screenshot_as_file(screenshot)


def test_loginpage():
    driver = webdriver.Edge()
    page = LoginPage(driver, 'user-name', 'password', 'login-button')
    page.open_page()
    page.enter_username('standard_user')
    page.enter_password('secret_sauce')
    page.click_login_button()
    time.sleep(3)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
    driver.quit()
