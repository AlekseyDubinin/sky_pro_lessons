with open('list_all', 'r', encoding='utf-8') as file:
    list_all = [_.strip() for _ in file]


def filter1(user_str: str, list1: list) -> list:
    return list(filter(lambda x: user_str in x, list1))


def map1(number: str, list1: list) -> list:
    wer = list(map(str.split, list1))
    return [j[int(number)] for j in wer]


def unique1(_, list1: list) -> list:
    return list(set(list1))


def sort1(value: str, list1) -> list:
    flag = False

    if value == 'desc':
        flag = True

    return sorted(list1, reverse=flag)


def limit1(number: str, list1: list) -> list:
    return list1[:int(number)]


def main(processing_list: list) -> None:
    try:
        for i in input().split('|'):
            user_command, value = i.split()
            if user_command in command_dict:
                processing_list = command_dict[user_command](value, processing_list)
            else:
                print('Ошибка ввода')
                return
        print(*processing_list, sep='\n')
    except ValueError:
        print('Ошибка ввода')


command_dict = {'filter': filter1,
                'map': map1,
                'unique': unique1,
                'sort': sort1,
                'limit': limit1
                }


if __name__ == '__main__':
    main(list_all)
