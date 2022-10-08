from Config.config import TestData
from Pages.BasePages import BasePages


class SignInPages(BasePages):

    BUTTONSIGNIN = "//a[@class='login']"



    def __init__(self,driver):
        super().__init__(driver)


    def get_pages(self):
        self.driver.get(TestData.BASE_URL_SIGNIN)


    def click_button_signin(self):
        self.do_click_XPATH(self.BUTTONSIGNIN)

    def click_button_SubmitCreate(self):
        self.do_click_XPATH(self.BUTTONSIGNIN)




