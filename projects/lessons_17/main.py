import psycopg2
from psycopg2 import Error
from config import host, user, password, db_name, port


def db_connect():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
            port=port
        )
        connection.autocommit = True

        return connection

    except Error as _ex:
        print('Error!', _ex)
        return False


def get_all_data(cursor):
    request = """
    SELECT * FROM all_info
    """
    cursor.execute(request)
    result = cursor.fetchall()
    for r in result:
        print(r)


def data_user(cursor, name="Павел"):
    request = f"""
            SELECT 
            all_info.name_stor,
            all_info.price,
            people.name
            FROM all_info JOIN people ON all_info.id_author = id_name
            WHERE people.name = '{name}'
    """
    cursor.execute(request)
    result = cursor.fetchall()
    for r in result:
        print(r)
        print('-' * 45)


def data_price(cursor, price_one=100, price_two=1000):
    request = f"""
    SELECT *
    FROM all_info
    WHERE price >= {price_one} and price <= {price_two}
    ORDER BY price
    """
    cursor.execute(request)
    result = cursor.fetchall()
    for r in result:
        print(r)
        print('-' * 45)


def data_citi(cursor, name_citi="Москва"):
    request = f"""
            SELECT 
            all_info.name_stor,
            all_info.price,
            address.address
            FROM all_info JOIN address ON all_info.id_author = id_addr
            WHERE  address.address LIKE '{name_citi}%'
    """
    cursor.execute(request)
    result = cursor.fetchall()
    for r in result:
        print(r)
        print('-' * 45)


def data_user_price(cursor, name='Павел', price=2500):
    request = f"""
            SELECT 
            all_info.name_stor,
            all_info.price,
            people.name
            FROM all_info JOIN people ON all_info.id_author = id_name
            WHERE people.name = '{name}' and all_info.price = {price}
    """
    cursor.execute(request)
    result = cursor.fetchall()
    for r in result:
        print(r)
        print('-' * 45)


def main():
    conn = db_connect()
    cur = conn.cursor()

    print('Поработаем с базой данных.\n'
          'Выбери из меню действия доступные для работы с базой:\n'
          '1. Вывести все данные из базы:\n'
          '2. Вывести данные конкретного пользователя\n'
          '3. Вывести данные в определенном диапазоне цен\n'
          '4. Вывести данные с выбором города\n'
          '5. Вывести данные с определенным пользователем и ценой')

    user = input('###: ')

    if int(user) == 1:
        get_all_data(cur)
    elif int(user) == 2:
        user_name = input('Укажите имя из базы: ')
        data_user(cur, user_name)
    elif int(user) == 3:
        price_one, price_two = input('Введите диапазон цен через запятую: ').split()
        data_price(cur, int(price_one), int(price_two))
    elif int(user) == 4:
        name_citi = input('Выберите город: ')
        data_citi(cur, name_citi)
    elif int(user) == 5:
        user_name = input('Укажите имя из базы: ')
        price = int(input('Укажите стоимость'))
        data_user_price(cur, name=user_name, price=price)

    conn.close()
    cur.close()


if __name__ == '__main__':
    main()
