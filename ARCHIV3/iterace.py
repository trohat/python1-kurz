def moje_iterable():
    print("já jsem generátor")
    yield 5
    print("po prvním returnu/yieldu")
    yield 6
    print("po druhém yieldu")
    yield 7
    print("funkce končí")


for x in moje_iterable():
    print("teď jsem ve for cyklu - začátek")
    print(f"z iterace se vrátilo {x}")
    print("teď jsem ve for cyklu - konec")

class MujIterator():
    """
    iteruje přes řetězec pozpátku
    """
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        self.index = len(self.string)
        return self

    def __next__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.string[self.index]

for x in MujIterator("jablko"):
    print(x)

class NekonecnyCyklus():
    def __iter__(self):
        self.pocitadlo = 10
        return self

    def __next__(self):
        self.pocitadlo -= 1
        if self.pocitadlo == 0:
            raise StopIteration
        return 5

for x in NekonecnyCyklus():
    print(x)

def retezec_pozadu(retezec):
    index = len(retezec)
    while index > 0:
        index -= 1
        yield retezec[index]

for x in retezec_pozadu("hruška"):
    print(x)

for x in enumerate("chameleon"):
    print(x)