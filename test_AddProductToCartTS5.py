import pytest
from selenium.webdriver.common.by import By
import TestBase


# exel TS3
# Nazwa Scenariusza: Dodanie jednego towaru do koszyka
# Opis przypadku testowego :  Dodanie towaru do koszyka
# Opis: Test sprawdza dodanie towaru do koszyka
# Warunki wstępne: Dostęp do strony http://automationpractice.com, dostepny pasek menu, produkt istniejący w bazie


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

    @pytest.mark.run(order=2)
    def test_EnterMenu(self):
        print(f' Przejscie do kategoii "T-shirts""')
        # given

        # when
        TestBase.MenuHoverOverTheFirstElementAndClickSecondElementXpath(self.driver, "//a[@title='Women']", "//li[@class='sfHover']//a[@title='T-shirts']")
        test = TestBase.waitForElementXPATH_boolen(self.driver, "//span[contains(text(),'T-shirts')]")


        # then
        assert True == test
        assert 'http://automationpractice.com/index.php?id_category=5&controller=category' == str(self.driver.current_url)

    @pytest.mark.run(order=3)
    def test_TakeFirstProduct(self):
        print(f' Wybranie pierwszego produktu z listy""')
        # given

        # when

        TestBase.HoverOverTheFirstElementAndClickSecondElementXpath(self.driver, "//a[@class='product_img_link']", "//span[contains(text(),'Add to cart')]", 0)
        TestBase.waitForElementXPATH(self.driver, "//div[@class='layer_cart_product col-xs-12 col-md-6']//h2")
        TestBase.waitForElementClickableXPATH(self.driver, "//span[@title='Continue shopping']//span")
        test = self.driver.find_element(by=By.XPATH, value="//div[@class='layer_cart_product col-xs-12 col-md-6']//h2").text

        # then
        assert "Product successfully added to your shopping cart" == str(test)


