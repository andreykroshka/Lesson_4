'''сортировка товаров'''


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
default = WebDriverWait(driver, 10).until(
    EC.element_located_to_be_selected((By.CSS_SELECTOR,'.orderby [value="menu_order"]')) )
high_to_low = driver.find_element_by_class_name("orderby")
select = Select(high_to_low)
select.select_by_value("price-desc")
default = WebDriverWait(driver, 10).until(
    EC.element_located_to_be_selected((By.CSS_SELECTOR,'.orderby [value="price-desc"]')) )
driver.quit()


'''completed'''