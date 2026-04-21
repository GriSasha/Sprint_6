from locators.ordered_window_page_locators import OrderedWindowPageLocators
from pages.base_page import BasePage

class OrderedWindowPage(BasePage):
    def check_header_order_rent(self):
        return self.wait_visibility_of_element(OrderedWindowPageLocators.ordered_header)
    
    def is_order_number_displayed(self):
        element = self.wait_visibility_of_element(OrderedWindowPageLocators.order_number)
        text = element.text

        has_title = "Номер заказа" in text
        has_digits = any(i.isdigit() for i in text)

        return has_title and has_digits
    
    def click_order_status_button(self):
        self.click_to_element(OrderedWindowPageLocators.order_status_button)
    