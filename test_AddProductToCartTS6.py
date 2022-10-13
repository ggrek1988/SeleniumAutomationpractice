import pytest
from selenium.webdriver.common.by import By

import TestBase
from selenium.webdriver.support.ui import Select


# exel TS3
# Nazwa Scenariusza: Dodanie jednego towaru do koszyka
# Opis przypadku testowego :  Dodanie towaru do koszyka
# Opis: Test sprawdza dodanie towaru do koszyka z kategorii Dress, wyszukując po kategorii i sortując listę towarów
# Warunki wstępne: Dostęp do strony http://automationpractice.com, dostępna menu, produkt istniejący w bazie


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
    def test_OpenPageDress(self):
        print(f' W menu odszukujemu i klikamy w Dress --> Casual Dresses')
        # given
    
        # when
        we = self.driver.find_elements(by=By.XPATH, value='//a[@title="Dresses"]')[0]
        mouseOverScript = "return arguments[0].click();"
        self.driver.execute_script(mouseOverScript, we)
        self.driver.find_element(by=By.XPATH,
                                 value="//div[@class='block_content']//ul[@class='tree dynamized']//a[contains(text(),'Casual Dresses')]").click()
    
        # then
        assert "http://automationpractice.com/index.php?id_category=9&controller=category" in str(self.driver.current_url)

    @pytest.mark.run(order=3)
    def test_CheckOptionsCatalog(self):
        print(f' W sekcji Catalog zaznaczamy Styles, Size,Price, oraz sortujemy dane "Sort by"')
        
        # given

        # when
        self.driver.find_element(by=By.XPATH,value="//input[@name='layered_id_attribute_group_1']").click()

        TestBase.waitForElementXPATH(self.driver, "//li[contains(.,'Size: S')]")
        self.driver.find_element(by=By.XPATH, value="//input[@name='layered_id_feature_13']").click()

        TestBase.waitForElementXPATH(self.driver, "//li[contains(.,'Styles: Girly')]")
        TestBase.sliderRange(self.driver, "//div[@id='layered_price_slider']/a[1]", 45, 5)


        select = Select(self.driver.find_element(by=By.XPATH, value="//select[@id='selectProductSort']"))
        select.select_by_visible_text('Product Name: A to Z')

        TestBase.waitForElementXPATH(self.driver, "//li[contains(.,'Styles: Girly')]")

        if TestBase.isElementPresentxPath(self.driver, "//li[contains(.,'Size: S')]"):
            assertelement1 = len(self.driver.find_elements(by=By.XPATH, value="//li[contains(.,'Size: S')]"))
        if TestBase.isElementPresentxPath(self.driver, "//li[contains(.,'Styles: Girly')]"):
            assertelement2 = len(self.driver.find_elements(by=By.XPATH, value="//li[contains(.,'Styles: Girly')]"))

        # then
        assert assertelement1 == 1
        assert assertelement2 == 1

    @pytest.mark.run(order=4)
    def test_TakeFirstProduct(self):
        print(f' Wybranie pierwszego produktu z listy""')
        # given

        # when

        TestBase.HoverOverTheFirstElementAndClickSecondElementXpath(self.driver, "//a[@class='product_img_link']",
                                                                        "//span[contains(text(),'Add to cart')]", 0)
        TestBase.waitForElementXPATH(self.driver, "//div[@class='layer_cart_product col-xs-12 col-md-6']//h2")
        TestBase.waitForElementClickableXPATH(self.driver, "//span[@title='Continue shopping']//span")

        self.driver.find_element(by=By.XPATH, value="//span[@title='Continue shopping']//span").click()



        cart_quantity = self.driver.find_elements(by=By.XPATH, value="//span[@class='ajax_cart_quantity']")[0]
        atrybut = cart_quantity.get_attribute('outerText')


        # then
        assert str(atrybut) == '1'



