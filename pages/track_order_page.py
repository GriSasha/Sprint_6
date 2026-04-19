from locators.track_order_page_locators import TrackOrderPageLocators
from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TrackOrderPage(BasePage):
    def wait_track_page_loaded(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(TrackOrderPageLocators.order_columns)
        )

    def get_value_by_title(self, title):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                TrackOrderPageLocators.value_by_title(title)
            )
        )
        return element.text.strip()

    def get_order_data(self):
        return {
            "name": self.get_value_by_title("Имя"),
            "surname": self.get_value_by_title("Фамилия"),
            "address": self.get_value_by_title("Адрес"),
            "metro": self.get_value_by_title("Станция метро"),
            "phone": self.get_value_by_title("Телефон"),
            "delivery_date": self.get_value_by_title("Дата доставки"),
            "rent_period": self.get_value_by_title("Срок аренды"),
            "color": self.get_value_by_title("Цвет"),
            "comment": self.get_value_by_title("Комментарий"),
        }

    def is_not_found_displayed(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(TrackOrderPageLocators.not_found_block)
            )
            return True
        except Exception:
            return False
        
    def click_scooter_logo(self):
        self.driver.find_element(*TrackOrderPageLocators.scooter_logo).click()

    def click_yandex_logo(self):
        self.driver.find_element(*TrackOrderPageLocators.yandex_logo).click()

