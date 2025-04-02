import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

searchBarField = (By.CSS_SELECTOR,".search-keyword")
productsAddToCartButton = (By.XPATH, "//div[@class='product-action']/button")
cartImage = (By.CSS_SELECTOR, ".cart-icon")
processedToCheckoutButton = (By.XPATH,"//button[text()='PROCEED TO CHECKOUT']")
promoCodeField = (By.CSS_SELECTOR, ".promoCode")
applyPromoCodeButton = (By.CSS_SELECTOR, ".promoBtn")
promoCodeMessage = (By.CSS_SELECTOR, ".promoInfo")
cartCount = (By.CSS_SELECTOR,".cart-count")

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(*searchBarField).send_keys("ber")
time.sleep(2)
productsAddToCartButtons = driver.find_elements(*productsAddToCartButton)
print(len(productsAddToCartButtons))
for button in productsAddToCartButtons:
        button.click()

print(driver.find_element(*cartCount).text)
driver.find_element(*cartImage).click()
driver.find_element(*processedToCheckoutButton).click()
time.sleep(2)
driver.find_element(*promoCodeField).send_keys("rahulshettyacademy")
driver.find_element(*applyPromoCodeButton).click()
wait.until(expected_conditions.presence_of_element_located(promoCodeMessage))

print(driver.find_element(*promoCodeMessage).text)
assert driver.find_element(*promoCodeMessage).text == "Code applied ..!"
