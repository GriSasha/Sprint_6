
from locators.about_rent_page_locators import AboutRentPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AboutRentPage(BasePage):
    def check_header_about_rent(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(AboutRentPageLocators.rent_header))

    def choose_date(self, day):
        self.driver.find_element(*AboutRentPageLocators.date_field).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(AboutRentPageLocators.next_month_button)).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(AboutRentPageLocators.day_in_calendar(day))).click()
        self.driver.find_element(*AboutRentPageLocators.rent_header).click()

    def choose_rent_period(self, period):
        period_map = {
            1: "сутки",
            2: "двое суток",
            3: "трое суток",
            4: "четверо суток",
            5: "пятеро суток",
            6: "шестеро суток",
            7: "семеро суток",
        }

        if period not in period_map:
            raise ValueError("days должен быть от 1 до 7")

        self.driver.find_element(*AboutRentPageLocators.rent_period).click()

        option = (
            By.XPATH,
            f"//div[contains(@class,'Dropdown-option') and normalize-space()='{period_map[period]}']"
        )
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(option)).click()

    def choose_scooter_color(self, color):
        color_map = {
        "black": AboutRentPageLocators.black_checkbox,
        "grey": AboutRentPageLocators.grey_checkbox,
        }
        checkbox = self.driver.find_element(*color_map[color])
        if not checkbox.is_selected():
            checkbox.click()

    def fill_comment(self, comment):
        self.driver.find_element(*AboutRentPageLocators.comment_for_courier).send_keys(comment)

    def click_order_button(self):
        self.driver.find_element(*AboutRentPageLocators.order_button_in_form).click()

    def fill_about_rent_form(self, day, period, color, comment):
        self.choose_date(day)
        self.choose_rent_period(period)
        self.choose_scooter_color(color)
        self.fill_comment(comment)
        self.click_order_button()


        
