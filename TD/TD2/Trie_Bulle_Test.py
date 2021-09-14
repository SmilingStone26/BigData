import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import *

#Recupe de la liste sans doublon
#-------------------------------------------------------------

readFile = [[0,0]]

for i in range(0,10):
    readFile.append([randrange(1,10000),randrange(1,10000)])
    print(readFile[i])

#-------------------------------------------------------------

print()

for i in range(len(readFile)-1,1,-1):
    for j in range(0,i):
        if(readFile[j][0]<readFile[j+1][0]):
            a = readFile[j]
            readFile[j] = readFile[j+1]
            readFile[j+1] = a

for j in range(0,len(readFile)):
    print(readFile[j])
