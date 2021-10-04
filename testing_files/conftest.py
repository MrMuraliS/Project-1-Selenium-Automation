import pytest
from selenium import webdriver
from Data.DataToTest import TestData


@pytest.fixture(scope='class')
def setUp(request):
    driver = webdriver.Chrome('C:\\Users\\Murali S\\Downloads\\chromedriver_win32\\chromedriver.exe')
    driver.maximize_window()
    driver.get('https://login.salesforce.com/?locale=eu')
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(params=TestData)
def Data(request):
    return request.param

