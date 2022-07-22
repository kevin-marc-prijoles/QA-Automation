import os
from selenium import webdriver

os.environ['PATH'] += r"C:/selenium_driver"
driver = webdriver.Chrome()

#This only goes to google.com nothing fancy lol
driver.get("https://google.com")