from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")
    
confirm_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
driver.implicitly_wait(5)

new_button = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
driver.implicitly_wait(5)
print(new_button)

driver.quit()

    