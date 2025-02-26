from selenium.webdriver.common.by import By

from test.conftest import driver


class Mainpage:
    def __init__(self,driver):
        self.driver = driver

    woman = (By.XPATH,"//a[@href='#Women']")
    tops =  (By.CSS_SELECTOR,"a[href*='/category_products/2']")


    def womanSection(self):
        return self.driver.find_element(*Mainpage.woman)
        # driver.find_element(By.XPATH, "//a[@href='#Women']").click()

    def topSection(self):
        return self.driver.find_element(*Mainpage.tops)
        # driver.find_element(By.CSS_SELECTOR,"a[href*='/category_products/2']").click()