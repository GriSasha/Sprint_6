from locators.dzen_page_locators import DzenPageLocators
from pages.base_page import BasePage


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class DzenPage(BasePage):

    def check_dzen_header(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(DzenPageLocators.dzen_header))


