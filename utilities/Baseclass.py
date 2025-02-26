import inspect
import logging
from tkinter.tix import Select

import pytest
from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from test.conftest import driver

@pytest.mark.usefixtures("setup")

class BaseClass():

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    # In the BaseClass or Utility Class
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll(self):
        self.driver.execute_script("window.scrollBy(0,600)")

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))
        # return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h4[class='modal-title w-100']")))


    def select_option_by_value(self,locator,value):
        optionselect = Select(locator)
        optionselect.select_by_value(value)

    def select_option_by_text(self,locator,text):
        optionselect = Select(locator)
        optionselect.select_by_visible_text(text)

    def select_option_by_index(self,locator,index):
        optionselect = Select(locator)
        optionselect.select_by_index(index)