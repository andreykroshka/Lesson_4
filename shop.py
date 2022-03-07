'''логин в систему'''


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
logout = WebDriverWait(driver, 5 ).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,".woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a")))
driver.quit()


'''Completed'''