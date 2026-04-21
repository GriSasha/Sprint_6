import pytest
import allure

from pages.questions_page import QuestionsPage
from urls import Urls
from data import answers, questions


class TestQuestionsPage:
    @allure.title('Проверка текста вопросов в разделе "Вопросы о важном"') 
    @allure.description(
        'Прокручиваем страницу до раздела "Вопросы о важном", кликаем на стрелочку каждого вопроса, убеждаемся, что открывается соответсвтующий текст'
        )
    @pytest.mark.parametrize(
    "index, expected_answer",
    answers,
    ids=questions
    )

    def test_questions_answers(self, driver, index, expected_answer):
        page = QuestionsPage(driver)
        page.open_page(Urls.url_samokat)

        actual_answer = page.open_question_and_get_answer(index)

        assert actual_answer == expected_answer

        
