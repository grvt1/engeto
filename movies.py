import datetime

oddelovac = "=" * 62

sluzby = ("dostupne filmy", "detaily filmu", 'reziseri', "doporuc film")

uzivatele = \
    {
        "tomas": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
        "petr": {"The Godfather", "The Dark Knight"},
        "marek": {"The Dark Knight", "The Prestige"}
    }

film_1 = \
    {
        "JMENO": "Shawshank Redemption",
        "HODNOCENI": "93/100",
        "ROK": 1994,
        "REZISER": "Frank Darabont",
        "STOPAZ": 144,
        "HRAJI":
            (
                "Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
                "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
                "Jeffrey DeMunn", "Larry Brandenburg"
            )
    }

film_2 = \
    {
        "JMENO": "The Godfather",
        "HODNOCENI": "92/100",
        "ROK": 1972,
        "REZISER": "Francis Ford Coppola",
        "STOPAZ": 175,
        "HRAJI":
            (
                "Marlon Brando", "Al Pacino", "James Caan",
                "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
                "John Marley", "Richard Conte"
            )
    }

film_3 = \
    {
        "JMENO": "The Dark Knight",
        "HODNOCENI": "90/100",
        "ROK": 2008,
        "REZISER": "Christopher Nolan",
        "STOPAZ": 152,
        "HRAJI":
            (
                "Christian Bale", "Heath Ledger", "Aaron Eckhart",
                "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
                "Monique Gabriela", "Ron Dean", "Cillian Murphy"
            )
    }

film_4 = \
    {
        "JMENO": "The Prestige",
        "HODNOCENI": "85/100",
        "ROK": 2006,
        "REZISER": "Christopher Nolan",
        "STOPAZ": 130,
        "HRAJI":
            (
                "Hugh Jackman", "Christian Bale", "Michael Caine",
                "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
                "David Bowie"
            )
    }


# check name and quit if there is no match
def check_name():
    name = input('Vyber jmeno: ')
    if name not in uzivatele:
        print('Neregistrovany uzivatel!')
        quit()

    else:
        global logged_in_user
        logged_in_user = name
        print('Vse v poradku!\n')
        print(oddelovac)
        print('VITEJTE V NASEM FILMOVEM SLOVNIKU!'.center(len(oddelovac)))
        print(oddelovac)
        print(f"| {' | '.join(sluzby)} |".center(len(oddelovac)))
        print(oddelovac)

        # if name is correct then continue to choose a service
        choose_a_service = input('Vyber sluzbu: ')
        check_choice(choose_a_service)


# check choice and quit if there is no match, otherwise execute the choice
def check_choice(choice):
    if choice not in sluzby:
        print('Vybrana sluzba neni v nabidce, ukoncuji..')
        print(oddelovac)
        quit()

    elif choice == 'dostupne filmy':
        show_movies_available()

    elif choice == 'detaily filmu':
        show_movies_available()
        chosen_movie = choose_a_movie()
        show_movie_details(chosen_movie)

    elif choice == 'reziseri':
        show_movie_directors()

    elif choice == 'doporuc film':
        recommend_a_movie()


# print available movies
def show_movies_available():
    movies_available_list = list(filmy.keys())
    movies_available = ''
    for i in movies_available_list:
        movies_available += i
        if movies_available_list.index(i) < len(movies_available_list) - 1:
            movies_available += ', '

    print(f'DOSTUPNE FILMY: {movies_available}')


# ask user to choose a movie
def choose_a_movie():
    chosen_movie = input('Vyber film: ')
    print(oddelovac)
    print(f'FILM: {chosen_movie}')

    check_if_movie_exists(chosen_movie)

    return chosen_movie


# check if movie is available
def check_if_movie_exists(chosen_movie):
    if chosen_movie not in filmy:
        print('Takovy film neni ve slovniku')
        print(oddelovac)
        quit()


# show details of the chosen movie
def show_movie_details(chosen_movie):
    for i in filmy[chosen_movie]:
        if i == 'HRAJI':
            actors = ''
            for y in filmy[chosen_movie][i]:
                actors += y
                actors += ', '
            actors = actors[:-2]
            print(f'{i}: {actors}')
        else:
            print(f'{i}: {filmy[chosen_movie][i]}')

    print(oddelovac)


# show all movie directors available
def show_movie_directors():
    print(oddelovac)

    directors = ''
    for i in filmy:
        if filmy[i]['REZISER'] not in directors:
            directors += filmy[i]['REZISER']
            directors += ', '
    directors = directors[:-2]
    print(f'Reziseri: {directors}')


# send an email with recommendation to a friend
def recommend_a_movie():
    print(oddelovac)
    recommending_to = input('Jmeno kamarada/ky: ')
    send_to = input('E-mail kamarada/ky: ')
    check_email_domain = '.' not in send_to.split('@')[1] if '@' in send_to else True
    while '@' not in send_to or check_email_domain:
        if '@' not in send_to:
            print('Email musi obsahovat \'@\''.center(len(oddelovac)))

        elif check_email_domain:
            print('Neplatny format domeny!'.center(len(oddelovac)))

        send_to = input('\nE-mail kamarada/ky: ')
        check_email_domain = '.' not in send_to.split('@')[1] if '@' in send_to else True

    # choose a movie to recommend a friend
    print(oddelovac)
    print('Jaky film chces doporucit?')
    show_movies_available()
    chosen_movie = choose_a_movie()
    print(oddelovac)

    # send movie details to a friend
    print(f'Ahoj {recommending_to.capitalize()}!,')

    # convert first X actors to a string then print hodnoceni and reziser
    pick_actors = ''
    pick_how_many_actors = 5
    for i in range(0, pick_how_many_actors):
        pick_actors += filmy[chosen_movie]['HRAJI'][i]
        if i == pick_how_many_actors - 2:
            pick_actors += ' a '
        if i <= pick_how_many_actors - 3:
            pick_actors += ', '
    print(f'\nMrkni na engeto.tv na {chosen_movie}! Mimo jine tam hraji {pick_actors}.')
    print(f'Ma to hodnoceni {filmy[chosen_movie]["HODNOCENI"]}. '
          f'Reziroval to jedinecny {filmy[chosen_movie]["REZISER"]}.')

    # print a msg based on whether movie is too old or not
    movie_length = filmy[chosen_movie]["STOPAZ"]
    current_year = int(str(datetime.date.today()).split('-')[0])
    movie_premiere_year = filmy[chosen_movie]["ROK"]
    how_old_is_the_movie = current_year - movie_premiere_year
    what_is_too_old = 15
    too_old = True if how_old_is_the_movie > what_is_too_old else False
    if too_old:
        print(f'Film je sice {how_old_is_the_movie} let stary (premiera byla v roce {movie_premiere_year}), '
              f'ale urcite tech {movie_length} minut stalo za to!')
    else:
        if how_old_is_the_movie >= 5:
            let = 'let'
        elif 1 <= how_old_is_the_movie <= 4:
            let = 'roky'
        else:
            let = 'rok'

        print(f'Film je jenom {how_old_is_the_movie} {let} stary (premiera byla v roce {movie_premiere_year}),'
              f'a tech {movie_length} minut stalo urcite za to!')

    # printing farewell
    print('\nDoufam, ze si film uzijes tak, jako jsem si ho uzil ja!')
    print(f'\nS pozdravem,\n\n', logged_in_user.capitalize().center(len(oddelovac)))
    print(oddelovac)


filmy = \
    {
        film_1['JMENO']: film_1,
        film_2['JMENO']: film_2,
        film_3['JMENO']: film_3,
        film_4['JMENO']: film_4
    }

# start program by calling a function to check if name is correct
logged_in_user = ''
check_name()
