import json

default_separator = ' | '
default_max_entries = 20


def save_high_score_question() -> bool:
    """
    Asks user if user wants to save score to high score table.
    Will be asked until user enters y/n
    Transforms answer to bool
    :return: bool
    """
    possible_choice = ['y', 'n']
    while (save := input('\nDo you want to save your score? y/n ')) not in possible_choice:
        print('Sorry, I only take ,,y" or ,,n"')
    return True if save == 'y' else False


def show_high_scores() -> None:
    """
    Loads current high_scores.json, calls functions longest_in_columns to get the longest string in a column
    to use for .center()
    Calls functions print_header and print_body to tell program to print data
    :return: None
    """
    data = load_high_scores()
    header = ('Pos', 'Username', 'Score', 'No. of Guesses', 'Total time')
    longest = longest_in_column(data, header)
    print_header(header, longest)
    print_body(data, longest)


def print_body(data: dict, longest: dict, separator=default_separator, max_entries=default_max_entries) -> None:
    """
    Prints centered high scores based on the longest strings in a column.
    String starts with a separator and each high score is divided by a separator as well
    :param max_entries: 20
    :param data: high_scores.json
    :param longest: {'No. of Guesses': 14, 'Pos': 3, 'Score': 5, 'Total time': 10, 'Username': 8}
    :param separator: ' | '
    :return: None
    """
    # convert and sort score to int since json does not like keys as integers for some reason
    # (cant be properly sorted if it's a string)
    # needs to be later converted back to str since that is what the data: dict is saved as
    score_int = sorted((int(score) for score in data))
    for score in score_int:
        score_str = str(score)
        row = separator
        for same_score in data[score_str]:
            row += str(data[score_str][same_score]['Pos']).center(longest['Pos']) + separator
            row += str(data[score_str][same_score]['Username']).center(longest['Username']) + separator
            row += str(data[score_str][same_score]['Score']).center(longest['Score']) + separator
            row += str(data[score_str][same_score]['No. of Guesses']).center(longest['No. of Guesses']) + separator
            row += str(data[score_str][same_score]['Total time']).center(longest['Total time']) + separator
        print(row)
    print('-'*len(row))


def print_header(header: tuple, longest: dict, separator=default_separator) -> None:
    """
    Prints centered titles based on the longest strings in a column.
    String starts with a separator and each title is divided by a separator as well
    :param header: ('Pos', 'Username', 'Score', 'No. of Guesses', 'Total time')
    :param longest: {'No. of Guesses': 14, 'Pos': 3, 'Score': 5, 'Total time': 10, 'Username': 8}
    :param separator: ' | '
    :return: None
    """
    row = separator
    for title in header:
        row += f'{title}'.center(longest[title])
        row += separator
    print('_'*len(row), row, sep='\n')


def longest_in_column(data: dict, header: tuple, max_entries=default_max_entries) -> dict:
    """
    Takes high_scores.json + pre-written header titles and looks for the longest value in each column
    to find on which number each column should be centered to.
    :param data: high_scores.json
    :param header: ('Pos', 'Username', 'Score', 'No. of Guesses', 'Total time')
    :param max_entries: Controls how many entries will be shown (and thus how many it is worth looking at)
    :return: {'No. of Guesses': 14, 'Pos': 3, 'Score': 5, 'Total time': 10, 'Username': 8}
    """
    # inits columns lengths with length of all the titles
    columns_lengths = {title: len(title) for title in header}

    for score in data:
        for same_score in data[score]:
            for title in columns_lengths:
                title_length = len(str(data[score][same_score][title]))
                title_longest_current = columns_lengths[title]
                columns_lengths[title] = \
                    title_length\
                    if title_length > title_longest_current\
                    else title_longest_current
        if data[score][same_score]['Pos'] > max_entries:
            break

    return columns_lengths


def save_high_score(username: str, no_of_guesses: int, total_time: float, score: str) -> None:
    """
    Saves high score of a user to a variable data
     and then sends it to a function dump_high_score to save it into the high_score.json
    :param username: michal
    :param no_of_guesses: 5
    :param total_time: 30.6
    :param score: 356
    :return: None
    """
    data = load_high_scores()
    same_score = 1 if score not in data else int(max(data[score])) + 1
    data[score] = {same_score: {
        'Username': username,
        'No. of Guesses': no_of_guesses,
        'Total time': total_time,
        'Score': int(score),
        'Pos': None
    }}
    data = update_pos_of_all(data)
    dump_high_scores(data)


def update_pos_of_all(data: dict) -> dict:
    """
    Takes score of all users and updates position
    :param data: high_scores.json
    :return: param data where position of all high scores are updated
    """
    score_int = sorted((int(score) for score in data))
    for score in score_int:
        score_str = str(score)
        for same_score in data[score_str]:
            data[score_str][same_score]['Pos'] = score_int.index(score) + 1

    return data


def load_high_scores() -> dict:
    """
    Loads high_scores with json and returns it as a dict
    :return: high_scores.json dict
    """
    file_name = 'C:\\Python\\Projects\\Git\\engeto\\projekt_2\\data\\high_scores.json'
    with open(file_name) as f:
        data = json.load(f)
    return data


def dump_high_scores(data: dict) -> None:
    """
    Saves data to high_scores.json
    :param data: high_scores.json
    :return: None
    """
    # dump file with jsons
    file_name = 'C:\\Python\\Projects\\Git\\engeto\\projekt_2\\data\\high_scores.json'
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=2, sort_keys=True)


if __name__ == '__main__':
    show_high_scores()
