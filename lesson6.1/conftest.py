from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

import pytest
from selenium import webdriver

@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
