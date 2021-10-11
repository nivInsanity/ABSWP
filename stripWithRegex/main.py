import re
import os

def RegexStrip(mainString,charsToBeRemoved):


    if(charsToBeRemoved!=''):
        regex=re.compile(r'[%s]'%charsToBeRemoved)#Interesting TO NOTE
        return regex.sub('',mainString)
    else:
        regex=re.compile(r'^\s+')
        regex1=re.compile(r'$\s+')
        newString=regex1.sub('',mainString)
        newString=regex.sub('',newString)
        return newString

Str = input('Wprowadz ciag znakow, ktory ma zostac zmodyfikowany:')

arg = input('\nWprowadz znak, ktory ma zostac usuniety lub wcisnij enter jezeli ma to byc bialy znak:')

print(RegexStrip(Str,arg))

os.system('pause')