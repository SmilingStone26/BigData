import csv

totalRow = 0
with open("C:/Users/ms861784/Downloads/wikirank-fr.tsv/wikirank-fr.tsv", encoding='utf-8') as file:
    rd = csv.reader(file,delimiter='\t')
    for row in rd:
        totalRow += 1
    print(totalRow)
