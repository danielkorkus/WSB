from selenium import webdriver
from time import sleep

driver = webdriver.Edge(executable_path=r'.\msedgedriver.exe')
driver.get('https://www.google.com/')
sleep(3)
driver.quit()
