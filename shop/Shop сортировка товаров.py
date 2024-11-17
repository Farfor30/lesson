from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.implicitly_wait(15)
MyAccount = driver.find_element("id","menu-item-50")
MyAccount.click()
Email = driver.find_element("id","username")
Email.send_keys("Piar20100@yandex.ru")
Password = driver.find_element("id","password")
Password.send_keys("FdnjvfnbpfwbzGbnth2024_11yjz,hm")
Login = driver.find_element("name","login")
Login.click()
Shop = driver.find_element("id","menu-item-40")
Shop.click()
sorting = driver.find_element("css selector","[value = 'menu_order']")
sorting_check = WebDriverWait(driver,2).until(EC.element_to_be_selected(sorting))
element = driver.find_element("class name","orderby")
select = Select(element)
select.select_by_value("price-desc")
element1 = driver.find_element("css selector","[value='price-desc']")
element2 = WebDriverWait(driver,2).until(EC.element_to_be_selected(element1))



