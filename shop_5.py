'''отображение, скидка товара'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
account_menu = driver.find_element_by_id('menu-item-50').click()
username = driver.find_element_by_id('username')
username.send_keys('asdzxc123@mail.com')
password = driver.find_element_by_id('password')
password.send_keys('Kroshka123')
login = driver.find_element_by_name("login").click()
shop_btn = driver.find_element_by_id('menu-item-40').click()
android_book = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]').click()
old_price = driver.find_element_by_css_selector('del > span')
old_price_get_text = old_price.text
assert old_price_get_text == '₹600.00'
new_price = driver.find_element_by_css_selector('ins > span')
new_price_get_text = new_price.text
assert new_price_get_text == '₹450.00'
book_title = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'images'))
)
book_title.click()
close_btn = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close'))
)
close_btn.click()
driver.quit()


'''completed'''