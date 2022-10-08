from random import randrange

import pytest
from selenium.webdriver.common.by import By

import TestBase

# exel TS1
# Nazwa Scenariusza: Rejestracja nowego uzytkownika
# Opis przypadku testowego : Rejestrowanie użytkownika  z poprawnym adresem email
# Opis: Test sprawdza rejestracje nowego uzytkownika poprzez formularz rejestracyjny
# Warunki wstępne: Dostęp do strony http://automationpractice.com, górne menu strony, formularz rejestracyjny, email testowy użytkownika
#
from Pages.SignInPages import SignInPages


@pytest.mark.usefixtures("setup")
class TestRegistrationNewUser:



    @pytest.mark.run(order=1)
    def test_OpenPage(self):

        self.SignInPages = SignInPages(self.driver)

        print(f' Wejscie na strone http://automationpractice.com')
        #given

        #when
        self.SignInPages.get_pages()

        # then
        assert "My Store" in self.driver.title

    @pytest.mark.run(order=2)
    def test_ClickSigninButton(self):
        print(f' klikniecie w button "Sign in"')
        self.SignInPages = SignInPages(self.driver)

        # given

        # when
        self.SignInPages.click_button_signin()
        TestBase.waitForElementXPATH(self.driver, '//div[@class="cat-title"]')

        # then
        assert "http://automationpractice.com/index.php?controller=authentication&back=my-account" in str(self.driver.current_url)

    @pytest.mark.run(order=3)
    def test_SendKeyEmail(self):
        print(f' Wpisanie adresu email')
        # given
        randomnumber = str(randrange(100))
        adres_email = f'test-{randomnumber}@gmail.com'

        # when
        self.driver.find_element(by=By.XPATH, value='//input[@id="email_create"]').send_keys(adres_email)
        input = self.driver.find_element(by=By.XPATH, value='//input[@id="email_create"]')
        TestBase.click_move_to_element_with_offset(self.driver, input)
        color = input.value_of_css_property("color")

        # then
        assert 'rgba(53, 179, 63, 1)' == str(color)

    @pytest.mark.run(order=4)
    def test_CreateNewAccount(self):
        print(f' Utworzenie nowego konta usera')
        # given


        # when
        self.driver.find_element(by=By.XPATH, value='//button[@id="SubmitCreate"]').click()
        TestBase.waitForElementXPATH(self.driver, "//h1[contains(text(),'Create an account')]", 10)
        formName = self.driver.find_element(by=By.XPATH, value='//h1[@class="page-heading"]').text

        # then
        assert str(formName) == "CREATE AN ACCOUNT" or str(formName) == "Create an Create an account"
