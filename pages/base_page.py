from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        self.find_element(locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element(locator).text
    
    def wait_visibility_of_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def wait_element_to_be_clickable(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_with_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_current_url(self):
        return self.driver.current_url
    
    def wait_number_of_windows(self, count, time=10):
        return WebDriverWait(self.driver, time).until(
        EC.number_of_windows_to_be(count)
        )

    def wait_for_url_contains(self, text, time=10):
        return WebDriverWait(self.driver, time).until(
        EC.url_contains(text)
        )


    def accept_cookies(self):
        try:
            self.driver.find_element(By.ID, "rcc-confirm-button").click()
        except:
            pass

    def hide_blockers_for_questions(self):
        self.driver.execute_script("""
            const blockers = [
                '.Home_Scooter__3YdJy',
                '.Home_BluePrint__TGX2n',
                'img[src="/assets/blueprint.png"]',
                'img[src="/assets/scooter.png"]'
            ];

            blockers.forEach(selector => {
                const element = document.querySelector(selector);
                if (element) {
                    element.style.display = 'none';
                }
            });
        """)

