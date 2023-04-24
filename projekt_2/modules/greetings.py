def greet_user(username) -> None:
    """
    Greets the user and prints out introduction.

    :param username: michal
    :return:
        Hi michal and welcome to the Bulls and Cows game!
        --------------------------------------------------------------------------------
        I've generated a random 4-digit number for you.
        .
        .
        .
        --------------------------------------------------------------------------------
    """
    greet_dict = {
        'greet': f'\nHi {username} and welcome to the Bulls and Cows game!',
        'what_I_did': "I've generated a random 4-digit number for you.",
        'what_user_needs_to_do': 'Your tasks will be to guess the number.',
        'hints_header': '\nI can straight away tell you that:',
        'hint_1': '  * Number does not start with a 0',
        'hint_2': '  * All numbers are unique (there are no two same numbers)',
        'alert': 'I will alert you if any of the above happens or if you will enter a non-integer.',
        'high_score': '\nYour total time and number of tries will be recorded',
        'high_score2': 'and if you will want you can have your results on the high score board.',
        'lets_play': "\nEnough of chitchat and let's play the game."
    }
    print_dict(greet_dict, '-'*longest_str(greet_dict), ['greet'], separator_at_end=True)


def print_dict(
        print_this: dict, separator: str,
        separator_after=None, separator_at_start=False, separator_at_end=False
) -> None:
    """
    Take dictionary and prints values.
    Possible to define if I want to print also a separator after certain keys or at start/end.
    :param print_this: dict of what I want to print
    :param separator: str of what I want to use as a separator
    :param separator_after: list of keys which I want to print a separator after
    :param separator_at_start: bool if I want to print separator before printing dictionary
    :param separator_at_end: bool if I want to print separator after printing dictionary
    :return: None
    """
    if separator_after is None:
        separator_after = list()

    if separator_at_start:
        print(separator)

    for value in print_this:
        print(print_this[value])
        if value in separator_after:
            print(separator)

    if separator_at_end:
        print(separator)


def longest_str(dictionary: dict) -> int:
    """
    Function will return length of the longest value from a dictionary
    :param dictionary:
    { 1: 'abc',
      2: 'abcd',
      3: 'abcde'
    }
    :return: 5
    """
    longest = 0
    for value in dictionary:
        longest = len(str(dictionary[value])) if len(str(dictionary[value])) > longest else longest
    return longest
