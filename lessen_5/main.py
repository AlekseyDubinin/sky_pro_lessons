from collections import Counter
import random

dict_alfa = {"а": 8, "б": 2, "в": 4, "г": 2, "д": 4, "е": 8, "ё": 1, "ж": 1, "з": 2, "и": 5, "й": 1, "к": 4, "л": 4,
             "м": 3, "н": 5, "о": 10, "п": 4, "р": 5, "с": 5, "т": 5, "у": 4, "ф": 1, "х": 1, "ц": 1, "ч": 1, "ш": 1,
             "щ": 1, "ъ": 1, "ы": 2, "ь": 2, "э": 1, "ю": 1, "я": 2}

points = {
    3: 3,
    4: 6,
    5: 7,
    6: 8}


def dictionary_processing(keys_list: list, number_letters=7) -> list:
    try:
        for i in range(number_letters):
            keys_list.append(random.choice(list(dict_alfa)))
            dict_alfa[keys_list[i]] -= 1
            if dict_alfa[keys_list[i]] == 0:
                del dict_alfa[keys_list[i]]
        return keys_list
    except ValueError:
        print("Буквы закончились")
        return keys_list


def word_check(answer: str, letters: str, keys_list: list, name: str):
    if Counter(answer) - Counter(letters):
        print('У вас нет таких букв, пробуйте еще раз')
        return False, 0
    else:
        with open('russian_word.txt', 'r', encoding='UTF-8') as file:
            contents = file.read()
        new_letter = []
        poin = 0
        if answer in contents:
            poin = points[len(answer)]
            print('Программа:\nТакое слово есть.')
            print(f'{name} получает {poin} баллов.')
            dictionary_processing(new_letter, len(answer) + 1)
            if len(new_letter) == 0:
                return 0, poin
            else:
                print('Добавляю буквы', ', '.join(new_letter))
                for i in answer:
                    if i in keys_list:
                        keys_list.remove(i)
                return new_letter, poin
        else:
            print('Программа:\nТакого слова нет.')
            print(f'{name} не получает очков.')
            dictionary_processing(new_letter, 1)
            print('Добавляю букву', ', '.join(new_letter))
            return new_letter, poin


def search_winner() -> None:
    if point_all_one > point_all_two:
        print(f'Выигрывает {user_one}.\nСчет {point_all_one}:{point_all_two}')
    else:
        print(f'Выигрывает {user_two}.\nСчет {point_all_two}:{point_all_one}')


def main(keys_one, point_all_one, keys_two, point_all_two):
    flag = True
    while True:
        if flag:
            print(f'Программа:\nХодит {user_one}')
            print('Ваши буквы: ', ", ".join(keys_one))
            user_answer = input('Пользователь:\n')
            if user_answer == 'stop':
                break
            if len(user_answer) < 3:
                print('Таких коротких слов нет, пробуй еще раз')
                continue
            wer, point = word_check(user_answer, ''.join(keys_one), keys_one, user_one)
            if not wer:
                continue
            elif len(wer) == 0:
                break
            keys_one += wer
            point_all_one += point

            flag = False
        else:
            print(f'Программа:\nХодит {user_two}')
            print('Ваши буквы: ', ", ".join(keys_two))
            user_answer = input('Пользователь:\n')
            if user_answer == 'стоп':
                break
            if len(user_answer) < 3:
                print('Таких коротких слов нет, пробуй еще раз')
                continue
            wer, point = word_check(user_answer, ''.join(keys_two), keys_two, user_two)
            if not wer:
                continue
            keys_two += wer
            point_all_two += point
            flag = True
    return point_all_one, point_all_two


def beginning_game():
    print('Программа:\nПривет.\nМы начинаем играть в Scrabble\n\nКак зовут первого игрока? ')

    user_one_name = input('Пользователь:\n')

    print('Программа:\nКак зовут второго игрока? ')

    user_two_name = input('Пользователь:\n')

    print(f'Программа:\n{user_one_name} vs {user_two_name}\n(раздаю случайные буквы)')
    print(f'{user_one_name} - буквы "{", ".join(dictionary_processing(keys_one))}"')
    print(f'{user_two_name} - буквы "{", ".join(dictionary_processing(keys_two))}"')
    return user_one_name, user_two_name


if __name__ == '__main__':
    keys_one = []
    keys_two = []
    point_all_one = 0
    point_all_two = 0
    user_one, user_two = beginning_game()
    point_all_one, point_all_two = main(keys_one, point_all_one, keys_two, point_all_two)
    search_winner()
