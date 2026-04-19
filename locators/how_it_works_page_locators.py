from selenium.webdriver.common.by import By

class HowItWorksPageLocators:
    order_button_at_bottom = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and normalize-space()='Заказать']")
    how_it_works_header = (By.XPATH, "//div[contains (@class, 'Home_SubHeader') and normalize-space()='Как это работает']")