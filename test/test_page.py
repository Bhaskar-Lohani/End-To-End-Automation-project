import time
from logging import getLogger
import pytest
from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login.login import loginpage
from pageobjects.PaymentDetails import Payments
from test.conftest import driver
from pageobjects.CheckOut import CheckOut
from pageobjects.MainPage import Mainpage
from pageobjects.Tops import Tops
from utilities.Baseclass import BaseClass


class TestHomepage(BaseClass):

    def test_women(self):
        # --- Login section ---
        login = loginpage(self.driver)
        login.getloginbutton().click()
        login.getusername().send_keys("bhaskar01@gmail.com")
        login.getpassword().send_keys("qwerty")
        login.getsubmit().click()



        self.driver.execute_script("window.scrollBy(0,400)")
        log = self.getLogger()

        mainPage = Mainpage(self.driver)
        mainPage.womanSection().click()
        mainPage.topSection().click()

        TopsPage = Tops(self.driver)
        womentops=TopsPage.gettop()

        log.info("getting all the tops name")
        for top in womentops:
            topName = top.find_element(By.XPATH, "./p").text

            log.info(topName)
            if topName == "Lace Top For Women":
                # if topName == "Blue Top":
                # if topName == "Fancy Green Top":
                self.scroll_to_element(top)
                add_to_cart_button = top.find_element(By.CSS_SELECTOR, "div div a.btn.btn-default.add-to-cart")
                self.wait_for_element(By.CSS_SELECTOR, "div div a.btn.btn-default.add-to-cart")
                add_to_cart_button.click()

                # Wait for the modal
                modal_title = self.wait_for_element(By.XPATH, "//h4[@class='modal-title w-100']")
                print(modal_title.text)
                assert ("Added!" in modal_title.text)


        viewCart = Tops(self.driver)
        viewCart.getviewcart().click()

        Checkout = CheckOut(self.driver)

        Checkout_details =Checkout.getdescription().text
        log.info("Getting description of selected top")
        log.info(Checkout_details)


        TotalAmount = CheckOut(self.driver)
        total_amount = TotalAmount.getamount().text
        log.info("getting details of tops price in cart ")
        log.info(total_amount)

        proceedtoCheckout = CheckOut(self.driver)
        proceedtoCheckout.proceedtocheckout().click()


        address = self.driver.find_element(By.XPATH, "//div/h2[text()='Address Details']").text
        assert "Address Details" in address

        placeOrder = CheckOut(self.driver)
        placeOrder.placeorder().click()

        testpaymet = Payments(self.driver)
        testpaymet.getnameoncard().send_keys("Mayank")
        testpaymet.getcardnumber().send_keys("225553366")
        testpaymet.getcvc().send_keys("124")
        testpaymet.getexpirationmonth().send_keys("12")
        testpaymet.getexpirationyear().send_keys("25")
        testpaymet.getpayandconfirmorder().click()

        orderconfirmation = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//p[contains(text(),'Congratulations! Your order has been confirmed!')]")))

        assert "Congratulations!" in orderconfirmation.text


