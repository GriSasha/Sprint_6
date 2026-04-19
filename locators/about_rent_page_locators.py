from selenium.webdriver.common.by import By

class AboutRentPageLocators:

    rent_header = (By.XPATH, "//div[contains(@class, 'Order_Header__BZXOb') and normalize-space()='Про аренду']")
    date_field = (By.XPATH, "//input[contains(@placeholder, '* Когда привезти самокат')]")
    current_month = (By.CLASS_NAME, "react-datepicker__current-month")
    next_month_button = (By.XPATH, "//button[contains(@class, 'react-datepicker__navigation--next')]")
    rent_period = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder') and normalize-space()='* Срок аренды']")
    dropdown_arrow_rent_form = (By.XPATH, "//span[contains(@class, 'Dropdown-arrow')]")
    order_checkbox = (By.XPATH, "//div[contains(@class='Order_Title__3EKne') and (normalize-space()='Цвет самоката')]")
    black_checkbox = (By.XPATH, "//input[contains(@id, 'black') and @type='checkbox']")
    grey_checkbox = (By.XPATH, "//input[contains(@id, 'grey') and @type='checkbox']")
    comment_for_courier = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button_in_form =  (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[normalize-space()='Заказать']")
    back_button_in_form =  (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[normalize-space()='Назад']")

    @staticmethod
    def day_in_calendar(day):
        return (
            By.XPATH,
        f"//div[contains(@class, 'react-datepicker__day') "
        f"and not(contains(@class, 'react-datepicker__day--outside-month')) "
        f"and normalize-space()='{day}']"
    )

