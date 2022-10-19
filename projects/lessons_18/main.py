import psycopg2
from config import *
from psycopg2 import Error


def db_connect():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
            port=port
        )
        print('Good')
        connection.autocommit = True

        return connection

    except Error as _ex:
        print('Error!', _ex)
        return False


def creat_shelter_info(cur):
    request = """
    CREATE TABLE IF NOT EXISTS shelter_info(
    id_shelter_info integer PRIMARY KEY,
    fk_animal_id integer REFERENCES animal_dict(id),
    fk_id_outcome_subtype integer REFERENCES outcome_subtype(id_outcome_subtype),
    outcome_month integer,
    outcome_year integer,
    fk_outcome_type integer REFERENCES outcome_type(id_outcome_type),
    age_upon_outcome varchar(255)
    )
    """
    cur.execute(request)


def entry_shelter_info(cur):
    request = """
    INSERT INTO shelter_info(id_shelter_info, fk_animal_id, fk_id_outcome_subtype, outcome_month, outcome_year, 
    fk_outcome_type, age_upon_outcome)
    SELECT main_animals.index, animal_dict.id, outcome_subtype.id_outcome_subtype, main_animals.outcome_month, 
    main_animals.outcome_year, outcome_type.id_outcome_type, main_animals.age_upon_outcome
    FROM main_animals LEFT JOIN animal_dict ON main_animals.animal_id = animal_dict.animal_id
    LEFT JOIN outcome_subtype ON main_animals.outcome_subtype = outcome_subtype.name_outcome_subtype
    LEFT JOIN outcome_type ON main_animals.outcome_type = outcome_type.name_outcome_type
    GROUP BY main_animals.index, animal_dict.id, outcome_subtype.id_outcome_subtype, main_animals.outcome_month, 
    main_animals.outcome_year, outcome_type.id_outcome_type, main_animals.age_upon_outcome
    """
    cur.execute(request)


def creat_animal_dict(cur):
    request = """
    CREATE TABLE IF NOT EXISTS animal_dict(
    id SERIAL PRIMARY KEY,
    animal_id varchar(255),
    fk_animal_type integer REFERENCES type_dict(id_type),
    name_kl varchar(255),
    fk_bread integer REFERENCES breed_dict(id_bread),
    fk_color1 integer REFERENCES colour_dict(id_colour),
    fk_color2 integer REFERENCES colour_dict(id_colour)
    )
    """
    cur.execute(request)


def entry_animal_dict(cur):
    request = """
    INSERT INTO animal_dict(animal_id, fk_animal_type, name_kl,  fk_bread, fk_color1, fk_color2)
    SELECT main_animals.animal_id, type_dict.id_type, main_animals.name, breed_dict.id_bread, a.id_colour, b.id_colour
    FROM  main_animals LEFT JOIN type_dict ON main_animals.animal_type = type_dict.name_type
    LEFT JOIN breed_dict ON main_animals.breed = breed_dict.name_breed
    LEFT JOIN colour_dict as a ON main_animals.color1 = a.name_colour
    LEFT JOIN colour_dict as b ON main_animals.color2 = b.name_colour
    GROUP BY main_animals.animal_id, type_dict.id_type, main_animals.name, breed_dict.id_bread, a.id_colour, b.id_colour
    """
    cur.execute(request)


def creat_type_dict(cur):
    request = """
    CREATE TABLE IF NOT EXISTS type_dict(
    id_type SERIAL PRIMARY KEY,
    name_type varchar(255)
    )
    """
    cur.execute(request)


def entry_type_dict(cur):
    request = """
    INSERT INTO type_dict(name_type)
    SELECT DISTINCT animal_type FROM main_animals
    """
    cur.execute(request)


def creat_breed_dict(cur):
    request = """
    CREATE TABLE IF NOT EXISTS breed_dict(
    id_bread SERIAL PRIMARY KEY,
    name_breed varchar(255)
    )
    """
    cur.execute(request)


def entry_breed_dict(cur):
    request = """
    INSERT INTO breed_dict(name_breed)
    SELECT DISTINCT breed FROM main_animals
    """
    cur.execute(request)


def creat_colour_dict(cur):
    request = """
    CREATE TABLE IF NOT EXISTS colour_dict(
    id_colour SERIAL PRIMARY KEY,
    name_colour varchar(255)
    )
    """
    cur.execute(request)


def entry_colour_dict(cur):
    request = """
    INSERT INTO colour_dict(name_colour)
    SELECT DISTINCT color1 FROM main_animals
    """
    cur.execute(request)


def creat_outcome_subtype(cur):
    request = """
    CREATE TABLE IF NOT EXISTS outcome_subtype(
    id_outcome_subtype SERIAL PRIMARY KEY,
    name_outcome_subtype varchar(255)
    )
    """
    cur.execute(request)


def entry_outcome_subtype(cur):
    request = """
    INSERT INTO outcome_subtype(name_outcome_subtype)
    SELECT DISTINCT outcome_subtype FROM main_animals
    """
    cur.execute(request)


def creat_outcome_type(cur):
    request = """
    CREATE TABLE IF NOT EXISTS outcome_type(
    id_outcome_type SERIAL PRIMARY KEY,
    name_outcome_type varchar(255)
    )
    """
    cur.execute(request)


def entry_outcome_type(cur):
    request = """
    INSERT INTO outcome_type(name_outcome_type)
    SELECT DISTINCT outcome_type FROM main_animals
    """
    cur.execute(request)


def user_add(cur):
    request = """
    GRANT SELECT ON ALL TABLES IN SCHEMA animal_world TO user2;
    GRANT USAGE ON SCHEMA animal_world TO user2;
    """
    cur.execute(request)


if __name__ == '__main__':
    conn = db_connect()
    cursor = conn.cursor()
    creat_type_dict(cursor)
    creat_breed_dict(cursor)
    creat_colour_dict(cursor)
    creat_outcome_subtype(cursor)
    creat_outcome_type(cursor)
    creat_animal_dict(cursor)
    creat_shelter_info(cursor)

    entry_type_dict(cursor)
    entry_breed_dict(cursor)
    entry_colour_dict(cursor)
    entry_outcome_subtype(cursor)
    entry_outcome_type(cursor)
    entry_animal_dict(cursor)
    entry_shelter_info(cursor)

