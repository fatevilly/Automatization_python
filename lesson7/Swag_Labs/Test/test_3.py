import pytest
from lesson7.Swag_Labs.Pages.Shop import BasePage
from lesson7.Swag_Labs.Pages.Shop import LoginPage
from lesson7.Swag_Labs.Pages.Shop import ProductsPage
from lesson7.Swag_Labs.Pages.Shop import CheckoutPage
from lesson7.Swag_Labs.Pages.Shop import PersonalInfoPage
from lesson7.Swag_Labs.Pages.Shop import OverviewPage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@pytest.fixture
def browser():
    """
    Фикстура для создания и закрытия экземпляра веб-драйвера.
    :return: объект веб-драйвера Selenium.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_complete_purchase(browser):
    """
    Тестирует процесс покупки товаров на сайте.
    """
    login_page = LoginPage(browser)
    products_page = ProductsPage(browser)
    checkout_page = CheckoutPage(browser)
    personal_info_page = PersonalInfoPage(browser)
    overview_page = OverviewPage(browser)

    login_page.open()
    login_page.login()

    products_page.add_products_to_cart("sauce-labs-backpack", "sauce-labs-bolt-t-shirt", "sauce-labs-onesie")
    products_page.go_to_cart()

    checkout_page.proceed_to_checkout()

    personal_info_page.fill_personal_info("Evgeny", "Gusinets", "246006")

    total_amount = overview_page.get_total_amount()
    assert total_amount == "58.29", f"Expected '58.29', but got {total_amount}"

    overview_page.complete_purchase()

    