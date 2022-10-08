import pytest
from selenium.webdriver.common.by import By
import TestBase


# exel TS3
# Nazwa Scenariusza: Pierwsze logowanie uzytkownika do panelu
# Opis przypadku testowego : Logowanie użytkownikiem zarejestrowanym  w systemie
# Opis: Test sprawdza logowanie uzytownika do systemu
# Warunki wstępne: Dostęp do strony http://automationpractice.com/index.php?controller=authentication&back=my-account,
# formularz logowania, utworzony email w systemie, email nie zarejestrowany w systemie


@pytest.mark.usefixtures("setup")
class TestLoginNewUser:

    @pytest.mark.run(order=1)
    def test_OpenPage(self):
        print(f' Wejscie na strone http://automationpractice.com')
        #given

        #when
        self.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        # then
        assert "Login - My Store" in self.driver.title

    @pytest.mark.run(order=2)
    def test_EmailEnter(self):
        print(f' Wpisanie adresu email w pole input Email address')

        # given
        adres_email = 'test5666@gmail.com'


        # when
        self.driver.find_element(by=By.XPATH, value="//input[@id='email']").send_keys(adres_email)
        input = self.driver.find_element(by=By.XPATH, value="//input[@id='email']")
        TestBase.click_move_to_element_with_offset(self.driver, input)
        color = input.value_of_css_property("color")

        # then
        assert 'rgba(53, 179, 63, 1)' == str(color)

    @pytest.mark.run(order=3)
    def test_PasswordEnter(self):
        print(f' Wpisanie adresu email w pole input Email address')

        # given
        password = '1234567'

        # when
        self.driver.find_element(by=By.XPATH, value="//input[@id='passwd']").send_keys(password)
        self.driver.find_element(by=By.XPATH, value="//span[contains(.,'Sign in')]").click()
        TestBase.waitForElementXPATH(self.driver, "//body[@id='my-account']", 10)

        # then
        assert "My account - My Store" in self.driver.title

