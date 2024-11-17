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
Check = driver.find_element("id","content")
Check_text = Check.text
assert "Logout" in Check_text




