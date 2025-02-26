from selenium.webdriver.common.by import By


class CheckOut:


    description = (By.XPATH,"//tr/td[@class='cart_description']")
    amount  = (By.XPATH,"//tr/td[@class='cart_total']")
    proceed = (By.CSS_SELECTOR,"a[class='btn btn-default check_out']")
    place_order = (By.CSS_SELECTOR,"a[href='/payment']")

    def __init__(self,driver):
        self.driver = driver

    def getdescription(self):
        return self.driver.find_element(*CheckOut.description)

    def getamount(self):
        return self.driver.find_element(*CheckOut.amount)

    def proceedtocheckout(self):
        return self.driver.find_element(*CheckOut.proceed)

    def placeorder(self):
        return self.driver.find_element(*CheckOut.place_order)


    # item_detail = self.driver.find_element(By.XPATH, "//tr/td[@class='cart_description']").text
    # total_amount = self.driver.find_element(By.XPATH, "//tr/td[@class='cart_total']").text
    # self.driver.find_element(By.XPATH, "//div/a[@class='btn btn-default check_out']").click()