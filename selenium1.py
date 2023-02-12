from selenium import webdriver
from time import sleep

driver = webdriver.Edge(executable_path=r'C:\Users\danie\OneDrive\Desktop\#python\msedgedriver.exe')
driver.get('https://www.google.com/')
sleep(3)
driver.quit()
