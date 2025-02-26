from selenium.webdriver.common.by import By


class Tops:
    def __init__(self,driver):
        self.driver = driver

    top = (By.XPATH,"//div[@class='productinfo text-center']")
    topName = (By.XPATH, "./p")
    viewcart = (By.CSS_SELECTOR, "div p:nth-child(2) a[href*='/view_cart")

    def gettop(self):
        return self.driver.find_elements(*Tops.top)
        # tops = self.driver.find_elements(By.XPATH, "//div[@class='productinfo text-center']")

    # def gettopname(self):
    #     return self.driver.find_element(*Tops.topName)


    def getviewcart(self):
        return self.driver.find_element(*Tops.viewcart)
# self.driver.find_element(By.CSS_SELECTOR, "div p:nth-child(2) a[href*='/view_cart']").click()