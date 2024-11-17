from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import  time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.implicitly_wait(15)
Shop = driver.find_element("id","menu-item-40")
Shop.click()
driver.execute_script("window.scrollBy(0,300);")
HTML5 = driver.find_element("css selector","[data-product_id='182']")
HTML5.click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,600);")
JS_Data = driver.find_element("css selector","[data-product_id='180']")
JS_Data.click()
time.sleep(3)
Basked = driver.find_element("class name","wpmenucart-contents")
Basked.click()
time.sleep(3)
Сross = driver.find_element("class name","remove")
Сross.click()
time.sleep(3)
Undo = driver.find_element("link text","Undo?")
Undo.click()
Quantity = driver.find_element("class name","qty")
Quantity.clear()
Quantity.send_keys("3")
Update_basket = driver.find_element("name","update_cart")
Update_basket.click()
Quantity_JS = Quantity.get_attribute("value")
assert Quantity_JS =="3"
time.sleep(3)
Apply = driver.find_element("name","apply_coupon")
Apply.click()
Message = WebDriverWait(driver,5).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"woocommerce-error"),"Please enter a coupon code."))
