from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)


    def accept_cookies(self):
        try:
            self.driver.find_element(By.ID, "rcc-confirm-button").click()
        except:
            pass

