from pathlib import Path
import pyperclip, shutil, os

# def findAndCopy():
    # #nie mam pojecia po co robilem ten kod ;-; (myslalem, ze zadanie jest inne...)
    # pathList = []
    # for path in Path('E:\\').rglob('*.jpg'):
    #     shutil.copy(path.name, 'C:\\destination')
    #
    # x = '\n'.join(str(x) for x in pathList)
    #
    # pyperclip.copy(x)
    # return pathList

    # for filename in os.listdir():
    #     if filename.endswith('.jpg'):
    #         print(filename)
    #         #shutil.copy(filename, 'C:\\Destination')


for filename in os.listdir():
        if filename.endswith('.jpg'):
            shutil.copy(filename, 'C:\\Destination')