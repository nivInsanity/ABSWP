import shelve

list

randomShelve = shelve.open('randShelve')


randomShelve[0] = str('Pierwsza wartosc')
randomShelve[1] = str('Druga wartosc')
randomShelve[2] = str('Trzecia wartosc')

randomShelve.close()