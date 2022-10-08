from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

"""This class is the parent of all class"""
class BasePages:

    def __init__(self,driver):
        self.driver = driver


    def do_click_XPATH(self,by_locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, by_locator))).click()





