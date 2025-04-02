import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

nameField = (By.NAME, "name")
emailField = (By.NAME,"email")
passwordField = (By.ID,"exampleInputPassword1")
iceCreamCheckBox = (By.ID,"exampleCheck1")
genderDropDownMenu = (By.ID, "exampleFormControlSelect1")
studentRadioButton = (By.ID, "inlineRadio1")



driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(*emailField).send_keys("momo@gmail.com")
driver.find_element(*passwordField).send_keys("momo@gmail.com")
driver.find_element(*iceCreamCheckBox).click()
Select(driver.find_element(*genderDropDownMenu)).select_by_visible_text("Female")
driver.find_element(*studentRadioButton).click()
time.sleep(2)
