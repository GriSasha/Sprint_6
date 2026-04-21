from locators.track_order_page_locators import TrackOrderPageLocators
from pages.base_page import BasePage

class TrackOrderPage(BasePage):
    def wait_track_page_loaded(self):
        self.wait_visibility_of_element(TrackOrderPageLocators.order_columns)
        
    def click_scooter_logo(self):
        self.click_to_element(TrackOrderPageLocators.scooter_logo)

    def click_yandex_logo(self):
        self.click_to_element(TrackOrderPageLocators.yandex_logo)

