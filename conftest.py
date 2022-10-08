import pytest
from selenium import webdriver
from Config.config import TestData



@pytest.fixture(scope="class")
def setup(request):
    print("start chrome driver")
    driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH) #if not added in PATH
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()

    #SELENIUM 4
    # from selenium import webdriver
    # from selenium.webdriver.chrome.service import Service as ChromeService
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option("useAutomationExtension", False)
    # service = ChromeService(executable_path=CHROMEDRIVER_PATH)
    # driver = webdriver.Chrome(service=service, options=options)
