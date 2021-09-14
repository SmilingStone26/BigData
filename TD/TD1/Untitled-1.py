
uneliste = [
    (34, "Article 1", 50), 
    (3, "Ar 2", 4), 
    (1, "Ar ", 100),
    (1, "Ar ", 0)
]

def  extract (el) :
    return el[2]

l = sorted (uneliste, key = extract)


l = sorted (uneliste, key = lambda el : el[2])

f = lambda el : el[2]

print ( f ( (1,2,11) ) )
for el in uneliste:
    print (el)


print ("Sorted")

for el in l:
    print (el)