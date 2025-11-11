import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sort(browserInstance):
    driver = browserInstance
    time.sleep(5)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "sort-icon").click()
    time.sleep(5)
    veggie_list = []
    veggie_webelements = driver.find_elements(By.XPATH, "//tr/td[1]")
    for element in veggie_webelements:
        veggie_list.append(element.text)

    new_list = veggie_list.copy()
    veggie_list.sort()

    print(veggie_list)
    print(new_list)
    assert new_list == veggie_list
