# Data Driven Method
import time
from logging import DEBUG

import pytest
import pytest_html.extras
from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from TestData.registrationData import registrationdata
from pageobjects import NewUserRegistration
from pageobjects.page import driver
from utilities.Baseclass import BaseClass
from pageobjects.NewUserRegistration import NewRegistration



class TestRegistration(BaseClass):


    def test_registration(self,getData):

        UserRegistration = NewRegistration(self.driver)
        UserRegistration.getsignlogin().click()
        UserRegistration.getUserNAme().send_keys(getData["Name"])
        UserRegistration.getUserEmail().send_keys(getData["Email"])
        UserRegistration.getsignbutton().click()
        UserRegistration.gettitle().click()
        UserRegistration.getpassword().send_keys(getData["password"])
        self.select_option_by_index(UserRegistration.selectDay(),(getData["Day"]))
        self.select_option_by_text(UserRegistration.selectMonth(),getData["Month"])
        self.select_option_by_value(UserRegistration.selectYear(),str(getData["Year"]))
        self.scroll()
        UserRegistration.selectcheckbox1().click()
        UserRegistration.selectcheckbox2().click()

        UserRegistration.getFirstName().send_keys(getData["Firstname"])
        UserRegistration.getLastName().send_keys(getData["Lastname"])
        UserRegistration.getaddress().send_keys(getData["Address"])
        UserRegistration.getaddress2().send_keys(getData["Address2"])
        UserRegistration.getCountry().send_keys(getData["Country"])
        UserRegistration.getState().send_keys(getData["State"])
        UserRegistration.getCity().send_keys(getData["City"])
        UserRegistration.getZipcode().send_keys(getData["Zipcode"])
        UserRegistration.getMobileNumber().send_keys(getData["MobileNumber"])
        self.scroll()
        UserRegistration.creataccount().click()
        alert_text = UserRegistration.Completeformfill().text


        assert ("ACCOUNT CREATED!" in alert_text)

        UserRegistration.getcontinue().click()
        UserRegistration.getLogin().click()
        Delete_Account= UserRegistration.getDelete().text

        assert ("ACCOUNT DELETED!" in Delete_Account)

        self.driver.refresh
    @pytest.fixture(params=registrationdata.test_registration_data)
    def getData(self,request):
        return request.param
