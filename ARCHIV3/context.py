class ContextManagement():
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def __enter__(self):
        print("spouštím context manager")
        return self

    def __exit__(self, exc_type, exc_val, exc_traceback):
        print("zavírám soubor")

with ContextManagement("Adam") as clovek:    
    print ("hehe, funguje to")
    print(clovek.jmeno)
    raise OSError("za souboru nejde číst")
