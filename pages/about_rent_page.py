
from locators.about_rent_page_locators import AboutRentPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class AboutRentPage(BasePage):
    def check_header_about_rent(self):
        return self.wait_visibility_of_element(AboutRentPageLocators.rent_header)

    def choose_date(self, day):
        self.click_to_element(AboutRentPageLocators.date_field)
        self.wait_element_to_be_clickable(AboutRentPageLocators.next_month_button).click()
        self.wait_element_to_be_clickable(AboutRentPageLocators.day_in_calendar(day)).click()
        self.click_to_element(AboutRentPageLocators.rent_header)

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

        self.click_to_element(AboutRentPageLocators.rent_period)

        option = (
            By.XPATH,
            f"//div[contains(@class,'Dropdown-option') and normalize-space()='{period_map[period]}']"
        )
        self.wait_element_to_be_clickable(option).click()

    def choose_scooter_color(self, color):
        color_map = {
        "black": AboutRentPageLocators.black_checkbox,
        "grey": AboutRentPageLocators.grey_checkbox,
        }
        checkbox = self.find_element(color_map[color])
        if not checkbox.is_selected():
            checkbox.click()

    def fill_comment(self, comment):
        self.add_text_to_element(AboutRentPageLocators.comment_for_courier, comment)

    def click_order_button(self):
        self.click_to_element(AboutRentPageLocators.order_button_in_form)

    def fill_about_rent_form(self, day, period, color, comment):
        self.choose_date(day)
        self.choose_rent_period(period)
        self.choose_scooter_color(color)
        self.fill_comment(comment)
        self.click_order_button()


        
