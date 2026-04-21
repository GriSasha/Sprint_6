from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    def click_order_button(self):
        self.click_to_element(MainPageLocators.order_button_at_top)

    def check_scooter_header(self):
        return self.wait_visibility_of_element(MainPageLocators.scooter_header)
    
    def click_scooter_logo(self):
        self.click_to_element(MainPageLocators.scooter_logo)

    def click_yandex_logo(self):
        self.click_to_element(MainPageLocators.yandex_logo)
