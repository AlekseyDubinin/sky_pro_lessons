class Question:
    def __init__(self, question_text: str, complexity_issue: str, correct_answer_option: str) -> None:
        self.question_text = question_text
        self.complexity_issue = complexity_issue
        self.correct_answer_option = correct_answer_option
        self.was_question_asked = False
        self.user_response = None
        self.points_question = complexity_issue

    def get_points(self) -> int:
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return int(self.points_question) * 10

    def is_correct(self) -> bool:
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов, иначе False.
        """
        return self.correct_answer_option == self.user_response

    def build_question(self) -> str:
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f'Вопрос: {self.question_text}\nСложность: {self.complexity_issue}/5'

    def build_feedback(self) -> str:
        """Возвращает:
        Ответ верный, получено __ баллов
        или
        Ответ неверный, верный ответ __
        """
        if self.was_question_asked:
            return f'Ответ верный, получено {self.get_points()} баллов'
        else:
            return f'Ответ неверный, верный ответ {self.correct_answer_option}'

    def __repr__(self) -> str:
        """
        Позволяет увидеть созданный объект в виде строки.
        :return: str
        """
        return f'{self.question_text} {self.complexity_issue} {self.correct_answer_option}'
