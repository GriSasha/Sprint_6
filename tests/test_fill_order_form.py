import pytest
import data
import allure
from pages.main_page import MainPage
from pages.whos_scooter_page import WhosScooterPage
from pages.about_rent_page import AboutRentPage
from pages.confirm_window_page import ConfirmWindowPage
from pages.ordered_window_page import OrderedWindowPage
from urls import Urls

class TestFillOrderForm:
    @allure.title('Проверка заполнения раздела "Для кого самокат" формы заказа') 
    @allure.description('На главной странице "Самоката" кликаем по кнопке "Заказать", в разделе "Для кого самокат" заполняем поля: Имя, Фамилия, Адрес, Станция метро, Телефон,'
    'кликаем по кнопке "Далее". Ожидаем появления раздела "Про аренду"')
    @pytest.mark.parametrize(
    "order_data",
    [
        (data.order_data[0]),
        (data.order_data[1]),
        (data.order_data[2]),
    ]
    )
    def test_after_filling_out_whos_scooter_page_opens_about_rent_page(self, driver, order_data):
        page = MainPage(driver)
        page.open_page(Urls.url_samokat)
        page.accept_cookies()

        page.click_order_button()

        whose_page = WhosScooterPage(driver)
        whose_page.fill_order_form(order_data)
        about_rent = AboutRentPage(driver)
        assert about_rent.check_header_about_rent()

    @allure.title('Проверка заполнения раздела "Про аренду" формы заказа') 
    @allure.description('На главной странице "Самоката" кликаем по кнопке "Заказать", в разделе "Для кого самокат" заполняем поля: Имя, Фамилия, Адрес, Станция метро, Телефон, ' \
    'кликаем по кнопке "Далее". В разделе "Про аренду" заполняем поля: Когда привезти самокат, Срок аренды, Цвет самоката, Комментарий,'
    'кликаем по кнопке "Заказать", ожидаем появления окна "Хотите оформить заказ?"')
    @pytest.mark.parametrize(
    "order_data, day, period, color, comment",
    [
        (data.order_data[0], data.day[0], data.period[0], data.color[0], data.comment[0]),
        (data.order_data[1], data.day[1], data.period[1], data.color[1], data.comment[1]),
        (data.order_data[2], data.day[2], data.period[2], data.color[2], data.comment[2]),
    ]
    )
    def test_after_filling_about_rent_page_opens_confirm_window(self, driver, order_data, day, period, color, comment):
        page = MainPage(driver)
        page.open_page(Urls.url_samokat)
        page.accept_cookies()

        page.click_order_button()

        whose_page = WhosScooterPage(driver)
        whose_page.fill_order_form(order_data)
        about_rent = AboutRentPage(driver)
        about_rent.check_header_about_rent()
        about_rent.fill_about_rent_form(day,period,color,comment)
        confirm_window = ConfirmWindowPage(driver)
        assert confirm_window.check_confirm_header()


    @allure.title('Проверка успешности заполнения формы заказа') 
    @allure.description('На главной странице "Самоката" кликаем по кнопке "Заказать", в розделе "Дл кого самокат" заполняем поля: Имя, Фамилия, Адрес, Станция метро, Телефон, ' \
    'кликаем по кнопке "Далее", в разделе "Про аренду" заполняем поля: Когда привезти самокат, Срок аренды, Цвет самоката, Комментарий,'
    'кликаем по кнопке "Заказать", ожидаем появления окна "Хотите оформить заказ?",'
    'кликаем по кнопке "Да", ожидаем появление окна "Заказ оформлен"')
    @pytest.mark.parametrize(
    "order_data, day, period, color, comment",
    [
        (data.order_data[0], data.day[0], data.period[0], data.color[0], data.comment[0]),
        (data.order_data[1], data.day[1], data.period[1], data.color[1], data.comment[1]),
        (data.order_data[2], data.day[2], data.period[2], data.color[2], data.comment[2]),
    ]
    )
    def test_after_click_confirm_window_yes_button_opens_success_order_window(self, driver, order_data, day, period, color, comment):
        page = MainPage(driver)
        page.open_page(Urls.url_samokat)
        page.accept_cookies()

        page.click_order_button()

        whose_page = WhosScooterPage(driver)
        whose_page.fill_order_form(order_data)
        about_rent = AboutRentPage(driver)
        about_rent.check_header_about_rent()
        about_rent.fill_about_rent_form(day,period,color,comment)
        confirm_window = ConfirmWindowPage(driver)
        confirm_window.check_confirm_header()
        confirm_window.click_yes_button()
        order_window = OrderedWindowPage(driver)
        assert order_window.check_header_order_rent()
        