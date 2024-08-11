from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

#CHROME
try:
    count = 0
    chrome.get("http://uitestingplayground.com/classattr")
    for _ in range(3):
        blue_button = chrome.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
        count = count + 1
        sleep(2)
        chrome.switch_to.alert.accept()
        print(count)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()

