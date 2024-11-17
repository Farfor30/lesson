from selenium import webdriver

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
HTML = driver.find_element("class name","cat-item-19")
HTML.click()
Cout = driver.find_element("css selector","li.cat-item-19>span")
Cout_text = Cout.text
assert  Cout_text == "(3)"



