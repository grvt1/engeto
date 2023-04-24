def show_selection(*args) -> None:
    """
    Funkce spoji zadane argumenty pomoci metody .join
    Argumenty se oddeli pomoci separatoru

    Priklad:
    args = ("a", "b", "c")
    vysledek:
    ---------
    a | b | c
    ---------
    """

    arguments = ' | '.join(*args)
    separator = '-'*len(arguments)
    print(separator, arguments, separator, sep='\n')

def summerize() -> None:
    """
    Pta se uzivatele na cisla, ktere chce secist
    Ukonci se po zadani quit, kde funkce pote vytiskne vysledek secteni vsech cisel

    Priklad:
    1 + 2 + 3 = 6
    """

    summerized = 0
    while True:
        vstup = input('Cislo: ')
        if vstup == 'quit':
            break
        else:
            summerized += int(vstup)
    print(f'Vysledek: {summerized}')


def minus() -> None:
    """
    Pta se uzivatele na cisla, ktere chce od sebe odecist
    Ukonci se po zadani '=', kde funkce pote vytiskne vysledek odecteni vsech cisel

    Priklad:
    1 - 2 - 3 = 6
    """
    summerized = 0
    while (vstup := input('Cislo: ')) != '=':
        summerized -= int(vstup)
    print(f'Vysledek: {summerized}')


def pow() -> None:
    """
    Funkce se zepta uzivatele na mocnence a mocnitele

    Priklad:
    2 ** 2 -> 4
    """

    base = int(input('Base: '))
    exponent = int(input('Exponent: '))
    result = base ** exponent
    print(result)

def count_avg() -> None:
    """
    Funkce se pta uzivatele na zadani cisel
    Po zadani quit se vseschna cisla sectou a vydeli poctem cisel (udela se prumer)

    Priklad:

    """

    cisla = []
    while (hodnota := input('Cislo: ')) != '=':
        cisla.append(int(hodnota))

    vysledek = sum(cisla) / len(cisla)
    print(vysledek)


def calculator():
    '''
    Main function
    '''
    selection = ('+', '-', '*', '/', 'pow', 'avg', 'quit')

    while True:
        show_selection(selection)
        vstup = input()
        if vstup == 'quit':
            break
        elif vstup == 'pow':
            pow()
        elif vstup == '+':
            summerize()
        elif vstup == '-':
            minus()
        elif vstup == 'avg':
            count_avg()

calculator()
