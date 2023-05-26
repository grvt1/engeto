"""
Here are the functions that are used for creating the .csv file
"""

import time
import csv

# modules
from projekt_3.export.json import load_json


def export_to_csv(file_path: str) -> None:
    """
    Exports data from 'json_data.json' to value of parameter 'file_path'.

    Function wil lat first try the selected path and quits if path is not correct.
    Function will then call another function to extract titles for headers
    and then will go row by row in 'all_json_data'.
    At the end program will print total time it took to export the data.
    :param file_path: 'results\vysledky_prostějov.csv'
    :return: None
    """
    # try if file_path is valid. Quit otherwise.
    try:
        with open(file_path):
            pass
    except FileNotFoundError as fil_e:
        print('Wrong file name/path for exporting. Exiting program.')
        quit()
    except OSError as os_e:
        print('Wrong file name/path for exporting. Exiting program.')
        quit()
    # continue with the program if file_path is valid.
    else:
        # Let user know that data are being currently exported to a selected file
        print(f'Exporting data to {file_path}...')
        # start the timer
        start_time = time.time()
        # extract header from json_data.json
        header = get_header()

        # use DictWriter to write all rows into the file
        with open(file_path, 'w', encoding='UTF-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=header)
            writer.writeheader()  # first write header
            all_json_data = load_json()  # then load json_data.json and write them inside the .csv one by one
            for row in all_json_data:
                writer.writerow(all_json_data[row])

        # print total time it took the function to finish
        total_time = round(time.time() - start_time, 2)
        print(f'Exported in {total_time}s.')


def get_header() -> list:
    """
    Goes through 'json_data.json' and finds all unique keys which will be used in the first row for the .csv file
    :return: set of all unique keys
    """
    all_data = load_json()
    return list(dict.fromkeys([
        title
        for row in all_data
        for title in all_data[row].keys()
    ]))