from selenium import webdriver
from selenium.webdriver.common.by import By


def test_eight_components():
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    #driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    driver.get("http://localhost:63342/pythonProjectYoutbe/SoftwareTesting/index.html?_ijt=iufem6kfgskn7auovaiu6toq1l&_ij_reload=RELOAD_ON_SAVE")

    driver.find_element(By.CLASS_NAME, "information")

    driver.find_element(By.CSS_SELECTOR, "#fname")

    driver.find_element(By.ID, "lname")

    driver.find_element(By.NAME, "newsletter")

    driver.find_element(By.LINK_TEXT, "Selenium Official Page")

    driver.find_element(By.PARTIAL_LINK_TEXT, "Official Page")

    driver.find_element(By.TAG_NAME, "a")

    driver.find_element(By.XPATH, "//input[@value='f']")

test_eight_components()