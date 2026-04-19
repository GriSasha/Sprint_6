from selenium.webdriver.common.by import By


class TrackOrderPageLocators:

    order_columns = (By.XPATH, "//div[contains(@class='Track_OrderColumns')]")
    cansel_button = By.XPATH, "//button[contains(@class='Button_Button__ra12g') and normalize-space()='Отменить заказ']"
    scooter_logo = (By.XPATH, "//a[contains(@class='Header_LogoScooter')]")
    yandex_logo = (By.XPATH, "//a[contains(@class='Header_LogoYandex')]")
    not_found_block = (By.XPATH, "//div[contains(@class='Track_NotFound')]")

    @staticmethod
    def value_by_title(title: str):
        return (
            By.XPATH,
            "//div[contains(@class='Track_Row')]"
            f"[.//div[contains(@class='Track_Title') and normalize-space()='{title}']]"
            "//div[contains(@class='Track_Value')]"
        )
