from selenium.webdriver.common.by import By

from test.conftest import setup


class NewRegistration:


    Signuplogin = (By.XPATH,"//div/ul/li[4]")
    Name = (By.XPATH,"//input[@data-qa='signup-name']")
    Email = (By.CSS_SELECTOR,"input[data-qa='signup-email']")
    SignupButton = (By.XPATH,"//button[@data-qa='signup-button']")
    title = (By.ID,"id_gender1")
    password=(By.ID,"password")
    Day = (By.ID,"days")
    Month = (By.NAME,"months")
    year = (By.ID,"years")
    checkbox1 = (By.ID,"newsletter")
    checkbox2 = (By.ID, "optin")
    Firstname = (By.ID,"first_name")
    Lastname = (By.NAME,"last_name")
    Address = (By.CSS_SELECTOR,"input[data-qa='address']")
    Address2 = (By.XPATH,"//input[@name='address2']")
    Country = (By.ID,"country")
    State = (By.ID,"state")
    City = (By.ID,"city")
    Zipcode = (By.XPATH,"//input[@data-qa='zipcode']")
    MobileNumber = (By.XPATH,"//input[@data-qa='mobile_number']")
    CreateAccount = (By.CSS_SELECTOR,"button[data-qa='create-account']")
    successmassage = (By.XPATH,"//div/h2[@class='title text-center']")
    Continue_text = (By.XPATH, "//div[@class='pull-right']")
    Login = (By.XPATH, "//div/ul/li[5]")
    Delete = (By.XPATH, "//div/h2[@data-qa='account-deleted']")

    def __init__(self,driver):
        self.driver = driver

    def getsignlogin(self):
        return  self.driver.find_element(*NewRegistration.Signuplogin)

    def getUserNAme(self):
        return self.driver.find_element(*NewRegistration.Name)

    def getUserEmail(self):
        return self.driver.find_element(*NewRegistration.Email)

    def getsignbutton(self):
        return self.driver.find_element(*NewRegistration.SignupButton)

    def gettitle(self):
        return self.driver.find_element(*NewRegistration.title)

    def getpassword(self):
        return self.driver.find_element(*NewRegistration.password)

    def selectDay(self):
        return self.driver.find_element(*NewRegistration.Day)

    def selectMonth(self):
        return self.driver.find_element(*NewRegistration.Month)

    def selectYear(self):
        return self.driver.find_element(*NewRegistration.year)

    def selectcheckbox1(self):
        return self.driver.find_element(*NewRegistration.checkbox1)

    def selectcheckbox2(self):
        return self.driver.find_element(*NewRegistration.checkbox2)

    def getFirstName(self):
        return  self.driver.find_element(*NewRegistration.Firstname)

    def getLastName(self):
        return self.driver.find_element(*NewRegistration.Lastname)

    def getaddress(self):
        return self.driver.find_element(*NewRegistration.Address)

    def getaddress2(self):
        return self.driver.find_element(*NewRegistration.Address2)

    def getCountry(self):
        return self.driver.find_element(*NewRegistration.Country)

    def getState(self):
        return self.driver.find_element(*NewRegistration.State)

    def getCity(self):
        return self.driver.find_element(*NewRegistration.City)

    def getZipcode(self):
        return self.driver.find_element(*NewRegistration.Zipcode)

    def getMobileNumber(self):
        return self.driver.find_element(*NewRegistration.MobileNumber)

    def creataccount(self):
        return self.driver.find_element(*NewRegistration.CreateAccount)

    def Completeformfill(self):
        return self.driver.find_element(*NewRegistration.successmassage)

    def getcontinue(self):
        return  self.driver.find_element(*NewRegistration.Continue_text)

    def getLogin(self):
        return  self.driver.find_element(*NewRegistration.Login)

    def getDelete(self):
        return self.driver.find_element(*NewRegistration.Delete)

