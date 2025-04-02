import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_default_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    return options

chrome_options = get_default_chrome_options()
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
dropDownField = (By.ID,"autosuggest")
countriesDom = (By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

driver.find_element(*dropDownField).send_keys("Eg")
time.sleep(2)
countries = driver.find_elements(*countriesDom)
print(len(countries))
for country in countries:
    if country.text == "Egypt":
        country.click()
        break
assert driver.find_element(*dropDownField).get_attribute("value") == "Egypt"