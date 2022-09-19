import json
import random
from questions import Question

with open('questions.json', 'r', encoding='utf-8') as file:
    questions_list = json.load(file)


def creating_playlist() -> list:
    """
    Создает список и элементов класса Question и перемешивает их перед началом игры.
    :return: list
    """
    questions = []

    for question in questions_list:
        questions.append(Question(question['q'], question['d'], question['a']))

    random.shuffle(questions)
    return questions


def output_results(points: int, correct_answers: int) -> None:
    """
    Выводит информацию по завершению игры.
    :param points: количество очков
    :param correct_answers: количество правильных ответов
    :return: None
    """
    print(f'\nВот и всё!\nОтвечено {correct_answers} вопроса из {len(questions_list)}\n'
          f'Набрано баллов: {points}')


def main() -> None:
    """
    Основная логи Игры
    """
    number_points = 0
    number_correct_answers = 0
    print('Игра начинается!\n')

    for question in creating_playlist():
        user = input(f'{question.build_question()}\nВведите ответ: ')
        question.user_response = user
        question.was_question_asked = question.is_correct()
        print(question.build_feedback())

        if question.was_question_asked:
            number_points += question.get_points()
            number_correct_answers += 1

    output_results(number_points, number_correct_answers)


if __name__ == '__main__':
    main()
