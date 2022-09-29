import random
import time

from classes import *
import json
import re


def open_file():
    with open('HH_Superjob_vacancy.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def data_collection(profession: str) -> None:
    """
    Функция формирует файл HH_Superjob_vacancy c двух сайтов HH, Superjob.
    :param profession: Название профессии
    :return:
    """

    hh = HH(profession)
    hh2 = hh.parser(url=hh.URL)
    superjob = Superjob(profession)
    superjob2 = superjob.parser(url=superjob.URL)
    site_all = hh2 + superjob2

    with open('HH_Superjob_vacancy.json', 'w') as file:
        json.dump(site_all, file, indent=4, ensure_ascii=False)

    print(f'Всего было найдено подходящих результатов {len(site_all)}\n')
    time.sleep(2)


def withdrawal_highest_salaries() -> None:
    """
    Функция фильтрует файл с вакансиями и выводит топ 5 высокооплач.
    :return:
    """
    file_all = sorted(open_file(), key=lambda x: int(x['salary']), reverse=True)[:5]
    for items in file_all:
        time.sleep(1)
        correct_output(items)


def print_first_10() -> None:
    """
    Функция выводит первые 10 вакансий.
    :return:
    """
    for items in open_file()[:10]:
        time.sleep(1)
        correct_output(items)


def output_random_20() -> None:
    """
    Функция выводит случайные 20 вакансий.
    :return:
    """
    random.shuffle(open_file())
    for iters in open_file()[:20]:
        time.sleep(1)
        correct_output(iters)


def correct_output(iters) -> None:
    """
    Функция выводит информацию в корректном виде.
    :param iters: Одна вакансия
    :return:
    """
    if iters["salary"] == 0:
        iters["salary"] = 'Зарплата не указана'
    print(Vacancy(job_title=iters["title"], salary_vacancies=iters["salary"], job_link=iters["job_posting_link"],
                  vacancy_description=iters["description"]))
