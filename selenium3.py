from selenium import webdriver
import time
import datetime
from selenium.webdriver.support import expected_conditions as excon
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

def make_screenshot(d):
    teraz = datetime.datetime.now()
    screenshot = 'screenshot' + teraz.strftime('_%H%M%S') + '.png'
    d.get_screenshot_as_file(screenshot)

def czekaj_na_id(element_id):
    timeout = 10
    timeout_message = f'Element id {element_id} not found in {timeout} s.'
    localizer = ('id', element_id)  # search by.ID
    localized = excon.visibility_of_element_located(localizer)
    wait = WebDriverWait(driver, timeout)
    return wait.until(localized, timeout_message)

#edge to background + ChromeOptions + FirefoxOptions
option = webdriver.EdgeOptions()
option.add_argument('headless')

# + option headless
driver = webdriver.Edge(options= option) # msedgedriver must be in project path
driver.get('http://www.saucedemo.com/')

try:
    lgn_btn = czekaj_na_id("login-button")
except TimeoutException:
    make_screenshot(driver)
    raise   # raise error ethier way
else:
    print('Found')
finally:
    make_screenshot(driver)
    time.sleep(2)
    driver.quit()