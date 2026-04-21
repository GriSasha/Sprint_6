from locators.confirm_window_page_locators import ConfirmWindowPageLocators
from pages.base_page import BasePage


class ConfirmWindowPage(BasePage):
    def check_confirm_header(self):
        return self.wait_visibility_of_element(ConfirmWindowPageLocators.confirm_header)
    
    def click_yes_button(self):
        self.click_to_element(ConfirmWindowPageLocators.button_yes_in_form)

