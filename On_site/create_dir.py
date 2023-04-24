import os

jmena_slozek = ['obrazky', 'texty', 'gify']

for slozka in jmena_slozek:
    if slozka not in dir():
        os.path.join()

    elif slozka in dir():
        print('Složka již existuje!')

print(dir())