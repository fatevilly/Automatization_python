from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

sleep(5)

username = driver.find_element(By.CSS_SELECTOR, '[name="user-name"]')
username.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
password.send_keys("secret_sauce")

login_button = driver.find_element(By.CSS_SELECTOR, '[name="login-button"]').click()
driver.implicitly_wait(60)

add_backpack = driver.find_element(By.CSS_SELECTOR, '[name="add-to-cart-sauce-labs-backpack"]').click()
add_t_shirt = driver.find_element(By.CSS_SELECTOR, '[name="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
add_t_shirt = driver.find_element(By.CSS_SELECTOR, '[name="add-to-cart-sauce-labs-onesie"]').click()

shopping_cart = driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
checkout_button = driver.find_element(By.CSS_SELECTOR, '[name="checkout"]').click()

first_name = driver.find_element(By.CSS_SELECTOR, '[name="firstName"]')
first_name.send_keys("Вера")
last_name = driver.find_element(By.CSS_SELECTOR, '[name="lastName"]')
last_name.send_keys("Фатеева")
postal_code = driver.find_element(By.CSS_SELECTOR, '[name="postalCode"]')
postal_code.send_keys("454077")

sleep(5)

continue_button = driver.find_element(By.CSS_SELECTOR, '[name="continue"]').click()

sleep(5)

total_label = driver.find_element(By.CSS_SELECTOR, "[data-test=total-label]").text

def test_shopping():
    assert total_label == "Total: $58.29"

driver.quit()


