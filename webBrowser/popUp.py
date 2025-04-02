import time

from selenium import webdriver
from selenium.webdriver.common.by import By

name = (By.NAME, "enter-name")
alertButton = (By.ID, "alertbtn")

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(*name).send_keys("Mohamed Mostafa")
driver.find_element(*alertButton).click()
time.sleep(2)
alert = driver.switch_to.alert
assert alert.text.__contains__("Mohamed Mostafa")
print(alert.text)
alert.accept()


