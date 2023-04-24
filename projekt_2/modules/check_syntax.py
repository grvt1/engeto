"""
This is where all the string checks are located
Checks can be called one by one or using function check_all to check all defined checks
"""
from projekt_2.modules.change_str import add_s


def check_all(check_this: str) -> bool:
    """
    Goes through all the functions in this class and returns True if all of them are True and false if at least one is False
    """
    checks = [
        string_is_int(check_this),
        correct_number_of_chars(check_this),
        first_char_not_0(check_this),
        unique_chars(check_this)
    ]
    return False if False in checks else True


def string_is_int(check_this: str) -> bool:
    """
    Checks whether
     Example 1:
    :param check_this: 4567
    :return: True

    Example 2:
    :param check_this: 4a56
    :return: False
    """
    if not check_this.isnumeric():
        print(" ! Numeric characters only.")
    return check_this.isnumeric()


def correct_number_of_chars(check_this: str, correct=4) -> bool:
    """
    Checks whether len(string) == correct.
    Param correct is optional, defaults to 4
    Example 1:
    :param check_this: 1234
    :param correct: 4
    :return: True

    Example 2:
    :param check_this: 234
    :param correct: 4
    :return: False
    """
    check = True if len(str(check_this)) == correct else False
    if not check:
        print(f' ! {correct} {add_s(correct, "digit")} needs to be entered.')

    return check


def first_char_not_0(check_this: str) -> bool:
    """
    Checks if 1st char in a string is a 0 (zero)
    Example 1:
    :param check_this: 0123
    :return: False

    Example 2:
    :param check_this: 1123
    :return: True
    """
    check = True if check_this[0] != '0' else False
    if not check:
        print(f" ! Can't start with a 0.")

    return check


def unique_chars(check_this: str) -> bool:
    """
    Checks whether any char in a string is not unique
    Example 1:
    :param check_this: 1123
    :return: False

    Example 2:
    :param check_this: 1423
    :return: True
    """
    for i in check_this:
        if check_this.count(i) > 1:
            print(f" ! Unique digits only.")
            return False
    return True
