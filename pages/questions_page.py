from locators.questions_page_locators import QuestionsPageLocators
from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class QuestionsPage(BasePage):
    def scroll_to_question(self, index):
        element = self.driver.find_element(*QuestionsPageLocators.questions[index])
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_question(self, index):
        element = self.driver.find_element(*QuestionsPageLocators.questions[index])

        self.driver.execute_script("arguments[0].scrollIntoView();", element)

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

        element.click()

    def get_answer_text(self, index):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(QuestionsPageLocators.answers[index])).text

    def open_question_and_get_answer(self, index):
        self.scroll_to_question(index)
        self.click_question(index)
        return self.get_answer_text(index)
