from logistics import *

fer_dict = {'milk': 10,
            'red': 3,
            'bread': 4}

shop_dict = {'milk': 5}

store = Store(fer_dict)
shop = Shop(shop_dict)

user_list = [Request(product='milk', amount=3, from1='store', to='shop'),
             Request(product='milk', amount=3, from1='store', to='shop'),
             Request(product='milk', amount=3, from1='store', to='shop'),
             Request(product='milk', amount=3, from1='store', to='shop')]


def main() -> None:
    for user in user_list:
        print(user)

        if store.remove(user.product, user.amount) and shop.add(user.product, user.amount):
            print('Нужное количество есть на складе')
            print('На складе хранится:\n')

            for name_prod, count in store.get_items.items():
                print(name_prod, count)

            print('В магазине хранится:\n')

            for name_prod, count in shop.get_items.items():
                print(name_prod, count)

        elif user.amount > shop.get_free_space:
            print('В магазин недостаточно места, попробуйте что то другое')
        else:
            print('Не хватает на складе, попробуйте заказать меньше')


if __name__ == '__main__':
    main()
