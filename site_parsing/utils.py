import random
import time

from classes import *
import json
import re

with open('HH_Superjob_vacancy.json', 'r', encoding='utf-8') as file:
    f = json.load(file)


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
    correct_salary(site_all)

    with open('HH_Superjob_vacancy.json', 'w') as file:
        json.dump(site_all, file, indent=4, ensure_ascii=False)

    print(f'Всего было найдено подходящих результатов {len(site_all)}\n')
    time.sleep(2)


def correct_salary(all_dict: dict) -> None:
    """
    Функция обрабатывает поле salary в словаре и преобразует в int
    :param all_dict: словарь с вакансиями
    :return:
    """
    for i in all_dict:
        num = re.findall(r'\d+', i["salary"])
        if len(num) == 0:
            i["salary"] = 0
        else:
            i["salary"] = int(max(num))


def withdrawal_highest_salaries() -> None:
    """
    Функция фильтрует файл с вакансиями и выводит топ 5 высокооплач.
    :return:
    """
    file_all = sorted(f, key=lambda x: x['salary'], reverse=True)[:5]
    for items in file_all:
        time.sleep(1)
        correct_output(items)


def print_first_10() -> None:
    """
    Функция выводит первые 10 вакансий.
    :return:
    """
    for items in f[:10]:
        time.sleep(1)
        correct_output(items)


def output_random_20() -> None:
    """
    Функция выводит случайные 20 вакансий.
    :return:
    """
    random.shuffle(f)
    for iters in f[:20]:
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
