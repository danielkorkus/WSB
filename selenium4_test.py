from selenium import webdriver
from selenium4 import LoginPage
import datetime
import time
import pytest


def make_screenshot(d):
    teraz = datetime.datetime.now()
    screenshot = 'screenshot' + teraz.strftime('_%H%M%S') + '.png'
    d.get_screenshot_as_file(screenshot)


test_data = [('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
             ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
             ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
             ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html')]


@pytest.mark.parametrize('user, password, url', test_data)
def test_loginpage(user, password, url):
    driver = webdriver.Edge()
    page = LoginPage(driver, 'user-name', 'password', 'login-button')
    page.open_page()
    page.enter_username(user)
    page.enter_password(password)
    page.click_login_button()
    time.sleep(3)
    # after coma if assert failed
    try:
        assert driver.current_url == url, make_screenshot(driver)
    finally:
        driver.quit()
