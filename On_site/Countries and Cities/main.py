import os
from pprint import pprint

txt_soubor = 'countries_and_cities.txt'


def nacti_txt_soubor(jmeno: str, encoding: str = 'UTF-8'):
    try:
        with open(jmeno, 'r', encoding=encoding) as txt:
            obsah = txt.readlines()
    except FileNotFoundError:
        error_file_not_found(jmeno)
    else:
        print(f'Soubor {jmeno} nacten.')
        return obsah
    finally:
        print('Ukoncuji funkci \'nacti_txt_soubor\'.\n')


def error_file_not_found(jmeno: str) -> None:
    print(f'Soubor \'{jmeno}\' neexistuje.',
          f'Aktualni adresar: {os.getcwd()}',
          f'Obsah adresare: {os.listdir()}',
          sep='\n'
          )


def zformatuj_nazvy(obsah: list):
    longest = nejdelsi_stat(obsah)
    for udaj in obsah:
        if udaj.lower() != 'quit':
            zeme, mesto = udaj.title().replace('\n', '').split(', ')
            print(f'{zeme=:<{longest}}',
                  f'{mesto=:}'
                  )


def nejdelsi_stat(obsah: list):
    zeme_list = [udaj.title().replace('\n', '').split(', ')[0] for udaj in obsah]
    return len(max(zeme_list, key=len))


if __name__ == '__main__':
    obsah = nacti_txt_soubor(txt_soubor)
    zformatuj_nazvy(obsah)
