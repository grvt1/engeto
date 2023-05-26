import os
from pprint import pprint
from typing import Any, Generator


def spust_prevadeni(soubor: str, slovnik: dict):
    if os.path.isfile(soubor):
        print('Spoustim prevod: ')
        prevedena_data = iteruj_pres_vsechna_data(otevri_soubor(soubor), slovnik)
        for nemovitost in prevedena_data:
            print(nemovitost)
    else:
        print('Soubor neexistuje')


def iteruj_pres_vsechna_data(data: list, slovnik: dict) -> set:
    return {
        prepis_novy_typ_bytu(line, slovnik)
        for line in data
    }


def otevri_soubor(soubor: str) -> list:
    with open(soubor, mode='r', encoding='UTF-8') as f:
        return f.readlines()


def prepis_novy_typ_bytu(line: str, slovnik: dict) -> str:
    dispozice, *zbytek = line.replace('\n', '').split(',', 1)
    novy_zapis = slovnik.get(dispozice, 'Dispozice nezname')
    return ','.join((novy_zapis, ','.join(zbytek)))


def prevod_bytu():

    abs_cesta = f'{os.getcwd()}{os.sep}solution{os.sep}vstupni_data.txt'

    prevodni_vzor = {
        "byt0001": "1+1",
        "byt0002": "2+1",
        "byt0003": "2+kk",
        "byt0004": "3+1",
        "byt0005": "3+kk",
        "byt0006": "4+1",
        "byt0007": "4+kk",
    }

    spust_prevadeni(abs_cesta, prevodni_vzor)


if __name__ == '__main__':
    prevod_bytu()