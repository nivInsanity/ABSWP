import re

my_little_string = 'AZ'

if re.match('''
    [(?=.*[A-Z]]

''', my_little_string):
    print('Twoje hasło jest bezpieczne')
else:
    print('Twoje hasło nie jest bezpieczne.')