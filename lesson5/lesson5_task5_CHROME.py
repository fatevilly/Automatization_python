from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

#CHROME
try:
    chrome.get("http://the-internet.herokuapp.com/inputs")
    input_field = chrome.find_element(By.TAG_NAME, "input")
    input_field.send_keys("1000")
    sleep(2)
    input_field.clear()
    sleep(1)
    input_field.send_keys("999")
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()