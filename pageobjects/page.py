import time
from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service_obj = Service(r'C:\Users\bhanu\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get("https://automationexercise.com/")
driver.execute_script("window.scrollBy(0,400)")
driver.find_element(By.XPATH,"//a[@href='#Women']").click()
driver.find_element(By.CSS_SELECTOR,"a[href*='/category_products/2']").click()


tops = driver.find_elements(By.XPATH,"//div[@class='productinfo text-center']")

for top in tops:
   topName =  top.find_element(By.XPATH, "./p").text
   print(topName)
   # if topName == "Lace Top For Women":
   # if topName == "Blue Top":

   if topName == "Fancy Green Top":
       driver.execute_script("window.scrollBy(0,400)")
       add_to_cart_button = top.find_element(By.CSS_SELECTOR, "div div a.btn.btn-default.add-to-cart")

       wait.until(EC.element_to_be_clickable(add_to_cart_button)).click()
       break # Exit loop after adding the item

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h4[class='modal-title w-100']")))

in_cart =  driver.find_element(By.CSS_SELECTOR,"h4[class='modal-title w-100']").text

print(in_cart)

assert ("Added!" in in_cart)

driver.find_element(By.CSS_SELECTOR,"div p:nth-child(2) a[href*='/view_cart']").click()
item_detail = driver.find_element(By.XPATH,"//tr/td[@class='cart_description']").text
print(item_detail)

total_amount = driver.find_element(By.XPATH,"//tr/td[@class='cart_total']").text

print(total_amount)

driver.find_element(By.XPATH,"//div/a[@class='btn btn-default check_out']").click()

address = driver.find_element(By.XPATH,"//div/h2[text()='Address Details']").text
assert "Address Details" in address