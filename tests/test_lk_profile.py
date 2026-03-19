from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_locators.locators import *
from data.urls import Urls

class TestStellarBurgersProfileForm:

    def test_click_profile_button_open_profile_form(self, login):
        driver = login
        driver.find_element(*MainPage.mn_profile_button).click()

        def profile_opened():
            history_btn = driver.find_element(*LKProfile.history_orders_visible)
            return driver.current_url == Urls.url_profile and history_btn.is_displayed()

        WebDriverWait(driver, 8).until(lambda d: profile_opened())
        assert profile_opened(), "Личный кабинет не открылся или 'История заказов' не видна"

    def test_click_constructor_button_show_constructor_form(self, login):
        driver = login
        driver.find_element(*MainPage.mn_profile_button).click()
        driver.find_element(*MainPage.mn_constructor_button).click()

        constructor_header = WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(MainPage.constructor_title_visible)
        )
        assert constructor_header.is_displayed(), "Заголовок 'Соберите бургер' не отображается"

    def test_click_logo_button_show_constructor_form(self, login):
        driver = login
        driver.find_element(*MainPage.mn_profile_button).click()
        driver.find_element(*MainPage.mn_logo).click()

        constructor_header = WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(MainPage.constructor_title_visible)
        )
        assert constructor_header.is_displayed(), "Заголовок 'Соберите бургер' не отображается после клика по логотипу"

    def test_click_logout_button_in_lk_open_login_form(self, login):
        driver = login
        driver.find_element(*MainPage.mn_profile_button).click()
        driver.find_element(*LKProfile.lk_logout_button).click()

        login_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthLogin.vhod_button_visible)
        )
        assert driver.current_url == Urls.url_login
        assert login_btn.is_displayed(), "Кнопка 'Вход' не отображается после выхода"
