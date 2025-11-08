import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.ShopPage import ShopPage
from pageObjects.login import LoginPage


def test_e2e(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage = LoginPage(driver)
    loginPage.login()
    time.sleep(5)
    shopPage = ShopPage(driver)
    shopPage.add_products_to_carts(product_name="Blackberry")
    shopPage.goToCart()
    driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
    driver.find_element(By.ID, "country").send_keys("ind")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT,"India").click()
    driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
    successText = driver.find_element(By.CLASS_NAME,"alert-success").text
    assert "Success! Thank you!" in successText
    driver.get_screenshot_as_file("screen.png")

