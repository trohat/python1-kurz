"""
Můj naprosto skvělý modul pro křičení a sčítání dvou čísel
"""

print("Modul se právě načítá")
print("__name__ je " + __name__)


konstanta = 42

def vykrik():
    print("Hurááááá")

def scitani(a,b):
    return a + b

if __name__ == "__main__":
    print("modul běží jako hlavní program")
    print(scitani(5,6))
    vykrik()