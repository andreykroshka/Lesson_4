'''количество товаров в категории'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
cat_html = driver.find_element_by_xpath('//*[@id="woocommerce_product_categories-2"]/ul/li[2]/a').click()
items_count = driver.find_elements_by_class_name("product")
if len(items_count) == 3:
    print("На странице 3 товара")
else:
    print("Ошибка. Количество товаров на странице: " + str(len(items_count)))
driver.quit()


'''completed'''