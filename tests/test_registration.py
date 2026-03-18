import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_locators.locators import *
from data.urls import Urls
from data.data import ValidData


class TestStellarBurgersRegistration:

    def test_registration_correct_email_and_pwd_successful_registration(self, driver):
        """При успешной регистрации перебрасывает на страницу входа"""
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys(ValidData.user_name)
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(ValidData.login)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(ValidData.password)
        driver.find_element(*AuthRegistre.ar_register_button).click()

        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthLogin.al_button_with_text_vhod)
        )

        assert driver.current_url == Urls.url_login, "После регистрации не перешли на страницу логина"
        assert login_button.is_displayed(), "Кнопка 'Вход' не отображается на странице логина"

    def test_registration_empty_name_nothing_happens(self, driver):
        """При пустом поле Имя ничего не происходит: остаёмся на странице, ошибки нет"""
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_email_field).send_keys('test1@yan.ru')
        driver.find_element(*AuthRegistre.ar_password_field).send_keys('124567')
        driver.find_element(*AuthRegistre.ar_register_button).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(AuthRegistre.ar_register_button)
        )

        error_messages = driver.find_elements(*AuthRegistre.ar_error_message)

        assert driver.current_url == Urls.url_register, "Произошёл неожиданный переход со страницы регистрации"
        assert len(error_messages) == 0, "Появилась ошибка при пустом имени"

    @pytest.mark.parametrize('invalid_email', [
        'test1@yanru', 'test2yan.ru', 'te st3@yan.ru', 'test4@ya n.ru',
        '@yan.ru', 'test6@.ru', 'test7@yan.'
    ])
    def test_registration_invalid_email_format_shows_error(self, driver, invalid_email):
        """При некорректном формате email показывается ошибка (ожидаем 'Некорректный email' или подсветку)"""
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys('Ильин Виталий')
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(invalid_email)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys('123456')
        driver.find_element(*AuthRegistre.ar_register_button).click()

        error_elem = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthRegistre.ar_error_message_invalid_email)
        )

        assert error_elem.is_displayed(), "Не отобразилась ошибка при некорректном email"

    @pytest.mark.parametrize('short_password', ['1', '12345'])
    def test_registration_short_password_shows_error(self, driver, short_password):
        """При пароле короче 6 символов отображается ошибка 'Некорректный пароль'"""
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys('Ильин Виталий')
        driver.find_element(*AuthRegistre.ar_email_field).send_keys('test1@yan.ru')
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(short_password)
        driver.find_element(*AuthRegistre.ar_register_button).click()

        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthRegistre.ar_error_message)
        )

        assert error_message.is_displayed(), "Не отобразилась ошибка при коротком пароле"
