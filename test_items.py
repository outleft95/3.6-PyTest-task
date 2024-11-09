import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_present_basket_button(browser):
    browser.get(link) 
    time.sleep(10)
    element = browser.find_elements(By.CSS_SELECTOR, "button.btn-primary")
    assert element, 'no element'