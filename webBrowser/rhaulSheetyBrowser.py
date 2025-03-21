import time

from selenium import webdriver
from selenium.webdriver.common.by import By

email = (By.NAME,"email")
password = (By.ID,"exampleInputPassword1")
iceCreamCheckBox = (By.ID,"exampleCheck1")
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(*email).send_keys("momo@gmail.com")
driver.find_element(*password).send_keys("momo@gmail.com")
driver.find_element(*iceCreamCheckBox).click()
time.sleep(2)
