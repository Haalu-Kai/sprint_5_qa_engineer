from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_locators.locators import *

class TestStellarBurgersConstructorForm:

    def test_constructor_go_to_sauces_scroll_to_sauces(self, login):
        driver = login
        driver.find_element(*MainPage.mn_constructor_button).click()
        driver.find_element(*MainPage.mn_sauces_button).click()

        def sauces_tab_active_and_header_visible():
            tab = driver.find_element(*MainPage.tab_sauces_current)
            header = driver.find_element(*MainPage.mn_h_sauces)
            return tab.is_displayed() and "current" in tab.get_attribute("class") and header.is_displayed()

        WebDriverWait(driver, 8).until(lambda d: sauces_tab_active_and_header_visible())
        assert sauces_tab_active_and_header_visible(), "Таб 'Соусы' не стал активным или заголовок не виден"

    def test_constructor_go_to_filling_scroll_to_filling(self, login):
        driver = login
        driver.find_element(*MainPage.mn_constructor_button).click()
        driver.find_element(*MainPage.mn_filling_button).click()

        def filling_tab_active_and_header_visible():
            tab = driver.find_element(*MainPage.tab_filling_current)
            header = driver.find_element(*MainPage.mn_h_filling)
            return tab.is_displayed() and "current" in tab.get_attribute("class") and header.is_displayed()

        WebDriverWait(driver, 8).until(lambda d: filling_tab_active_and_header_visible())
        assert filling_tab_active_and_header_visible(), "Таб 'Начинки' не стал активным или заголовок не виден"

    def test_constructor_go_to_bun_scroll_to_bun(self, login):
        driver = login
        driver.find_element(*MainPage.mn_constructor_button).click()
        driver.find_element(*MainPage.mn_bun_button).click()

        def buns_tab_active_and_header_visible():
            tab = driver.find_element(*MainPage.tab_buns_current)
            header = driver.find_element(*MainPage.mn_h_bun)
            return tab.is_displayed() and "current" in tab.get_attribute("class") and header.is_displayed()

        WebDriverWait(driver, 8).until(lambda d: buns_tab_active_and_header_visible())
        assert buns_tab_active_and_header_visible(), "Таб 'Булки' не стал активным или заголовок не виден"
