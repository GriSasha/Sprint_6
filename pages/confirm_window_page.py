from locators.confirm_window_page_locators import ConfirmWindowPageLocators
from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class ConfirmWindowPage(BasePage):
    def check_confirm_header(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(ConfirmWindowPageLocators.confirm_header))
    
    def click_yes_button(self):
        self.driver.find_element(*ConfirmWindowPageLocators.button_yes_in_form).click()

