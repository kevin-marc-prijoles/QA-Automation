import os
from selenium import webdriver

os.environ['PATH'] += r"C:/selenium_driver"
driver = webdriver.Chrome()
driver.get("https://google.com")