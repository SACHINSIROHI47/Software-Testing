#pip install --upgrade selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Provide the path to the ChromeDriver executable
service = Service("chromedriver.exe")

# Initialize the driver using the Service object
driver = webdriver.Chrome(service=service)

# Open the Python website
driver.get("https://www.python.org")

# Locate the search bar using its ID
search_bar = driver.find_element(By.ID, "id-search-field")

