ime = "Akadiusz"
wiek = 29
plec = "mężczyzna"

imie2 = "Wioletta"
wiek2 = 23
plec2 = "kobieta"

osoba1 = ('Arkadiusz', 29, 'mężczyzna')
osoba2 = ('Wioletta', 23, 'kobieta')
osoba3 = ('Kuba', 33, 'mężczyzna')

listaGosci = {
    ('Arkadiusz', 29, 'mężczyzna'),
    ('Wioletta', 22, 'kobieta'),
    ('Kuba', 32, 'mężczyzna')
            }
listaGosci2 = {
    ('Arkadiusz', 28, 'mężczyzna'),
    ('W', 32, 'kobieta'),
    ('K', 22, 'mężczyzna')
            }
listaGosci3 = listaGosci & listaGosci2

for imie, wiek, plec in listaGosci:
    print( "Imię: " , imie, "\nwiek: ", wiek), plec
