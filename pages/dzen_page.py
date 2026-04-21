from locators.dzen_page_locators import DzenPageLocators
from pages.base_page import BasePage

class DzenPage(BasePage):

    def check_dzen_header(self):
        return self.wait_visibility_of_element(DzenPageLocators.dzen_header)
