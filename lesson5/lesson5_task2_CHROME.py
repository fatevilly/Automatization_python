from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

#CHROME
try:
    count = 0
    chrome.get("http://uitestingplayground.com/dynamicid")

    for _ in range(3):
        chrome.get("http://uitestingplayground.com/dynamicid")
        add_button = chrome.find_element(
            By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
        count = count + 1
        sleep(2)
        print(count)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()