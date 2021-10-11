import os, re, shutil

#Path finding scripot
def makeFilesPathTab():

    fileTab = []

    for root, dirs, files in os.walk('C:\\exampleFolder'):
        for file in files:
            if file.startswith('Spam') and file.endswith('.txt'):

                i = os.path.join(root, file)
                fileTab += [i]

    return fileTab

#here we find files called 'Spam + \d\d\d +.txt' and rename all when order is wrong.
def regexFindAndRename():

    nList = makeFilesPathTab()

    regex = re.compile(r'\d\d\d')

    intFinder = re.findall(regex, str(nList))

    listOfInts = []

    for i in range(len(intFinder)):

        oneInt = int(intFinder[i])

        listOfInts += [oneInt]

    print(listOfInts)

    evenInt = []
    oddInt = []

    for i in range(0, len(listOfInts), 2):
        evenInt.append(listOfInts[i])

    for i in range(1, len(listOfInts), 2):
        oddInt.append(listOfInts[i])

    print(evenInt, oddInt)

    min_val = min(len(evenInt), len(oddInt))

    for i in range(min_val):

        if oddInt[i] - evenInt[i] == 1:
            print(oddInt[i] - evenInt[i])
            continue

        elif evenInt[0] != 0 or len(oddInt) == 0:
            print('The order of the files is wrong, I will correct it.')
            print('\nelif instruction')

            for i in range(len(nList)):

                filledNumber = str(i).zfill(3)
                correctFileName = ('C:\\correctOrderFiles\\Spam' + filledNumber + '.txt')
                primaryString = (nList[i])
                shutil.move(primaryString, correctFileName)
            break

        else:
            print('The order of the files is wrong, I will correct it.')
            print('\nelse instruction')

            for i in range(len(nList)):
                filledNumber = str(i).zfill(3)
                correctFileName = ('C:\\correctOrderFiles\\Spam' + filledNumber + '.txt')
                primaryString = (nList[i])
                shutil.move(primaryString, correctFileName)

            break

    print('Order of files is correct.')

#Opposite to previous - when order is correct it mess up order.
def makeGapsBetweenFiles():

    nList = makeFilesPathTab()

    regex = re.compile(r'\d\d\d')

    intFinder = re.findall(regex, str(nList))

    listOfInts = []

    for i in range(len(intFinder)):

        oneInt = int(intFinder[i])

        listOfInts += [oneInt]

    evenInt = []
    oddInt = []

    for i in range(0, len(listOfInts), 2):
        evenInt.append(listOfInts[i])

    for i in range(1, len(listOfInts), 2):
        oddInt.append(listOfInts[i])

    min_val = min(len(evenInt), len(oddInt))

    counter = 0

    for i in range(min_val):
        if oddInt[i] - evenInt[i] == 1:
            print('Order of files is correct, it is time to mess with it.')

            for i in range(len(nList)):

                filledNumber = str(counter).zfill(3)
                correctFileName = ('C:\\messedOrderFiles\\Spam' + filledNumber + '.txt')
                primaryString = (nList[i])
                print(correctFileName)
                shutil.move(primaryString, correctFileName)
                counter += 2
        break

    print('Order of files is messed up again. :)')

