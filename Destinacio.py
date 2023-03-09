import datetime

mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
domeny = ("gmail.com", "seznam.cz", "email.cz")
slevy = ("Olomouc", "Svitavy", "Ostrava")
ceny = (150, 200, 120, 120, 100, 180)
dvojita_cara = "=" * 35
cara = "-" * 35

AKT_ROK = str(datetime.date.today()).split('-')[0]

# Privitani
print('VITEJTE U NASI APLIKACE DESTINATIO!')
print(dvojita_cara)

# vytiskni na obrazovku zarovnana mesta
nejdelsi_nazev = len(max(mesta, key=len))
for i in mesta:
    pocet_mezer_za_mestem =  ' '*(nejdelsi_nazev - len(i))
    print(f'{mesta.index(i) + 1} - {i}{pocet_mezer_za_mestem} | {ceny[mesta.index(i)]}')

print(dvojita_cara)

# Vyber destinace + kontrola jestli je vyber spravny (quit pokud neni)
destinace = input('VYBER CISLO DESTINACE: ')
if destinace.isalpha() or int(destinace) > 6 or int(destinace) < 1:
    print(f'VYBER: {destinace} NEEXISTUJE! UKONCUJI..')
    print(cara)
    quit()
else:
    vyber = mesta[int(destinace) - 1]
    print(f'DESTINACE: {vyber}')
    print(cara)

    # Kontrola, jestli ma zakaznik narok na slevu 25%
    finalni_cena = ceny[int(destinace) - 1]
    if vyber in slevy:
        finalni_cena *= 0.75
        print(f'ZISKAVATE 25% SLEVU! CENA: {finalni_cena},-')
        print(cara)

    # Kontrola, zda jmeno obsahuje mezeru a jestli tam nejsou spec. znaky / cislice
    cele_jmeno = input('Zadej celé jméno: ')
    cele_jmeno_bez_mezer = cele_jmeno.replace(' ', '')
    if ' ' not in cele_jmeno or not cele_jmeno_bez_mezer.isalpha():
        print('Jmeno nebo prijmeni nejsou v poradku! Ukoncuji..')
        quit()
    else:
        jmeno, prijmeni = cele_jmeno.split()[0], cele_jmeno.split()[1]
        print(f'Jmeno: {jmeno}')
        print(f'Prijmeni: {prijmeni}')
        print(cara)

        # Kontrola, zda email obsahuje @ a zda zadana domena je v seznamu pov. domen
        email = input('EMAIL: ')
        if '@' not in email or email.split('@')[1] not in domeny:
            print('Neplatna emailova adresa. Ukoncuji..')
            quit()
        else:
            print('Email je v poradku')
            print(dvojita_cara)

            # Pokud vse probehne v poradku, tak zrekapituluje objednavku a posle listek na email
            print(f'DEKUJI, {jmeno}, ZA OBJEDNAVKU.')
            print(f'CIL. DESTINACE: {vyber}, CENA JIZDNEHO: {finalni_cena},-')
            print(f'NA TVUJ MAIL: {email}, JSME TI POSLALI LISTEK')