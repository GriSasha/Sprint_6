from selenium.webdriver.common.by import By

class WhosScooterPageLocators:

    order_header = (By.XPATH, "//div[contains(@class, 'Order_Header__BZXOb') and normalize-space()='Для кого самокат']")
    name_field = (By.XPATH, "//input[contains(@placeholder, '* Имя')]")
    surname_field = (By.XPATH, "//input[contains(@placeholder, '* Фамилия')]")
    address_field = (By.XPATH, "//input[contains(@placeholder, '* Адрес: куда привезти заказ')]")
    station_field = (By.XPATH, "//input[contains(@placeholder, '* Станция метро')]")

    @staticmethod
    def metro_station_option(metro):
        return (
            By.XPATH,
            f"//div[contains(@class, 'select-search__select')]//button[normalize-space()='{metro}']"
        )
    
    phone_field = (By.XPATH, "//input[contains(@placeholder, '* Телефон: на него позвонит курьер')]")
    next_button = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and normalize-space()='Далее']")