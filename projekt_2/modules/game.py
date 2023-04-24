import random
import time

# modules
from projekt_2.modules.change_str import add_s
from projekt_2.modules.check_syntax import check_all
from projekt_2.modules.greetings import longest_str, print_dict
from projekt_2.modules.high_score import save_high_score_question, save_high_score, show_high_scores


def new_game(username: str) -> None:
    """
    This functions controls main game. User will be asked to enter a new guess until bulls != 4
    Inputs will be checked along the way for correct syntax, guesses and time is counted.
    After winning user will be asked if user wants to save the high score. If user says yes then high score will be saved
    and high score of default 20 people will be shown
    :param username: michal
    :return: None
    """
    # generate number and wait for user to enter any key to start the game
    generated_number = generate_number()
    input('Enter any key to start the timer: ')
    print(generated_number)
    start_time = time.time()
    no_of_guesses = 0
    while True:
        no_of_guesses += 1
        guess = user_guess(no_of_guesses)  # calls a function that writes what guess number this is + checks syntax

        total_time = round(time.time() - start_time, 2)  # total time since starting the game

        result = check_bulls_and_cows(guess, generated_number)  # checks for any bulls and cows
        if result:  # if user guesses the number correctly then show score, how many guesses it took and time spent
            score = str(int((total_time + no_of_guesses)*100))
            win(no_of_guesses, start_time, score)
            if save_high_score_question():  # ask user if user wants to save the score, if yes then save and show top 20
                save_high_score(username, no_of_guesses, total_time, score)
                show_high_scores()
            break
        print(f' - Time: {total_time}s')


def generate_number() -> str:
    """
    Generates a list of 4 digits from a sample of 1-9.
    List is then converted to an integer via .join
    :return: 6954
    """
    generate_4_dig = ''.join(repr(int(n)) for n in random.sample(range(1, 10), 4))

    return generate_4_dig


def user_guess(guess_number: int) -> str:
    """
    Ask user to enter a guess that will be analyzed via the check class
    User will be asked to enter a new guess until the text
    :param guess_number: 1
    :return: True once the syntax will be correct
    """
    while True:
        guess = input(f'\nGuess {guess_number}: ')

        if check_all(guess):
            break

    return guess


def check_bulls_and_cows(user_guessed: str, generated_number: str) -> bool:
    """
    Compares param user_guessed with param generated_number and prints out no. of bulls and cows
    bulls: count of numbers in param user_guessed that are also in param generated_number and that are on the same index
    cows: count of numbers that are also in param generated_number
    returns True once bulls count is equal to 4 (meaning user guessed correctly the generated_number)
    :param user_guessed: 1234
    :param generated_number: 1253
    prints: ' - 2 bulls / 3 cows'
    :return: False
    """
    bulls = 0
    cows = 0
    for i in user_guessed:
        if i in generated_number:
            cows += 1
            if user_guessed.index(i) == generated_number.index(i):
                bulls += 1

    print(f' - {bulls} {add_s(bulls, "bull")} / {cows} {add_s(cows, "cow")}')
    return True if bulls == 4 else False


def win(no_of_guesses: int, start_time: float, score: str) -> None:
    """
    Prints number of guesses and total time it took user to guess the number
    """
    total_time = round(time.time() - start_time, 2)
    print('\nYou have guessed the number!\nCongratulations!')
    print(f' - It took you {no_of_guesses} {add_s(no_of_guesses, "guess")} and {total_time}s.')
    print(f' - Your total score is: {score}')


def what_now() -> bool:
    """
    Prints possible options for the user. User will be asked until user provides one of the possible options
    :return: 'quit' or 'new game'
    """
    # define what I want to print
    title = {'title': 'Now you have 3 options to choose from.'}
    possible_choices = {
        'quit': '1) If you fear another round you can ofcourse quit (type ,,quit")',
        'high score': '2) You can look at high scores (type ,,high score")',
        'new game': '3) Or if you are brave enough you can start again with a new number (type ,,new game")'
    }
    separator = '-'*longest_str(possible_choices)

    while True:
        # print title + possible choices
        print_dict(title, separator, separator_at_start=True, separator_at_end=False)
        print_dict(possible_choices, separator, separator_at_start=False, separator_at_end=False)

        # ask user for input until user enters one of the keys in dict possible_choices
        while (next_step := input('What will it be? ').lower()) not in possible_choices:
            print('Wrong input. I can only take: ')
            for choice in possible_choices:
                print(f' - {choice}'.title())
            next_step = input('What will it be? ').lower()
        print(separator)

        # if user chooses high score then print high score table
        if next_step == 'high score':
            show_high_scores()
        elif next_step == 'quit':
            print('Hm,.. Afraid to loose I see. Come back when you gather up some courage.')

        # break away from this function only if user chooses to quit or new game
        if next_step == 'quit' or next_step == 'new game':
            return False if next_step == 'new game' else True
