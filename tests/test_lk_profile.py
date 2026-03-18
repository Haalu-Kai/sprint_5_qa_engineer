from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from web_locators.locators import *
from data.urls import Urls


class TestStellarBurgersProfileForm:

    def test_click_profile_button_open_profile_form(self, login):
        """Открыть личный кабинет"""
        driver = login
        driver.find_element(*MainPage.mn_profile_button).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LKProfile.lk_info_message))

        
        history_button = driver.find_element(*LKProfile.history_orders_button)  

        assert driver.current_url == Urls.url_profile
        assert history_button.is_displayed(), "Кнопка 'История заказов' не отображается в ЛК"

    def test_click_constructor_button_show_constructor_form(self, login):
        """Переход из личного кабинета в конструктор при нажатии кнопки 'Конструктор'"""
        driver = login
        driver.find_element(*MainPage.mn_profile_button).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LKProfile.lk_info_message))

        driver.find_element(*MainPage.mn_constructor_button).click()

        constructor_header = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPage.constructor_header)
        )

        assert constructor_header.is_displayed(), "Заголовок 'Соберите бургер' не отображается"


    def test_click_logo_button_show_constructor_form(self, login):
        """Переход из личного кабинета в конструктор при нажатии на лого"""
        driver = login
        driver.find_element(*MainPage.mn_profile_button).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LKProfile.lk_info_message))

        driver.find_element(*MainPage.mn_logo).click()

        constructor_header = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPage.constructor_header)
        )

        assert constructor_header.is_displayed(), "Заголовок 'Соберите бургер' не отображается после клика по логотипу"

    def test_click_logout_button_in_lk_open_login_form(self, login):
        """Выйти из аккаунта"""
        driver = login
        driver.find_element(*MainPage.mn_profile_button).click()

        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(LKProfile.lk_info_message))

        driver.find_element(*LKProfile.lk_logout_button).click()

        WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(AuthLogin.al_login_button_any_forms)
        )

        login_button = driver.find_element(*AuthLogin.login_button_with_text)  

        assert driver.current_url == Urls.url_login
        assert login_button.is_displayed(), "Кнопка 'Вход' не отображается после выхода"
