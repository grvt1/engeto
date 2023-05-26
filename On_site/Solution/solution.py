import json
import csv
import os
from pprint import pprint


rel_cesta = 'data/'
zadouci_klice = ('first_name', 'last_name', 'email')

def json_to_csv():
    jsony = najdi_jsony(rel_cesta)
    obsah_jsonu = [filtr(zaznam) for soubor in jsony for zaznam in precti_json(soubor)]
    zapis_csv('result.csv', obsah_jsonu)


def zapis_csv(cilovy_soubor, zaznamy):
    print(f'Saving zaznamy to {cilovy_soubor}')
    with open(cilovy_soubor, 'w', encoding='UTF-8', newline='') as csv_vystup:
        zapis = csv.DictWriter(csv_vystup, fieldnames=zaznamy[0].keys())
        zapis.writeheader()
        zapis.writerows(zaznamy)


def filtr(puvodni_zaznam):
    vyfiltrovany_obsah = {}
    for klic in puvodni_zaznam.keys():
        if klic not in zadouci_klice:
            continue
        vyfiltrovany_obsah[klic] = puvodni_zaznam[klic]

    return vyfiltrovany_obsah


def precti_json(nazev):
    print(f'Loading: {nazev}')
    try:
        with open(rel_cesta + nazev, 'r', encoding='UTF-8') as file:
            json_file = json.load(file)
    except FileNotFoundError:
        print(f'{rel_cesta + nazev} not found.')
    else:
        return json_file


def najdi_jsony(adresar: str):
    return [
        jmeno
        for jmeno in os.listdir(adresar)
        if os.path.splitext(jmeno)[-1] == '.json' and '_' in jmeno
    ]


if __name__ == '__main__':
    json_to_csv()