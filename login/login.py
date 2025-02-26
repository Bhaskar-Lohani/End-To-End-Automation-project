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

class loginpage:
    def __init__(self,driver):
        self.driver = driver


    loginbutton = (By.XPATH,"//div/ul/li[4]")
    username = (By.XPATH,"//input[@data-qa='login-email']")
    password = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    submit = (By.CSS_SELECTOR,"button[data-qa='login-button']")
    logout = (By.XPATH,"//div/ul/li[4]")

    def getloginbutton(self):
        return self.driver.find_element(*loginpage.loginbutton)

    def getusername(self):
        return  self.driver.find_element(*loginpage.username)


    def getpassword(self):
        return self.driver.find_element(*loginpage.password)

    def getsubmit(self):
        return self.driver.find_element(*loginpage.submit)

    # def getlogout(self):
    #     return self.driver.find_element(*loginpage.logout)

# driver.find_element(By.XPATH,"//div/ul/li[4]").click()
#
#
#
# driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys("bhaskar01@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"input[data-qa='login-password']").send_keys("qwerty")
# driver.find_element(By.CSS_SELECTOR,"button[data-qa='login-button']").click()
#
# # driver.find_element(By.XPATH,"//div/ul/li[4]").click()
