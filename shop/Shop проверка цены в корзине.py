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
Basked_add = driver.find_element("css selector","[data-product_id='182']")
Basked_add.click()
time.sleep(3)
Item = driver.find_element("class name","wpmenucart-contents")
Item_text = Item.text
assert "1 item" and "₹180.00" in Item_text
Basked = driver.find_element("class name","wpmenucart-contents")
Basked.click()
Subtotal = WebDriverWait(driver,5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[data-title='Subtotal']>span"),"180.00"))
Total = WebDriverWait(driver,5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".order-total .woocommerce-Price-amount"),"183.60"))


