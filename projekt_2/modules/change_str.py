def add_s(number: int, word: str) -> str:
    """
    Add "s" or "es" to param word if param number is higher than 1
    :param number: 2
    :param word: 'bull'
    :return: 'bulls'
    """
    add = ''
    if number != 1:
        if word[-1] == 's':
            add = 'es'
        else:
            add = 's'

    return word + add
