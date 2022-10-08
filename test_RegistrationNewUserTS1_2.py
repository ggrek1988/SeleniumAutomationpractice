import pytest
from selenium.webdriver.common.by import By
import TestBase


# exel TS1
# Nazwa Scenariusza: Rejestracja nowego uzytkownika
# Opis przypadku testowego : Rejestrowanie użytkownika z nieprawidłowym adresem email
# Opis: Test sprawdza rejestracje nowego uzytkownika poprzez formularz rejestracyjny
# Warunki wstępne: Dostęp do strony http://automationpractice.com, górne menu strony, formularz rejestracyjny, Niepoprawny adres email
#


@pytest.mark.usefixtures("setup")
class TestRegistrationNewUser:

    @pytest.mark.run(order=1)
    def test_OpenPage(self):
        print(f' Wejscie na strone http://automationpractice.com')
        #given

        #when
        self.driver.get("http://automationpractice.com")
        # then
        assert "My Store" in self.driver.title

    @pytest.mark.run(order=2)
    def test_ClickSigninButton(self):
        print(f' klikniecie w button "Sign in"')
        # given

        # when
        self.driver.find_element(by=By.XPATH, value="//a[@class='login']").click()
        TestBase.waitForElementXPATH(self.driver, '//div[@class="cat-title"]')

        # then
        assert "http://automationpractice.com/index.php?controller=authentication&back=my-account" in str(self.driver.current_url)

    @pytest.mark.run(order=3)
    def test_SendKeyEmail(self):
        print(f' Wpisanie adresu email')
        # given
        adres_email = f'test@gmail'

        # when
        inputemail = self.driver.find_element(by=By.XPATH, value='//input[@id="email_create"]').send_keys(adres_email)
        input = self.driver.find_element(by=By.XPATH, value='//input[@id="email_create"]')
        TestBase.click_move_to_element_with_offset(self.driver, input)
        color = input.value_of_css_property("color")

        # then
        assert 'rgba(241, 51, 64, 1)' == str(color)

    @pytest.mark.run(order=4)
    def test_CreateNewAccount(self):
        print(f' Utworzenie nowego konta usera')
        # given

        # when
        self.driver.find_element(by=By.XPATH, value='//button[@id="SubmitCreate"]').click()
        errorelement = TestBase.waitForElementXPATH_boolen(self.driver, "//li[contains(text(),'Invalid email address.')]", 10)

        if errorelement:
            error = True
        else:
            error = False

        # then
        assert True == error


