class Int(int):
    dict_number = {
        'один': 1,
        'два': 2,
        'три': 3,
        'четыре': 4,
        'пять': 5
    }

    def __add__(self, other):
        if isinstance(other, str):
            if other.isdigit():
                return super(Int, self).__add__(int(other))
            elif other in self.dict_number:
                return super(Int, self).__add__(self.dict_number[other])

            raise TypeError(f'справа от знака "+" непонятный текст.'
                            ' Если что, я понимаю текстом цифры с 1 по 5.')

        return super(Int, self).__add__(other)


x = Int(5)

print(x + '5')  # 10
print(x + 'один')  # 6
# print(x + 'пять')  # 10
print(x + 'шесть')
# print(x + 'a')
# print(x + 1)
# print(x + (1,))
