import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import random

#Zadanie 1

lList = []

#Zadanie 2

lList = list(range(100, 201))

#Zadanie 3

zList = []

for i in range (int(len(lList))):

    newVar = lList[i] + 8
    lList[i] = newVar
    zList.append(newVar)

#Zadanie 4

order = list(reversed((range(0, 101))))
lList = [lList[i] for i in order]
print(lList)

#Zadanie 5

gList = []

for i in range(100):
    randomIntegers = random.randint(0, 1)
    gList.append(randomIntegers)

#Zadanie 6

for i in range(len(gList)):
    boolValue = bool(gList[i])
    gList[i] = boolValue

#Zadanie 7

twentyFiveList = []
seventyFiveList = []

for i in range(25):
    twentyFiveList.append(gList[i])

for i in range(25, 100):
    seventyFiveList.append(gList[i])

#Zadanie 8

smallerList = []
biggerList = []

while len(smallerList) < 25:
    a = np.random.choice(lList)
    if a not in smallerList:
        smallerList.append(a)

while len(biggerList) < 75:
    b = np.random.choice(lList)
    if b not in biggerList and b not in smallerList:
        biggerList.append(b)

#Zadanie 9

for i in range(10):
    smallerList = []
    biggerList = []

    while len(smallerList) < 25:
        a = np.random.choice(lList)
        if a not in smallerList:
            smallerList.append(a)

    while len(biggerList) < 75:
        b = np.random.choice(lList)
        if b not in biggerList and b not in smallerList:
            biggerList.append(b)

    averageValue = sum(smallerList) / len(smallerList)
    secondAverageValue = sum(biggerList) / len(biggerList)
    attempt = i

    print('Attempt', i, ':')
    print('Average from smaller = ', averageValue, '\nAverage from bigger = ', secondAverageValue)

#Zadanie 10

for i in range(len(gList)):
    print(zList[i], gList[i])

