import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service

@pytest.fixture
def setup(browser):

    chrompath = Service('C:/chromedriver.exe')
    edgepath = Service('C:/msedgedriver.exe')

    if browser == 'chrome':
        driver = webdriver.Chrome(service=chrompath)
    elif browser == 'edge':
        driver = webdriver.Edge(service=edgepath)
    else:
        driver = webdriver.Chrome(service=chrompath)
    return driver

def pytest_addoption(parser):               #This will get the value from CLI/hooks
    parser.addoption('--browser', help="chrome for Chrome browser, edge for Edge browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')  #This will return the browser value to setup method


################### Pytest HTML report ################
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Darek'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

