import time

from selenium.webdriver.common.by import By

from pageObjects.checkout_confirmation import Checkout_Confirmation


class ShopPage:
    def __init__(self,driver):
        self.driver = driver
        self.shop_link = (By.CLASS_NAME, "nav-link")
        self.product_carts = (By.XPATH, "//div[@class='card h-100']")
        self.cart_link = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def add_products_to_carts(self, product_name):
        self.driver.find_element(*self.shop_link).click()
        time.sleep(5)
        products = self.driver.find_elements(*self.product_carts)

        # chaining operation
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
                time.sleep(5)

    def goToCart(self):
        self.driver.find_element(*self.cart_link).click()
        checkoutConfirmation = Checkout_Confirmation(self.driver)
        return checkoutConfirmation



