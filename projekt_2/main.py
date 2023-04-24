"""

main.py: druhý projekt do Engeto Online Python Akademie

author: Michal Trumpich

email: michal.trumpich@gmail.com

discord: Michal T.#8572

"""

# modules
from projekt_2.modules.greetings import greet_user
from projekt_2.modules.game import what_now, new_game


def main():
    greet_user(username := input('Enter username to start: '))

    while True:
        new_game(username)

        chicken_out = what_now()
        if chicken_out:
            break


main()
