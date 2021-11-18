import os
import glob

print("Aktuální pracovní adresář je", os.getcwd())
#os.chdir("C")
#os.chdir("..")




with open("slova.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line, end="")
    print("poslední příkaz uvnitř with")
    # tady se zavře soubor

# with = context management, zavře soubor za nás
# jinak soubor musíme zavřít ručně

seznam = [55, 66, 78, 95, 56, 23]

with open("cisla.txt", "w") as f2:
    for cislo in seznam:
        f2.write(str(cislo))

with open("slova.txt", "a") as f2:
    for cislo in seznam:
        f2.write( "\n" + str(cislo)) 

with open("slova.txt") as f1, open("nova_slova.txt", "w") as f2:
    for line in f1:
        f2.write(line)

a = open("slova.txt")
for line in a:
    print("slon")
    print(line)