import pytest
from selenium.webdriver.common.by import By
import TestBase


# exel TS3
# Nazwa Scenariusza: Wyszukiwanie towarów
# Opis przypadku testowego : Wyszukanie nie istniejącego towaru
# Opis: Test sprawdza uzycie wyszukiwarki towarów
# Warunki wstępne: Dostęp do strony http://automationpractice.com, pole wyszukiwarki, produkt istniejący w bazie, produkt którego nie ma w bazie


@pytest.mark.usefixtures("setup")
class TestLoginNewUser:

    @pytest.mark.run(order=1)
    def test_OpenPage(self):
        print(f' Wejscie na strone http://automationpractice.com')
        # given

        # when
        self.driver.get("http://automationpractice.com")

        # then
        assert "My Store" in self.driver.title

    @pytest.mark.run(order=1)
    def test_EnterNameProductAndSearch(self):
        print(f' Uzycie wyszukiwarki po wpisaniu towaru')
        # given
        nameProduct = 'Nowy towar'

        # when
        self.driver.find_element(by=By.XPATH, value="//input[@id='search_query_top']").send_keys(nameProduct)
        self.driver.find_element(by=By.XPATH, value="//button[@name='submit_search']").click()

        searchproduct = TestBase.waitForElementXPATH_boolen(self.driver,
                                                           "//p[contains(text(),'No results were found for your search')]", 10)
        if searchproduct:
            error = True
        else:
            error = False

        # then
        assert True == error


