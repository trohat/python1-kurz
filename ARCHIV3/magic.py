class Cislo():
    def __init__(self, cislo):
        self.cislo = cislo

    def __add__(self, other):
        print("sčítám")
        return self.cislo + other.cislo

    def __mul__(nalevo, napravo):
        print("Měl bych násobit, ale nechci")
        return f"{nalevo.cislo} * {napravo.cislo} a nevím kolik to je"

c1 = Cislo(5)
c2 = Cislo(6)

print(c1 + c2)
print(c1 * c2)
print(c1 / c2)