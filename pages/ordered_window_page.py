from locators.ordered_window_page_locators import OrderedWindowPageLocators
from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class OrderedWindowPage(BasePage):
    def check_header_order_rent(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderedWindowPageLocators.ordered_header))
    
    def is_order_number_displayed(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(OrderedWindowPageLocators.order_number)
        )
        text = element.text

        has_title = "Номер заказа" in text
        has_digits = any(i.isdigit() for i in text)

        return has_title and has_digits
    
    def click_order_status_button(self):
        self.driver.find_element(*OrderedWindowPageLocators.order_status_button).click()
    