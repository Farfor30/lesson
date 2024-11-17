from selenium.webdriver.support.select import Select

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.implicitly_wait(15)
driver.execute_script("window.scrollBy(0,600);")
SeleniumRuby = driver.find_element("css selector","div.woocommerce .post-160>a>h3")
SeleniumRuby.click()
Rewiews = driver.find_element("class name","reviews_tab")
Rewiews.click()
Stars = driver.find_element("class name","star-5")
Stars.click()
Comment = driver.find_element("id","comment")
Comment.send_keys("Nice book!")
Name = driver.find_element("id","author")
Name.send_keys("Nik")
Email = driver.find_element("id","email")
Email.send_keys("Butt@ya.ru")
Submin = driver.find_element("id","submit")
Submin.click()