"""
election_scrapper.py: My 3rd project for the Engeto Academy

author: Michal Trumpich
e-mail: michal.trumpich@gmail.com
discord: Michal T.#8572
"""○○

import os

# modules
from projekt_3.scrapping.soup import get_region_name
from projekt_3.export.csv import export_to_csv
from projekt_3.scrapping.join_data import scrap_data


def election_scrapper(link: str, file_name: str) -> None:
    """
    Main function for the election scrapper that takes 2 param and calls 1 function to scrap the data
     and 2nd function to export the data to a file
    :param link:
    :param file_name:
    :return:
    """
    scrap_data(link)
    export_to_csv(file_name)


# link for 2017 CZE election results
scrap_this = 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102'

# get region name which will be used in the .csv file name
region = get_region_name(scrap_this)
export_to = f'results{os.sep}vysledky_{region}.csv'

# start main function
election_scrapper(scrap_this, export_to)
