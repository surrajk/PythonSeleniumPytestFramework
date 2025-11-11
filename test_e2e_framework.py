import json
import time

import pytest

from pageObjects.login import LoginPage
test_data_path = "/Users/surrajkhopkar/Library/CloudStorage/GoogleDrive-surraj.khopkar@gmail.com/My Drive/CodeBase/PythonSeleniumPytestFramework/data/test_e2e_framework.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage = LoginPage(driver)
    time.sleep(5)
    shop_page = loginPage.login(test_list_item["userName"],test_list_item["userPassword"])
    shop_page.add_products_to_carts(test_list_item["productName"])
    checkout = shop_page.goToCart()
    checkout.checkout()
    checkout.enter_delivery_address("ind")
    checkout.validate_order()





