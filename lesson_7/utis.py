import json


def load_students() -> list:
    """
    Функция получает данные из файла students.json и возвращает в виде list.
    :return: list
    """
    with open('students.json', 'r', encoding='UTF-8') as file:
        students_list = json.load(file)
        return students_list


def load_professions() -> list:
    """
    Функция получает данные из файла professions.json и возвращает в виде list.
    :return: list
    """
    with open('professions.json', 'r', encoding='UTF-8') as file:
        professions_list = json.load(file)
        return professions_list


def get_student_by_pk(pk: int) -> dict:
    """
    Функция ищет студента в списке и возвращает все данные, если студента нет,
     то возвращается пустой словарь.
    :param pk: int номер студента.
    :return: dict
    """
    students_list = load_students()
    for student in students_list:
        if student["pk"] == pk:
            return student

    return dict()


def get_profession_by_title(title: str) -> dict:
    """
    Функция ищет профессию в списке, если нет, то возвращает пустой словарь.
    :param title: str название профессии.
    :return: dict
    """
    professions_list = load_professions()
    for profession in professions_list:
        if profession["title"] == title:
            return profession

    return dict()


def check_fitness(student: dict, profession: dict) -> dict:
    """
    Функция смотрит сколько скиллов есть у пользователя для работы на определенной профессии.
    Считает на сколько пользователь подходит к данной профессии.
    :param student: dict
    :param profession: dict
    :return: dict
    """
    has_student = list(set(student['skills']).intersection(set(profession['skills'])))
    lacks = list(set(profession['skills']).difference(set(student['skills'])))
    fit_percent = round((len(has_student) / len(profession['skills']) * 100))
    if len(has_student) == 0:
        has_student = ['0', 'языков']
    return {"has": has_student,
            "lacks": lacks,
            "fit_percent": fit_percent}
