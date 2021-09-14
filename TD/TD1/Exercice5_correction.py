#trier et supprimer les doublons

import csv
from operator import itemgetter

tsvFile = open("C:/Users/ms861784/Downloads/wikirank-fr.tsv/wikirank-fr.tsv", encoding='utf-8')
readFile = csv.reader(tsvFile, delimiter = "\t")
articles = dict()
for row in readFile:
    id = row[0]
    name = row[1]
    quality = row[2]
    pop = row[3]
    author = row[4]
    if id in articles:
        dejavu = articles[id]
        if dejavu == (id,name,quality,pop,author):
            print("Doublon normal : ", id)
            pass
        else:
            print("Double etrange : ", id)
    else:
        articles[id] = (id,name,quality,pop,author)

print('Nombre d\'articles uniques : ', len(articles))
