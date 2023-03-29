# DONE promenne
sklad = {
    'mleko':    [30,  5],    # index 0 -> cena; index 1 -> mnozstvi
    'maso':     [100, 1],
    'banan':    [30, 10],
    'jogurt':   [10,  5],
    'chleb':    [20,  5],
    'jablko':   [10, 10],
    'pomeranc': [15, 10], 
}

nabidka = """
+-----------+----------+
| POTRAVINA |   CENA   |
+-----------+----------+
| mleko     |    30,-  |
| maso      |   100,-  |
| banan     |    30,-  |
| jogurt    |    10,-  |
| chleb     |    20,-  |
| jablko    |    10,-  |
| pomeranc  |    15,-  |
+-----------+----------+
"""

oddelovac = '=' * 40

# --------------------------------------------

# DONE kosik = dict()
cart = {}

# DONE Pozdrav a vypsani nabidky
print('Vitejte v nasem online nakupnim kosiku',
      oddelovac,
      nabidka,
      oddelovac,
      'Pro ukonceni nakupu zadej ,,quit"',
      sep='\n'
      )

# DONE cely cyklus
while (item := input('Vyber polozku: ')) != 'quit'.lower() and item != 'konec'.lower():

    # DONE pokud zbozi nebude v nabidce
    if item not in sklad:
        print('Zbozi neni v nabidce')

    # DONE Pokud vybrane neni v nakupnim kosiku
    elif item not in cart and sklad[item][1] > 0:
        cart[item] = [sklad[item], 1]
        sklad[item][1] -= 1

    # DONE pokud zbozi je v kosiku
    elif item in cart and sklad[item][1] > 0:
        cart[item][1] += 1
        sklad[item][1] -= 1

    # DONE pokud zbozi jiz neni skladem
    elif sklad[item][1] == 0:
        print('Zbozi jiz neni skladem')

# DONE vypis kosiku
print(cart)
