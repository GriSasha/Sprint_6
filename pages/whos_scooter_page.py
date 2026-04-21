from locators.whos_scooter_page_locators import WhosScooterPageLocators
from pages.base_page import BasePage

class WhosScooterPage(BasePage):
    def check_header_whos_scooter(self):
        return self.wait_visibility_of_element(WhosScooterPageLocators.order_header)

    def set_name(self, name):
        self.add_text_to_element(WhosScooterPageLocators.name_field, name)

    def set_surname(self, surname):
        self.add_text_to_element(WhosScooterPageLocators.surname_field, surname)

    def set_address(self, address):
        self.add_text_to_element(WhosScooterPageLocators.address_field, address)

    def set_station(self, metro):
        self.add_text_to_element(WhosScooterPageLocators.station_field, metro)
        self.wait_element_to_be_clickable(WhosScooterPageLocators.metro_station_option(metro))
        self.click_to_element(WhosScooterPageLocators.metro_station_option(metro))
        self.click_to_element(WhosScooterPageLocators.order_header)

    def set_phone(self, phone):
        self.add_text_to_element(WhosScooterPageLocators.phone_field, phone)

    def click_next_button(self):
        self.click_to_element(WhosScooterPageLocators.next_button)

    def fill_order_form(self, user_data):
        self.set_name(user_data["name"])
        self.set_surname(user_data["surname"])
        self.set_address(user_data["address"])
        self.set_station(user_data["metro"])
        self.set_phone(user_data["phone"])
        self.click_next_button()

