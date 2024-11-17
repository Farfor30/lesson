from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.implicitly_wait(15)
MyAccount = driver.find_element("id","menu-item-50")
MyAccount.click()
EmailAddress = driver.find_element("id","reg_email")
EmailAddress.send_keys("Piar20100@yandex.ru")
Password = driver.find_element("id","reg_password")
Password.send_keys("FdnjvfnbpfwbzGbnth2024_11yjz,hm")
Register = driver.find_element("name","register")
Register.click()

