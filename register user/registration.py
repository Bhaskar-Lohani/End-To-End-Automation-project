import time
from logging import DEBUG

from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

service_obj = Service(r'C:\Users\bhanu\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)


driver.get("https://automationexercise.com/")
driver.find_element(By.XPATH,"//div/ul/li[4]").click()
driver.find_element(By.NAME,"name").send_keys("bhanu")
driver.find_element(By.CSS_SELECTOR,"input[data-qa='signup-email']").send_keys("bhaskar02@gmail.com")
driver.find_element(By.XPATH,"//button[@data-qa='signup-button']").click()
time.sleep(3)

# CheckBox

driver.find_element(By.ID,"id_gender1").click()

# # static dropdown

Birthday = Select(driver.find_element(By.ID,"days"))
Birthday.select_by_index(11)


BirthMonth = Select(driver.find_element(By.NAME,"months"))
BirthMonth.select_by_visible_text("March")

Birthyear = Select(driver.find_element(By.ID,"years"))
Birthyear.select_by_value('1999')

Country = Select(driver.find_element(By.ID,"country"))
Country.select_by_value("India")


driver.find_element(By.ID,"password").send_keys("qwerty")



driver.execute_script("window.scrollBy(0,200)")
Checkboxs = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(Checkboxs))

for Checkbox in Checkboxs:
    if Checkbox.get_attribute("id") ==  "optin":
        Checkbox.click()
        # assert Checkbox.is_selected()



driver.find_element(By.ID,"first_name").send_keys("Bhaskar")
driver.find_element(By.NAME,"last_name").send_keys("last_name")
driver.find_element(By.ID,"company").send_keys("Automation Hub")

driver.find_element(By.CSS_SELECTOR,"input[data-qa='address']").send_keys("Mayur Vihar")
driver.find_element(By.XPATH,"//input[@name='address2']").send_keys("Delhi")

driver.find_element(By.ID,"state").send_keys("Delhi")
driver.find_element(By.ID,"city").send_keys("MayurVihar")
driver.find_element(By.XPATH,"//input[@data-qa='zipcode']").send_keys("252627")
driver.find_element(By.XPATH,"//input[@data-qa='mobile_number']").send_keys("954758975")

driver.execute_script("window.scrollBy(0,700)")
driver.find_element(By.CSS_SELECTOR,"button[data-qa='create-account']").click()

time.sleep(3)

Completeformfill =driver.find_element(By.XPATH,"//div/h2[@class='title text-center'] ").text
# print(Completeformfill)
assert ("ACCOUNT CREATED!" in Completeformfill)

driver.find_element(By.XPATH,"//div[@class='pull-right']").click()

driver.find_element(By.XPATH,"//div/ul/li[5]").click()

DeleteAccount = driver.find_element(By.XPATH,"//div/h2[@data-qa='account-deleted']").text
print(DeleteAccount)
assert ("ACCOUNT DELETED!" in DeleteAccount)



