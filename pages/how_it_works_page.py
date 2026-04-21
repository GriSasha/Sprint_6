from locators.how_it_works_page_locators import HowItWorksPageLocators
from pages.base_page import BasePage

class HowItWorksPage(BasePage):
    def check_visability_of_header(self):
        self.scroll_to_element(HowItWorksPageLocators.how_it_works_header)
    
    def click_order_button(self):
        self.click_to_element(HowItWorksPageLocators.order_button_at_bottom)
        