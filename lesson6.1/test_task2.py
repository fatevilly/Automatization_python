from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from configuration import *

#chrome_browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_calculator_form(chrome_browser):
    chrome_browser.get(URL_2)
    delay = chrome_browser.find_element(By.CSS_SELECTOR, '#delay')
    delay.clear()
    delay.send_keys("45")

    chrome_browser.find_element(By.XPATH, '//span[text() = "7"]').click()
    chrome_browser.find_element(By.XPATH, '//span[text() = "+"]').click()
    chrome_browser.find_element(By.XPATH, '//span[text() = "8"]').click()
    chrome_browser.find_element(By.XPATH, '//span[text() = "="]').click()
    
    WebDriverWait(chrome_browser, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), "15"))
    result_text = chrome_browser.find_element(By.CLASS_NAME, "screen").text

    assert result_text == "15"
