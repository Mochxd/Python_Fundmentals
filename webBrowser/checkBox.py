from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkBoxDom = (By.XPATH,"//input[@type = 'checkbox']")
checkBoxes = driver.find_elements(*checkBoxDom)
print(len(checkBoxes))
for checkBox in checkBoxes:
    if checkBox.get_attribute("value") == "option2":
        checkBox.click()
        assert checkBox.is_selected()
        break

