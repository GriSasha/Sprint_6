from selenium.webdriver.common.by import By

class MainPageLocators:

    scooter_header = (By.XPATH, "//div[contains(@class, 'Home_Header')]")
    order_button_at_top = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and normalize-space()='Заказать']")
    scooter_logo = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    yandex_logo = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")