def iss(elem_1, elem_2):
    result = ''
    if id(elem_1) == id(elem_2):
        result += 'Две переменные ссылаются на один и тот же адрес в памяти, '
    else:
        result += 'Две переменные ссылаются на разные адреса в памяти, '

    if elem_1 == elem_2:
        result += 'имеют одинаковые значения.\n'
    else:
        result += 'имеют разные значения.\n'

    return result, f'id первой переменной: {id(elem_1)}\nid второй переменной: {id(elem_2)}\n' \
                   f'Значение первой переменной: {elem_1}\nЗначение второй переменной: {elem_2}'


x, y = [1, [2]], [1, [2]]
print(*iss(x, y))


A = 'spam'
B = A
B = 'shrubbery'
print(*iss(A, B))

A = ['spam']
B = A[:]
B[0] = 'shrubbery'
print(*iss(A, B))

print(iss([], []))
print(iss('', ''))
print(iss({}, {}))
