import allure
from urls import Urls
from pages.main_page import MainPage
from pages.dzen_page import DzenPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestClickYandexLogo:
    @allure.title('Проверка: при клике на логотип "Яндекс" на главной странице открывается страница "Дзен"') 
    @allure.description('На странице ищем логотип "Яндекс" и проверяем, что при клике на него через редирект открывается страница "Дзен"')
    def test_after_clicking_yandex_logo_opens_dzen_page(self, driver):

        page = MainPage(driver)
        page.open_page(Urls.url_samokat)


        page.click_yandex_logo()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
        dzen_page = DzenPage(driver)
        dzen_page.check_dzen_header()

        
        assert 'dzen.ru' in driver.current_url



        