from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class MainPage(BasePage):
    def click_order_button(self):
        self.driver.find_element(*MainPageLocators.order_button_at_top).click()

    def check_scooter_header(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(MainPageLocators.scooter_header))
    
    def click_scooter_logo(self):
        self.driver.find_element(*MainPageLocators.scooter_logo).click()

    def click_yandex_logo(self):
        self.driver.find_element(*MainPageLocators.yandex_logo).click()

