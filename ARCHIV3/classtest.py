class Clovek():
    def __init__(self, jm):
        self.jmeno = jm + "aabbbb"

    def kric(self):
        print("kricim 1")

class C2(Clovek):
    def __init__(self, j):
        self.jmeno = j + "cccccc"

    

class C3(C2):
    def __init__(self, j):
        super().__init__(j)

    def kric(self):
        print("kricim 3")

    def piskni(self):
        super().kric()

c = C3("a")
c.piskni()

