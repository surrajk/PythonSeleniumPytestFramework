from selenium.webdriver.common.by import By

from pageObjects.ShopPage import ShopPage


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")


    def login(self):
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.password_input).send_keys("learning")
        self.driver.find_element(By.ID, "signInBtn").click()
        shop_page = ShopPage(self.driver)
        return shop_page