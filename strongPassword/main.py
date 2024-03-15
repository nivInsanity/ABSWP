import re

print('Witaj w programie, ktory zweryfikuje czy twoje haslo jest bezpieczne.')

password = input("\nWprowadz haslo skladajace sie z liter, cyfr oraz duzych znakow:\n")

#TODO: funkcja sprawdzajaca znaki w hasle!
#TODO: Po napisaniu funkcji petle zmuszajace uzytkownika wprowadzic poprawne dane!!!

def passChecker(mPassword):

    counter = 0

    if len(mPassword) < 8:
        print('Twoje haslo powinno skladac sie z co najmniej 8 znakow!')

    if re.search(r'\d', mPassword):
        print('Haslo posiada cyfre.')
        counter += 1
    if re.search(r'[A-Z]', mPassword):
        print('Haslo ma duzy znak.')
        counter += 1
    if re.search(r'[a-z]', mPassword):
        print('Haslo ma maly znak.')
        counter += 1

    if counter == 0:
        print('Twoje haslo nie jest bezpieczne!')
    elif counter == 1:
        print('Sila twojego hasla: slabe.')
    elif counter == 2:
        print('Sila twojego hasla: srednie.')
    elif counter == 3:
        print('\nSila twojego hasla: mocne.')

passChecker(password)