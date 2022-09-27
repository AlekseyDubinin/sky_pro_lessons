from classes import *
import json


def data_collection(profession):

    hed = HH(profession)
    qw = hed.parser(url=hed.URL)
    hed2 = Superjob(profession)
    qw2 = hed2.parser(url=hed2.URL)
    qwers = qw + qw2

    with open('HH_vacancy.json', 'w') as file:
        json.dump(qwers, file, indent=4, ensure_ascii=False)

        print(len(qwers))


data_collection('Java')