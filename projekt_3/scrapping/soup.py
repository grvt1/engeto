"""
Here all the functions that are used to extract data from the page are located.
"""

import requests
from bs4 import BeautifulSoup, Tag, ResultSet


def load_soup(link: str) -> BeautifulSoup:
    """
    Loads links via bs4
    :param link: 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103'
    :return: BeautifulSoup
    """
    try:
        return BeautifulSoup(requests.get(link).text, 'html.parser')
    except Exception as e:
        print(e)
        print('Wrong link. Exiting program.')
        quit()


def get_div_publikace(link: str) -> Tag:
    """
    Loads <div class='publikace'> from selected link
    :param link: 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103'
    :return:
    """
    return load_soup(link).find('div', {'id': 'publikace'})


def get_all_tr(link: str) -> list:
    """
    Loads all tr in <div class='publikace'> from the link and returns it as a list
    :param link: 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103'
    :return: list of all trs inside <div class='publikace'>
    """
    return get_div_publikace(link).find_all('tr')


def base_link(link: str) -> str:
    """
    Takes link and deletes everything after last '/'.
    :param link: 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103'
    :return: 'https://volby.cz/pls/ps2017nss/'
    """
    return '/'.join(link.split('/')[:-1]) + '/'


def get_region_name(link: str) -> str:
    """
    Calls function that loads <div class='publikace'> and extracts 'okres' from the page.
    Will be used for creating file name.
    :param link: 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103'
    :return: 'Prostějov'
    """
    return get_div_publikace(link).find_all('h3')[1].get_text().split()[1].lower()


def get_titles_from_overall_details(all_tr: list) -> list:
    """
    Goes to city details and extracts titles from first table where overall city details are stored.
    Will skip ,,Okrsky'' title because that one is redundant.
    :param all_tr: <tr>
                    <th colspan="3" id="sa1">Okrsky</th>
                    <th data-rel="L1" id="sa2" rowspan="2">Voliči<br/>v seznamu</th>
                    <th data-rel="L1" id="sa3" rowspan="2">Vydané<br/>obálky</th>
                    <th id="sa4" rowspan="2">Volební<br/>účast v %</th>
                    <th data-rel="L1" id="sa5" rowspan="2">Odevzdané<br/>obálky</th>
                    <th data-rel="L1" id="sa6" rowspan="2">Platné<br/>hlasy</th>
                    <th id="sa7" rowspan="2">% platných<br/>hlasů</th>
                    </tr>, <tr>
                    <th id="sb1">celkem</th>
                    <th id="sb2">zpr.</th>
                    <th id="sb3">v %</th>
                   </tr>
    :return: ['celkem', 'zpr.', 'v %', 'Voliči v seznamu', 'Vydané obálky', 'Volební účast v %', 'Odevzdané obálky', 'Platné hlasy', '% platných hlasů']
    """
    return [
        th.get_text(separator=' ')
        for tr in all_tr[1::-1]
        for th in tr.find_all('th')
        if th.get_text() != 'Okrsky'
    ]


def get_city_overall_details(all_tr: list, titles: list) -> dict:
    """
    Will extract overall city details (from first table on city details).
    Will try to find them in row 2 but if it fails then function will go to row 1 (there are two types of city details).
    Returns only data from 'Voliči v seznamu', 'Vydané obálky' and 'Platné hlasy'.
    :param all_tr:  <tr>
                        <td class="cislo" headers="sa1 sb1">1</td>
                        <td class="cislo" headers="sa1 sb2">1</td>
                        <td class="cislo" headers="sa1 sb3">100,00</td>
                        <td class="cislo" data-rel="L1" headers="sa2">205</td>
                        <td class="cislo" data-rel="L1" headers="sa3">145</td>
                        <td class="cislo" headers="sa4">70,73</td>
                        <td class="cislo" data-rel="L1" headers="sa5">145</td>
                        <td class="cislo" data-rel="L1" headers="sa6">144</td>
                        <td class="cislo" headers="sa7">99,31</td>
                    </tr>
    :param titles: ['Voliči v seznamu',
                    'Vydané obálky',
                    'Volební účast v %',
                    'Odevzdané obálky',
                    'Platné hlasy',
                    '% platných hlasů']

    :return: {'% platných hlasů': '99,29',
              'Odevzdané obálky': '283',
              'Platné hlasy': '281',
              'Volební účast v %': '66,51',
              'Voliči v seznamu': '427',
              'Vydané obálky': '284',
              'celkem': '1',
              'v %': '100,00',
              'zpr.': '1'}
    """
    try:
        city_statistics = [td.get_text() for td in all_tr[2].find_all('td')]
        if not city_statistics:
            city_statistics = [td.get_text() for td in all_tr[1].find_all('td')]
    except IndexError as ind_e:
        # print(ind_e)
        pass
    else:
        combine_titles_and_statistics = dict(zip(titles, city_statistics))
        return {'registered': combine_titles_and_statistics['Voliči v seznamu'].replace('\xa0', ''),
                'envelopes': combine_titles_and_statistics['Vydané obálky'].replace('\xa0', ''),
                'valid': combine_titles_and_statistics['Platné hlasy'].replace('\xa0', '')
                }


def get_city_code(tr: Tag) -> str:
    """
    Extracts city code (PSČ) from base link
    :param tr:  <tr>
                    <td class="cislo" headers="t1sa1 t1sb1"><a href="ps311?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103">506761</a></td>
                    <td class="overflow_name" headers="t1sa1 t1sb2">Alojzov</td>
                    <td class="center" headers="t1sa2"><a href="ps311?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103">X</a></td>
                </tr>
    :return: '506761'
    """
    return tr.find('td', {'class': 'cislo'}).get_text()


def get_city_name(tr: Tag) -> str:
    """
    Extracts city name from base link and returns it.
    :param tr:  <tr>
                    <td class="cislo" headers="t1sa1 t1sb1"><a href="ps311?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103">506761</a></td>
                    <td class="overflow_name" headers="t1sa1 t1sb2">Alojzov</td>
                    <td class="center" headers="t1sa2"><a href="ps311?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103">X</a></td>
                </tr>
    :return: 'Alojzov'
    """
    return tr.find('td', {'class': 'overflow_name'}).get_text()


def get_city_details_link(tr: Tag, base_url: str) -> str:
    """
    Extracts <a href=''> link for city details (marked with 'x') and returns it as a full link.

    :param tr:  <tr>
                    <td class="cislo" headers="t1sa1 t1sb1"><a href="ps311?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103">506761</a></td>
                    <td class="overflow_name" headers="t1sa1 t1sb2">Alojzov</td>
                    <td class="center" headers="t1sa2"><a href="ps311?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103">X</a></td>
                </tr>
    :param base_url: 'https://volby.cz/pls/ps2017nss/'
    :return: 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103'
    """
    return base_url + tr.find('td', {'class': 'center'}).find('a', href=True)['href']


def get_city_party_votes(all_tr: list) -> dict:
    """
    Function that will go through city details and collect party name and number of votes
    :param all_tr: page for city details where the number of votes for each party are located
    :return: party_name: number of votes
    """
    party_votes = {}
    for tr in all_tr:
        try:
            all_td = tr.find_all('td')
            name = tr.find('td', {'class': 'overflow_name'}).get_text()
            votes = all_td[2].get_text()
        except AttributeError as atr_e:
            # print(atr_e, '- <td class=\'overflow_name\' not available', tr, '-' * 50, sep='\n')
            pass
        else:
            if name != '-':
                party_votes[name] = votes
    return party_votes
