import allure
from urls import Urls
from pages.main_page import MainPage

class TestClickScooterLogo:
    @allure.title('Проверка: при клике на логотип "Самоката" на главной странице открывается страница "Самоката"') 
    @allure.description('На странице ищем логотип "Самоката" и проверяем, что при клике на него открывается главна страница "Самоката"')
    def test_after_clicking_scooter_logo_opens_scooter_main_page(self, driver):

        page = MainPage(driver)
        page.open_page(Urls.url_samokat)


        page.click_scooter_logo()
        scooter_header = page.check_scooter_header().text


        assert 'Самокат' in scooter_header
        assert 'на пару дней' in scooter_header

        
