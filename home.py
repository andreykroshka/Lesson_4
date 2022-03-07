'''добавление комментария'''

from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
selenium_ruby = driver.find_element_by_class_name('post-160').click()
reviews = driver.find_element_by_class_name('reviews_tab').click()
star_five = driver.find_element_by_class_name('reviews_tab').click()
your_review = driver.find_element_by_id('comment')
your_review.send_keys('Nice book!')
name = driver.find_element_by_id('author')
name.send_keys('Andrey')
email = driver.find_element_by_id('email')
email.send_keys('asdzxc123@mail.com')
submit = driver.find_element_by_id('submit').click()
driver.quit()

'''completed'''