#Framework by ggrek@gmail.com

from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def isElementPresentxPath(driver,locator:str):
    try:

        driver.find_element(by=By.XPATH, value=locator)

        return True
    except NoSuchElementException:
        return False

def areElementsPresentxPath(driver,locator:str):
    try:
        element = driver.find_element(by=By.XPATH, value=locator)
        if len(element) > 0:
            return True
    except InvalidSelectorException:
        return False

def MenuHoverOverTheFirstElementAndClickSecondElementXpath(driver,firstElemett,secondElement):
    we = driver.find_element(by=By.XPATH, value=firstElemett)
    ActionChains(driver).move_to_element(we).perform()
    waitForElementXPATH(driver,secondElement)
    driver.find_element(by=By.XPATH, value=secondElement).click()

def HoverOverTheFirstElementAndClickSecondElementXpath(driver,firstElement,secondElement,element:int):
    we = driver.find_element(by=By.XPATH, value=firstElement)
    ActionChains(driver).move_to_element(we).perform()
    waitForElementClickableXPATH(driver,secondElement)
    driver.find_elements(by=By.XPATH, value=secondElement)[element].click()


def click_move_to_element_with_offset(driver,locator):
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(locator, 150, 0)  # move 150 pixels to the right to access Help link
    action.click()
    action.perform()

def HoverOverElementXpath(driver,firstlocator,secondlocator):
    we = driver.find_element(by=By.XPATH, value=firstlocator)
    ActionChains(driver).move_to_element(we).perform()
    waitForElementClickableXPATH(driver, secondlocator)

def waitForElementXPATH(driver,xpatch:str,time = 10):

    wait = WebDriverWait(driver, time)
    wait.until(EC.presence_of_element_located((By.XPATH, xpatch)))

def waitForElementClickableXPATH(driver,xpatch:str,time = 10):

    wait = WebDriverWait(driver, time)
    wait.until(EC.element_to_be_clickable((By.XPATH, xpatch)))



def waitForElementXPATH_boolen(driver,xpatch:str,time = 10):
    try:
        wait = WebDriverWait(driver, time)
        wait.until(EC.presence_of_element_located((By.XPATH, xpatch)))
        return  True
    except:
        return False

def sliderRange(driver,xpath,x,y):
    element = driver.find_element(by=By.XPATH, value=xpath)
    action = ActionChains(driver)

    action.click_and_hold(element).move_by_offset(x, y).release().perform()

def waitForTextXPATH(driver,xpatch,text,time=10):
    wait = WebDriverWait(driver, time)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, xpatch),text))

