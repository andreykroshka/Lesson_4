'''регистрация аккаунта'''
import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
account_menu = driver.find_element_by_id('menu-item-50').click()
emailadress = driver.find_element_by_id('reg_email')
emailadress.send_keys('asdzxc123@mail.com')
password = driver.find_element_by_id('reg_password')
password.send_keys('Kroshka123')
register = driver.find_element_by_name("register").click()
driver.quit()


'''completed'''