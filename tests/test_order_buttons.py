import allure
from urls import Urls
from pages.main_page import MainPage
from pages.whos_scooter_page import WhosScooterPage
from pages.how_it_works_page import HowItWorksPage


class TestOrderScooter:
    @allure.title('Проверка клика на кнопку "Заказать" вверху главной страницы "Самоката"') 
    @allure.description('Кликаем на кнопку "Заказать" вверху страницы, дожидаемся перехода к форме заказа')
    def test_click_top_order_button_opens_whose_scooter_page(self, driver):
        page = MainPage(driver)
        page.open_page(Urls.url_samokat)

        page.click_order_button()
        assert WhosScooterPage(driver).check_header_whos_scooter()

    @allure.title('Проверка клика на кнопку "Заказать" внизу главной страницы "Самоката"') 
    @allure.description('Кликаем на кнопку "Заказать" внизу страницы, дожидаемся перехода к форме заказа')
    def test_click_bottom_order_button_opens_whose_scooter_page(self, driver):
        page = HowItWorksPage(driver)
        page.open_page(Urls.url_samokat)

        page.check_visability_of_header()
        page.click_order_button()

        assert WhosScooterPage(driver).check_header_whos_scooter()