from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

#CHROME
try:
    chrome.get("http://the-internet.herokuapp.com/login")
    username_field = chrome.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    sleep(2)
    password_field = chrome.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    sleep(2)
    click_button = chrome.find_element(By.CLASS_NAME, "radius").click()
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()