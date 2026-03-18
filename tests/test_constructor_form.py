from web_locators.locators import *

class TestStellarBurgersConstructorForm:

    def test_constructor_go_to_sauces_scroll_to_sauces(self, login):
        """Проверка перехода на "Соусы" """
        driver = login
        driver.find_element(*MainPage.mn_constructor_button).click()

        sauces_tab = driver.find_element(*MainPage.mn_sauces_button)
        sauces_tab.click()

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((MainPage.mn_sauces_button[0], MainPage.mn_sauces_button[1] + "[contains(@class, 'current')]"))
        )

  

        h_sauce = driver.find_element(*MainPage.mn_h_sauces)
        assert h_sauce.is_displayed(), "Заголовок 'Соусы' не отображается после переключения"

    def test_constructor_go_to_filling_scroll_to_filling(self, login):
        """Проверка перехода на "Начинки" """
        driver = login
        driver.find_element(*MainPage.mn_constructor_button).click()

        filling_tab = driver.find_element(*MainPage.mn_filling_button)
        filling_tab.click()

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((MainPage.mn_filling_button[0], MainPage.mn_filling_button[1] + "[contains(@class, 'current')]"))
        )

        h_filling = driver.find_element(*MainPage.mn_h_filling)
        assert h_filling.is_displayed()

    def test_constructor_go_to_bun_scroll_to_bun(self, login):
        """Проверка перехода на "Булки" """
        driver = login
        driver.find_element(*MainPage.mn_constructor_button).click()


        bun_tab = driver.find_element(*MainPage.mn_bun_button)  
        bun_tab.click()

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((MainPage.mn_bun_button[0], MainPage.mn_bun_button[1] + "[contains(@class, 'current')]"))
        )

        h_bun = driver.find_element(*MainPage.mn_h_bun)  
        assert h_bun.is_displayed()
