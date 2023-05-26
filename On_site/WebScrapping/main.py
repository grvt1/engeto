from pprint import pprint
from time import sleep

import requests
from bs4 import BeautifulSoup, Tag


def main():
    page = 1
    max_page = 1
    titles = []
    body = {}

    while True:
        all_tr = get_table_tag_top(page).find_all('tr')

        if max_page == 1:

        if not titles:
            titles = get_titles(all_tr[0])

        for tr in all_tr[1:]:
            td_data = tr.find_all('td')
            rank = td_data[0].get_text()
            td_text = []
            for td in td_data:
                td_text.append(td.get_text())

            body[rank] = {}
            for title in titles:
                body[rank][title] = td_text[titles.index(title)]

        if page == 93:
            break
        page += 1


def get_url(page: int = 1):
    return f'https://heroes3.cz/hraci/index.php?page={page}&order=0&razeni=DESC'


def load_soup(page):
    return BeautifulSoup(requests.get(get_url(page)).text, 'html.parser')


def get_table_tag_top(page):
    return load_soup(page).find('table', {'class': 'tab_top'})


def get_titles(first_tr: Tag):
    return [
        str(td.get_text()).lower()
        for td in first_tr.find_all('th')
    ]



main()