from utils import withdrawal_highest_salaries, print_first_10, output_random_20, data_collection


method_dict = {
    '3': withdrawal_highest_salaries,
    '1': print_first_10,
    '2': output_random_20
}


def main() -> None:
    print('Привет, мы поможем подобрать лучших работодателей с сайтов НН и Superjob')
    name_job = input('Введи название профессии\n')
    print('Отлично, начинаем искать:(можешь понаблюдать как обрабатывается твой запрос)')
    data_collection(name_job)

    user_com = input('выберите дальнейшие действия:\n'
                     '1. Вывести первые 10 вакансий\n'
                     '2. Вывести случайные 20 вакансий\n'
                     '3. Вывести топ 5 вакансий с самыми большими зарплатами\n'
                     '4. Выход\n')

    if user_com == '4':
        print('Успехов в поиске работы!')
        return

    method_dict[user_com]()


if __name__ == '__main__':
    main()
