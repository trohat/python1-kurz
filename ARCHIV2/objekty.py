class Clovek:
    def __init__(self, jmeno_z_parametru, 
                    prijmeni_z_parametru, vek=20):
        self.jmeno = jmeno_z_parametru
        self.prijmeni = prijmeni_z_parametru
        self.vek = vek
        self.kde_pracuje = "IBM"
        if self.vek >= 18:
            self.plnolety = True
        else:
            self.plnolety = False

    def __str__(self):
        return f"Jmenuji se {self.jmeno} {self.prijmeni}"\
            f" a je mi {self.vek} let."

karel = Clovek("Karel", "Novák", 29)

aneta = Clovek("Aneta", "Fialová", 15)
aneta2 = Clovek("Aneta", "Modrá")
aneta3 = Clovek(prijmeni_z_parametru="Červená",
                    vek=2, jmeno_z_parametru="Pavla")

print(karel)
print(aneta)
print(aneta2)
print(aneta3)

