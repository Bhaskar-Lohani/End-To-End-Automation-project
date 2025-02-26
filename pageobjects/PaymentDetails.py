from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Payments:
    NameonCard = (By.NAME,"name_on_card")
    CardNumber = (By.NAME,"card_number")
    CVC = (By.CSS_SELECTOR,"input[class='form-control card-cvc']")
    ExpirationMonth = (By.CSS_SELECTOR,"input[class='form-control card-expiry-month']")
    ExpirationYear = (By.XPATH,"//input[@name='expiry_year']")
    PayandConfirmOrder = (By.ID,"submit")

    def __init__(self,driver):
        self.driver = driver

    def getnameoncard(self):
        return self.driver.find_element(*Payments.NameonCard)

    def getcardnumber(self):
        return self.driver.find_element(*Payments.CardNumber)

    def getcvc(self):
        return self.driver.find_element(*Payments.CVC)

    def getexpirationmonth(self):
        return self.driver.find_element(*Payments.ExpirationMonth)

    def getexpirationyear(self):
        return self.driver.find_element(*Payments.ExpirationYear)

    def getpayandconfirmorder(self):
        return self.driver.find_element(*Payments.PayandConfirmOrder)




