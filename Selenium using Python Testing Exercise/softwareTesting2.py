from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("chromedriver.exe")
# Initialize the driver using the Service object
driver = webdriver.Chrome(service=service)
# driver.get("https://www.python.org")
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
title = driver.title
print("Driver Title Name is = ",title)

#https://www.selenium.dev/documentation/webdriver/getting_started/install_library/











