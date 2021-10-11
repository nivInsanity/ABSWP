import re
import glob

#Szukanie wszystkich plikow tekstowych
def fileFind():

    myFiles = glob.glob('*.txt')

    return myFiles

#otwiera plik i pokazuje zdania, w ktorych wystepuje slowo wprowadzone przez uzytkownika
def openAndSearch():

    fileList = fileFind()

    fileOpen = open(fileList[0])

    regString = input('\nPodaj slowo, ktore ma byc zawarte w danej linijce/kach tekstu:\n')


    for i in fileOpen.readlines():
        line = re.findall(regString, i)
        if line:
            print(i)

    fileOpen.close()

openAndSearch()