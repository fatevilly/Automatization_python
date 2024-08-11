from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()
#FIREFOX
try:
    count = 0
    firefox.get("http://uitestingplayground.com/classattr")
    for _ in range(3):
        blue_button = firefox.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
        count = count + 1
        sleep(2)
        firefox.switch_to.alert.accept()
        print(count)

except Exception as ex:
    print(ex)
finally:
    firefox.quit()
