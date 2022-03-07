'''отображение страницы товара'''


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
html_5_book = driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]').click()
book_title = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "product_title"), "HTML5 Forms"))
driver.quit()


'''completed'''