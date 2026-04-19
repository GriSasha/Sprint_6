from locators.whos_scooter_page_locators import WhosScooterPageLocators
from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class WhosScooterPage(BasePage):
    def check_header_whos_scooter(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(WhosScooterPageLocators.order_header))

    def set_name(self, name):
        self.driver.find_element(*WhosScooterPageLocators.name_field).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*WhosScooterPageLocators.surname_field).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*WhosScooterPageLocators.address_field).send_keys(address)

    def set_station(self, metro):
        self.driver.find_element(*WhosScooterPageLocators.station_field).send_keys(metro)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(WhosScooterPageLocators.metro_station_option(metro)))
        self.driver.find_element(*WhosScooterPageLocators.metro_station_option(metro)).click()
        self.driver.find_element(*WhosScooterPageLocators.order_header).click()

    def set_phone(self, phone):
        self.driver.find_element(*WhosScooterPageLocators.phone_field).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*WhosScooterPageLocators.next_button).click()

    def fill_order_form(self, user_data):
        self.set_name(user_data["name"])
        self.set_surname(user_data["surname"])
        self.set_address(user_data["address"])
        self.set_station(user_data["metro"])
        self.set_phone(user_data["phone"])
        self.click_next_button()

