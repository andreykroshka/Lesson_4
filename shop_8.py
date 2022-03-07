'''покупка товара'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
shop_btn = driver.find_element_by_id('menu-item-40').click()
driver.execute_script("window.scrollBy(0, 300);")
add_html5 = driver.find_element_by_css_selector('[data-product_id="182"]').click()
basket = driver.find_element_by_css_selector('[title="View Basket"]').click()
checkout_btn = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'checkout-button'))
)
checkout_btn.click()
first_name = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, 'billing_first_name'))
)
first_name.send_keys('Andrey')
last_name = driver.find_element_by_id('billing_last_name')
last_name.send_keys('Sakerin')
email = driver.find_element_by_id('billing_email')
email.send_keys('asdzxc123@mail.com')
phone = driver.find_element_by_id('billing_phone')
phone.send_keys('89997776655')
country = driver.find_element_by_css_selector('span[role="presentation"]').click()
placeholder = driver.find_element_by_class_name('select2-input')
placeholder.send_keys('Russia')
choose = driver.find_element_by_class_name('select2-match').click()
street = driver.find_element_by_name('billing_address_1')
street.send_keys('Lenina')
suite = driver.find_element_by_name('billing_address_2')
suite.send_keys('3')
city = driver.find_element_by_name('billing_city')
city.send_keys('Omsk')
state = driver.find_element_by_name('billing_state')
state.send_keys('Omskaya')
postcode = driver.find_element_by_name('billing_postcode')
postcode.send_keys('644050')
driver.execute_script("window.scrollBy(0, 600);")
check_radio = driver.find_element_by_id('payment_method_cheque').click()
place_btn = driver.find_element_by_id('place_order').click()
inscription = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'), 'Thank you. Your order has been received.')
)
text = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tr:nth-child(3) > td'), 'Check Payments')
)
driver.quit()


'''completed'''