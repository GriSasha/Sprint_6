from locators.how_it_works_page_locators import HowItWorksPageLocators
from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class HowItWorksPage(BasePage):
    def check_visability_of_header(self):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(HowItWorksPageLocators.how_it_works_header))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    def click_order_button(self):
        self.driver.find_element(*HowItWorksPageLocators.order_button_at_bottom).click()