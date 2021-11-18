# EXCEPTIONS

print("cože??")
while True:
    try:
        cislo1 = int(input("Zadej číslo:"))
        cislo2 = int(input("Zadej číslo:"))
       
        vysledek = cislo1 / cislo2
        print("vypočítáno, končíme")
        break
    except ValueError as e1:
        print("ValueError")
        print(e1)
    except ZeroDivisionError as e2:
        print("ZeroDivision")
        print(repr(e2))
    except:
        print("Nějaká nečekaná výjimka")

print("program v pohodě pokračuje")


#LBYL = look before you leap
#EAFP = easier to ask forgiveness than permission  

class TooManyEmployersException(Exception):
    pass


employers = 500

"""

def delej_neco_jineho():
    if employers > 400:
        raise TooManyEmployersException

def delej_neco():
    delej_neco_jineho()

try:
    delej_neco()
except TooManyEmployersException:
    print("too many")


class PrilisMnohoKopeckuVyjimka(Exception):
    def __init__(self):
        print("běží __init__xx")

    def __str__(self):
        return "__str__"




if 4 > 5:
        raise PrilisMnohoKopeckuVyjimka()



"""
