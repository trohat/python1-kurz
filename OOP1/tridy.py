class Clovek():
    pocet = 0

    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        print(self.__class__)
        print(Programator.pocet, Clovek.pocet)
        print(Programator.pocet is Clovek.pocet)
        self.__class__.pocet += 1
        print(self.__class__)
        print(Programator.pocet, Clovek.pocet)
        print(Programator.pocet is Clovek.pocet)

    def __repr__(self):
        return f"Jsem {self.jmeno} {self.prijmeni} a "\
            f"uz existuje {self.__class__.pocet} lidí."

    def vstavej(self):
        print("Dobré ráno")

    def pozdrav(self):
        print("Dobrý den")

    def jdi_do_prace(self):
        print("Vyrážím do práce, za chvíli tam budu.")
        self.pozdrav()

class Programator(Clovek):
    def __init__(self, jmeno, prijmeni, jazyk):
        super().__init__(jmeno, prijmeni)
        self.jazyk = jazyk

    def pozdrav(self):
        print("Ahoj")

    def programuj(self):
        print("Programuji si bez oblíbeného programovacího jazyka.")
        super().pozdrav()

    def __repr__(self):
        return "Jsem programátor\n" + super().__repr__()

karel = Programator("Karel", "Novák", "Python")
aneta = Clovek("Aneta", "Bílá")
aneta2 = Clovek("Aneta", "Bílá")
aneta3 = Clovek("Aneta", "Bílá")
aneta4 = Clovek("Aneta", "Bílá")
aneta5 = Clovek("Aneta", "Bílá")
karel2 = Programator("Karel", "Novák", "Python")
print(aneta)
print(karel)


