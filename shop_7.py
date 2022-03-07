'''работа в корзине'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
shop_btn = driver.find_element_by_id('menu-item-40').click()
driver.execute_script("window.scrollBy(0, 300);")
add_html5 = driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(3)
add_JSdata = driver.find_element_by_css_selector('[data-product_id="180"]').click()
basket = driver.find_element_by_css_selector('span.cartcontents').click()
time.sleep(3)
delete_JSdata = driver.find_element_by_css_selector('[data-product_id="182"]').click()
undo_btn = driver.find_element_by_css_selector('.woocommerce-message > a').click()
quantity_JS = driver.find_element_by_name('cart[045117b0e0a11a242b9765e79cbf113f][qty]')
quantity_JS.clear()
quantity_JS.send_keys('3')
update_btn = driver.find_element_by_name('update_cart').click()
quantity_book = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-quantity > div > input")
quantity_book_check = quantity_book.get_attribute("value")
assert quantity_book_check == '3'
time.sleep(3)
coupon_btn = driver.find_element_by_name('apply_coupon').click()
field = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-error'), 'Please enter a coupon code.')
)
driver.quit()


'''completed'''