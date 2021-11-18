class Clovek:
    def __init__(self, jmeno, prijmeni, pracoviste, povolani):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.pracoviste = pracoviste
        self.povolani = povolani

    def vstavej(self):
        print("Dobré ráno.")
        print("Dnes jsem se dobře vyspal.")

    def jdi_do_mesta(self, mesto):
        """ mesto je obycejny parametr """
        print(f"Jdu do {mesto}")

    def jdi_do_prace(self, pracoviste):
        """ pracoviste je obycejny parametr neboli nezávislá proměnná 
        tj. nepotřebuji tečku """
        print(f"Jdu do {pracoviste}")

    def jdi_do_prace2(self, lokace):
        """ pracoviste je vlastnost patřící instanci, proto jdu 
        pomocí tečkové notace
        tj. např. pracoviste je vlastnost patřící Karlovi 
        přístup přes tečku = přístup do objektu, resp. do instance
        """
        print(f"Jdu do {self.pracoviste} v {lokace}")

    
karel = Clovek("Karel", "Novák", "IBM", "programátor")

print(dir(karel))
"""
karel.pracoviste = "Etnetera"
karel.jmeno = "Václav"

karel.vstavej()
karel.jdi_do_prace("Avast")
karel.jdi_do_prace2()
karel.jdi_do_mesta("Dillí")

aneta = Clovek("Aneta", "Černá", "Seznam.cz", "manažerka")

aneta.jdi_do_prace2()
"""