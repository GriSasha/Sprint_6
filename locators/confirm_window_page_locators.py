from selenium.webdriver.common.by import By

class ConfirmWindowPageLocators:

    confirm_header = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(., 'Хотите оформить заказ?')]")
    button_not_in_form =  (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Нет']")
    button_yes_in_form =  (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Да']")
