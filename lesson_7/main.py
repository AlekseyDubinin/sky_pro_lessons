from utis import *


def main() -> None:
    """
    Основная логика программы.
    :return:
    """
    number_student = int(input('Программа: Введите номер студента\nПользователь: '))
    dict_student = get_student_by_pk(number_student)

    if len(dict_student) == 0:
        print('Программа: У нас нет такого студента')
        return
    else:
        print(f'Программа: Студент {dict_student["full_name"]}\n'
              f'Программа: Знает {", ".join(dict_student["skills"])}')

    prof = input(f'Программа: Выберите специальность для оценки студента {dict_student["full_name"]}\n'
                 f'Пользователь: ')

    dict_professions = get_profession_by_title(prof)

    if len(dict_professions) == 0:
        print('Программа: У нас нет такой специальности')
    else:
        info = check_fitness(dict_student, dict_professions)
        print(f'Программа: Пригодность {info["fit_percent"]}%\n'
              f'Программа: {dict_student["full_name"]} знает {", ".join(info["has"])}\n'
              f'Программа: {dict_student["full_name"]} не знает {", ".join(info["lacks"])}')


if __name__ == '__main__':
    main()
