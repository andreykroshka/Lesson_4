'''проверка цены в корзине'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
shop_btn = driver.find_element_by_id('menu-item-40').click()
add_to_basket = driver.find_element_by_css_selector('[data-product_id="182"]').click()
basket = WebDriverWait(driver, 5).until(
     EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.cartcontents'), '1')
 )
amount = driver.find_element_by_css_selector('span.cartcontents')
amount_get_text = amount.text
assert amount_get_text == '1 Item'
price = driver.find_element_by_css_selector('a > span.amount')
price_get_text = price.text
assert price_get_text == "₹180.00"
amount.click()
subtotal = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, 'cart-subtotal'), '₹180.00')
)
total = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, 'order-total'), '₹189.00')
)
driver.quit()


'''completed'''