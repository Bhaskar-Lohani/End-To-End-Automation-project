import time
import pytest
from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = None
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):


    global driver
    browser_name = request.config.getoption("browser_name")
    print(browser_name)
    if browser_name == "chrome":
         service_obj = Service(r'C:\Users\bhanu\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe')
         driver = webdriver.Chrome(service=service_obj)

    elif browser_name == "edge":
        service_obj = Service(r'C:\Users\bhanu\Desktop\edgedriver_win64\msedgedriver.exe')
        driver = webdriver.Edge(service=service_obj)

    driver.implicitly_wait(5)
    driver.get("https://automationexercise.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)