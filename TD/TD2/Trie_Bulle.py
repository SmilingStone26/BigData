import csv
import matplotlib as mpl
import matplotlib.pyplot as plt

#Recupe de la liste sans doublon
#-------------------------------------------------------------

tsvFile = open("wikirank-fr.tsv", encoding='utf-8')
readFile = list(csv.reader(tsvFile, delimiter = "\t"))
writeFile = open("exportFile.tsv", 'w', encoding='utf-8')


#-------------------------------------------------------------
"""
for i in range(len(readFile)-2,1,-1):
    for j in range(0,i):
        if(int(readFile[i][0])<int(readFile[i+1][0])):
            readFile[i+1],readFile[i]=readFile[i],readFile[i+1]
            print('readFile : ', readFile[i])
            print('readFile1 : ', readFile[i+1])
"""
print()

#for i in range(len(readFile)-1,1,-1):
for i in range(100,1,-1):
    for j in range(0,i):
        if(int(readFile[j][0])<int(readFile[j+1][0])):
            a = readFile[j]
            readFile[j] = readFile[j+1]
            readFile[j+1] = a
    writer = csv.writer(writeFile, delimiter="\t")
    writer.writerows([readFile[i][0],readFile[i][1],readFile[i][2],readFile[i][3],readFile[i][4]])
    print(readFile[i])
