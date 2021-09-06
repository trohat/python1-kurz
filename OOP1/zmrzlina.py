class KopecekZmrzliny:
    def __init__(self, flavour, price):
        self.flavour = flavour
        self.price = price

    def __str__(self):
        return f"I am an icecream with {self.flavour} flavour."

kop1 = KopecekZmrzliny("chocolate", 10)
kop2 = KopecekZmrzliny("vanilla", 2)
kop3 = KopecekZmrzliny("strawberry", 3)

class ZmrzlinovyPohar:
    """
    Umí přidávat kopečky metodou pridej_kopecek s jedním parametrem.
    """
    def __init__(self):
        self.kopecky = []

    def pridej_kopecek(self, kopecek):
        self.kopecky.append(kopecek)

    def celkova_cena(self):
        total = 0
        for kopecek in self.kopecky:
            total += kopecek.price
        return total

    def __str__(self):
        result = "Já jsem zmrzlinový pohár a tohle jsou moje zmzliny:\n"
        result += ", ".join(kopecek.flavour for kopecek in self.kopecky).capitalize()
        result += f".\nZaplaťte {self.celkova_cena()} Kč. Dobrou chuť."
        return result

pohar = ZmrzlinovyPohar()

pohar.pridej_kopecek(kop1)
pohar.pridej_kopecek(kop2)
pohar.pridej_kopecek(kop3)

#pohar.kopecky.append(kop3)  # tohle by fungovalo ale tak to dělat nechceme

#print(ZmrzlinovyPohar.__doc__) # takhle obvykle ne

print(pohar)

print(kop1.flavour)
print (pohar.celkova_cena())