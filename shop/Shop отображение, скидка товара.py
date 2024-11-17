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
Book = driver.find_element("class name","post-169")
Book.click()
The_old_price = driver.find_element("class name","woocommerce-Price-amount")
The_old_price_text = The_old_price.text
assert "600" in The_old_price_text
New_price = driver.find_element("css selector",".price>ins>.woocommerce-Price-amount")
New_price_text = New_price.text
assert "450" in New_price_text
Book_btn = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME,"images")))
Book_btn = driver.find_element("class name","images")
Book_btn.click()
Close_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"pp_close")))
Close_btn = driver.find_element("class name","pp_close")
Close_btn.click()