"""
Main modules to use for joining data together
(code, location, city details and number of votes for each party in each city)
"""

import time

from bs4 import ResultSet
from projekt_3.export.json import dump_json
from projekt_3.scrapping.soup import get_city_overall_details, get_all_tr, base_link, get_city_details_link, \
    get_city_code, get_city_name, get_titles_from_overall_details, get_city_party_votes


def scrap_data(link: str) -> None:
    """
    After starting the timer function will try to get all <tr> inside the main link
     that will be used throughout the function.

    It will then go through all of <tr>'s and will try to get a link where further details are located at.
    Function will continue if link is successfully extracted. Otherwise, will go to the next <tr>.

    If no error occurs then new row will be created inside dict 'data' with city code and name
    and will continue with extracting details about the city
     - total number of registered people, number of envelopes, number of votes for each party,...

    Function checks whether in the first detail link there arent additional 'orksky'
     if yes it will extract the links for each okrsek and puts it into list 'links'.
     If there are not 'okrsky' in the 'detailed_link' then only the 'detailed_link' will be added into the list 'links'
     It will then loop through all the links and will pop used link after each loop.

    Data will be dumped to json after the successful extraction of all the necessary data
     and total of time of how long program took to extract and dump the data will be printed.
    :param link: 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103'
    :return: None
    """
    start_time = time.time()
    region_all_tr = get_all_tr(link)
    print('Scrapping data...')
    data = {}
    row = 1
    base_url = base_link(link)
    for tr in region_all_tr:
        try:
            details_link = get_city_details_link(tr, base_url)
        # Print error if details link cant be extracted
        except AttributeError as atr_e:
            # print(atr_e, '- details_link not available', tr, '-' * 50, sep='\n')
            pass

        # if details_link could be extracted then visit that link
        # and try to find if there are additional sub_links (okrsky)
        else:
            # create new row with city details
            data[row] = {
                'code': get_city_code(tr),
                'location': get_city_name(tr),
                'registered': 0,
                'envelopes': 0,
                'valid': 0
            }

            all_td = get_all_tr(details_link)[1].find_all('td', {'class': 'cislo'})
            links = [base_url + td.find('a', href=True)['href'] for td in all_td]
            if not links:
                links.append(details_link)

            # go through all of extracted links and sum data for all sub_regions (if there are any)
            while links:
                city_details_all_tr = get_all_tr(links[0])

                # extract titles from the overall city details (no. of registered people, no. of envelopes...)
                titles_in_detail_data = get_titles_from_overall_details(city_details_all_tr)
                data[row].update(
                    update_data_with_city_overall_details(
                        data[row],
                        city_details_all_tr,
                        titles_in_detail_data
                    )
                )
                # update row with party names and their respective votes in each city
                data[row].update(
                    update_data_with_city_party_votes(
                        data,
                        city_details_all_tr
                    )
                )

                # remove link that was used in this round
                links.pop(0)
                # pprint(data)

            row += 1

    dump_json(data)
    total_time = round(time.time() - start_time, 2)
    print(f'Data extracted and dumped into json in {total_time}s.')


def update_data_with_city_overall_details(
        row_data: dict,
        city_details_all_tr: list,
        titles_in_detail_data: list
) -> dict:

    """
    Will try to extract data about registered people, total number of envelopes and how many were valid.
    Function will update the dict 'row_data' and returns it back to the caller.

    :param row_data: data for row that I want to add the data to
    :param city_details_all_tr: list of all <tr>'s for the city in current row
    :param titles_in_detail_data: extracted titles from city overview
    :return: updated row dictionary with number of registered people, number of envelopes and how many were valid
    """
    try:
        city_details = get_city_overall_details(city_details_all_tr, titles_in_detail_data)
        row_data['registered'] += int(city_details['registered'])
        row_data['envelopes'] += int(city_details['envelopes'])
        row_data['valid'] += int(city_details['valid'])
    except TypeError as type_e:
        # print(type_e, city_details_all_tr, '-' * 50, sep='\n')
        pass
    except ValueError as val_e:
        # try to find which values were not correct and print them out
        city_details = get_city_overall_details(city_details_all_tr, titles_in_detail_data)
        bol = {
            details: city_details[details]
            for details in city_details
            if not city_details[details].isnumeric()
        }
        print(val_e, ' - city_details are in the wrong format (not a number)', bol, '-' * 50, sep='\n')
    finally:
        # either way return back row_data (even if data are the same because of the error
        return row_data


def update_data_with_city_party_votes(
        row_data: list,
        city_details_all_tr: list
) -> dict:
    """
    Extracts data from each city about the political parties - name and number of votes they got.
    Will check if that party name is already there (for when there is more then 1 'okrsek').
     If party name is not there yet then add number of votes in that city/okrsek.
     If party name is already added there then add number of votes from this okrsek to total number of votes for that party

    :param row_data: data for row that I want to add the data to
    :param city_details_all_tr: list of all <tr>'s for the city in current row
    :return: {party: number of votes}
    """
    party_data = get_city_party_votes(city_details_all_tr)
    return {
        party: (
            party_data[party]
            if party not in row_data
            else row_data[party] + party_data[party]
        )
        for party in party_data
    }
