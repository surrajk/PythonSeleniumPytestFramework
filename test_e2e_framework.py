import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.ShopPage import ShopPage
from pageObjects.checkout_confirmation import Checkout_Confirmation
from pageObjects.login import LoginPage


def test_e2e(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage = LoginPage(driver)
    time.sleep(5)
    shop_page = loginPage.login()
    shop_page.add_products_to_carts(product_name="Blackberry")
    checkout = shop_page.goToCart()
    checkout.checkout()
    checkout.enter_delivery_address("ind")
    checkout.validate_order()





