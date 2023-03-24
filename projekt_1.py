"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Trumpich

email: michal.trumpich@gmail.com

discord: Michal T.#8572
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''
At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''
The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']


class main:
    separator = '-' * 60
    user_information = {
        'bob': 123,
        'ann': 'pass123',
        'mike': 'password123',
        'liz': 'pass123'
    }

    def __init__(self):
        super(main, self).__init__()
        self.enter_credentials()

    # DONE ask user for username and password
    def enter_credentials(self):
        entered_username = input('Username: ')
        entered_password = input('Password: ')
        self.check_credentials(entered_username, entered_password)

    # DONE check and greet user if username/password matches, quit program otherwise
    def check_credentials(self, username, password):
        check_username = username.lower() in self.user_information
        check_password = False if not check_username else str(password) == str(self.user_information[username])
        if check_username and check_password:
            print(self.separator,
                  '\n' + f'Welcome to the app, {username}'.center(len(self.separator)),
                  '\n' + 'We have 3 texts to be analyzed.'.center(len(self.separator)),
                  '\n' + self.separator)
            self.choose_text_to_analyze()

        else:
            print('unregistered user, terminating the program..')
            quit()

    # DONE enable user to analyze texts and ask user for a valid input until user provides one
    def choose_text_to_analyze(self):
        choose_text = input('Enter a number between 1 and 3 to select: ')
        input_is_numeric = choose_text.isnumeric()
        input_is_wrong_number = False if not input_is_numeric else 1 > int(choose_text) or int(choose_text) > 3
        while not input_is_numeric or input_is_wrong_number:
            choose_text = input('Invalid input: ')
            input_is_numeric = choose_text.isnumeric()
            input_is_wrong_number = False if not input_is_numeric else 1 > int(choose_text) or int(choose_text) > 3

        print(self.separator)
        self.analyze_text(int(choose_text)-1)

    # DONE analyze text and call function print_cases
    def analyze_text(self, selection):
        selected_text = TEXTS[selection]
        shaven_text = selected_text.replace('.', '').split()

        count = {
            'total': len(shaven_text),
            'titlecase': 0,
            'uppercase': 0,
            'lowercase': 0,
            'numeric': 0,
            'sum': 0
        }
        words_length = {}
        case_is = None
        for word in shaven_text:
            # count cases
            if word.istitle():
                case_is = 'titlecase'
            elif word.isupper():
                case_is = 'uppercase'
            elif word.islower():
                case_is = 'lowercase'
            elif word.isnumeric():
                case_is = 'numeric'
                count['sum'] += int(word)
            count[case_is] += 1

            # create a dict of all the different word lengths and their count - length: count
            length = len(word)
            if length in words_length:
                words_length[length] += 1
            else:
                words_length[length] = 1

        self.print_cases(count)
        self.print_words_length(words_length)

    # DONE print total words, cases and sum of all the numerics
    def print_cases(self, count):
        # print everything in the count var
        for i in count:
            beginning = 'There are '
            ending = ' ' + i + ' words.'
            if i == 'total':
                ending = ' words in the selected text.'
            elif i == 'numeric':
                ending = ' ' + i + ' strings.'
            elif i == 'sum':
                beginning = 'The sum of all the numbers is '
                ending = '.'

            print(f'{beginning}{count[i]}{ending}')
        print(self.separator)

    # DONE print length occurrences
    def print_words_length(self, words_length):
        highest_value = sorted(words_length.values(), reverse=True)[0]
        sorted_keys = sorted(words_length.keys())

        print('LEN|',
              'OCCURRENCES'.center(highest_value),
              '|NR.',
              '\n' + self.separator)

        for length in sorted_keys:
            # create text for len
            space_before_len = 3 - len(str(length))
            len_text = ' '*space_before_len + str(length) + '|'

            # create text for occurrences
            occurrences_text = '*'*words_length[length]

            # create text for nr
            space_before_nr = highest_value - words_length[length]
            nr_text = ' '*space_before_nr + '|' + str(words_length[length])

            # combine and print all
            print(len_text, occurrences_text, nr_text)


main()
