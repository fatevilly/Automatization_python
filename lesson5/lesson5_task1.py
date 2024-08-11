from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
    firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")
#button_locator = '//button[text()="Add Element"]'
#button_locator = '//button[text()="Delete"]'
    for _ in range(5):
        add_button = chrome.find_element(
            By.XPATH, '//button[text()="Add Element"]').click()
        add_button = firefox.find_element(
            By.XPATH, '//button[text()="Add Element"]').click()

        sleep(1)

        chrome_delete_buttons = chrome.find_elements(
            "xpath", '//button[text()="Delete"]')
        firefox_delete_buttons = firefox.find_elements(
            "xpath", '//button[text()="Delete"]')
    
    print(
        f"Размер списка кнопок Delete в Chrome: {len(chrome_delete_buttons)}")
    print(
        f"Размер списка кнопок Delete в Firefox: {len(firefox_delete_buttons)}")

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()