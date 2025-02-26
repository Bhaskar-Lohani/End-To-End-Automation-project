from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from utilities.Baseclass import BaseClass
from login.login import loginpage, driver


class TestLogin(BaseClass):




    def test_loginpage(self):
        clicklogin = loginpage(self.driver)
        clicklogin.getloginbutton().click()
        clicklogin.getusername().send_keys("bhaskar01@gmail.com")
        clicklogin.getpassword().send_keys("qwerty")
        clicklogin.getsubmit().click()
        clicklogin.getlogout().click()


    def test_invalidcredentials(self):
        clicklogin = loginpage(self.driver)
        clicklogin.getloginbutton().click()
        clicklogin.getusername().send_keys("Ankitjoshi@gmail.com")
        clicklogin.getpassword().send_keys("asdfg")
        clicklogin.getsubmit().click()
        
        error_message = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(
            (By.XPATH,"//p[contains(text(),'Your email or password is incorrect!')]")))
        assert "Your email or password is incorrect!" in error_message.text,"Invalid Username or Password"

