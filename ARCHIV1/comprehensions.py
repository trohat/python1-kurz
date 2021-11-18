#SET = množina

#LIST COMPREHENSION

#GENERATOR EXPRESSION

list1 = []

for x in range(10):
    list1.append(x * x)

print(list1)

list2 = [x * x 
for x in range(10)] 

list3 = [
    x * x
    for x in range(10)
    if x % 2 == 1
]

print(list2)
print(list3)

list3 = [ x * x for x in range(10) if x % 2 == 1 ]

dict1 = {
    x : x * x
    for x in range(10)
    if x % 2 == 1
}

print(dict1)

dict2 = {
    char: char + "ahoj"
    for char in "nosorozec"
}

print(dict2)

#dict comprehension

dict3 = {
    word: word.capitalize()
    for word in "tohle je moje veta".split()
}
print(dict3)

set1 = {
    word
    for word in "tohle je moje kolo a karolíny kocka a moje kolo".split()
    if word.startswith("k")
}

#set comprehension

print(set1)

list3 = [
    x * x if x > 5 else x * x * x
    for x in range(10)
    
]

print(list3)

list comprehension
listX = [
    1. řádek - výraz, který použiji do výsledného listu
    2. řádek - cyklus, přes který iteruji
    3. řádek - podmínka, která vyřadí některé hodnoty (nemusí být)
]

dictX = {
    1. řádek - výraz, který chci jako klíč : výraz který chci jako hodnotu
    2. řádek - cyklus, přes který iteruji
    3. řádek - podmínka, která vyřadí některé hodnoty (nemusí být)
}

setX = {
    1. řádek - výraz, který použiji do setu
    2. řádek - cyklus, přes který iteruji
    3. řádek - podmínka, která vyřadí některé hodnoty (nemusí být)
}

pozn. řádky jsou jen kvůli přehlednosti, lze vše napsat na jeden řádek

generator expression = (
    vnitřek bude stejný jak výše u listu, liší se jen typ závorek
    vhodný pokud potřebuji dále iterovat - hodnoty se vytváří postupně, ne najednou
)


for number in (char.upper() for char in "dlouhééééslovo")