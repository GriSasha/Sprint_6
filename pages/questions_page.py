from locators.questions_page_locators import QuestionsPageLocators
from pages.base_page import BasePage

class QuestionsPage(BasePage):
    def scroll_to_question(self, index):
        self.wait_visibility_of_element(QuestionsPageLocators.questions[index])

    def click_question(self, index):
        locator = QuestionsPageLocators.questions[index]
        self.scroll_to_element(locator)
        self.hide_blockers_for_questions()
        self.click_to_element(locator)

    def get_answer_text(self, index):
        return self.wait_visibility_of_element(QuestionsPageLocators.answers[index]).text

    def open_question_and_get_answer(self, index):
        self.scroll_to_question(index)
        self.click_question(index)
        return self.get_answer_text(index)
