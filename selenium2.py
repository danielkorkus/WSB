from selenium import webdriver
import time
import datetime


def make_screenshot(d):
    teraz = datetime.datetime.now()
    screenshot = 'screenshot' + teraz.strftime('_%H%M%S') + '.png'
    d.get_screenshot_as_file(screenshot)


driver = webdriver.Edge()
driver.get('http://www.saucedemo.com/')
print('Nazwa strony ', driver.title)

try:
    pole_user = driver.find_element('id', 'user-name')
    pole_user.clear()
    pole_user.send_keys('standard_user')

except:
    make_screenshot(driver)

pole_haslo = driver.find_element('xpath', '//*[@id="password"]')
pole_haslo.clear()
pole_haslo.send_keys('secret_sauce')
przycisk_login = driver.find_element('id', 'login-button')
# print(przycisk_login.get_attribute('enabled'))

if przycisk_login.get_attribute('disabled') == None:
    przycisk_login.click()
else:
    make_screenshot(driver)

time.sleep(2)
make_screenshot(driver)
driver.quit()
