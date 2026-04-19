from selenium.webdriver.common.by import By

class OrderedWindowPageLocators:

    ordered_header = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(.,'Заказ оформлен')]")
    order_number = (By.XPATH, "//div[contains(@class, 'Order_Text') and contains(.,'Номер заказа:')]")
    order_status_button =  (By.XPATH, "//div[contains(@class, 'Order_NextButton')]//button[text()='Посмотреть статус']")