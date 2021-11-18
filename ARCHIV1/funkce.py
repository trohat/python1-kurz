#DRY = dont repeat yourself
"""
def pozdrav(jmeno=""):
    if jmeno != "":
        print(f"ahoj {jmeno}")
    print("odlož si oblečení do šatníku")
    print("v obývacím pokoji je občerstvení")

print("já jsem uvítací robot")

pozdrav([1, 2])
pozdrav("Radku")
pozdrav("Jano")
pozdrav("Pavlo")
pozdrav()
"""

def scitej(prvni_parameter, druhy_parametr, *args, **kwargs):
    print(f"N-tice jménem args vypadá takhle: {args}")
    print(f"Slovník (tj. dict) jménem kwargs vypadá takhle: {kwargs}")

scitej(1, [2, 5, 9], 10, 11, oddelovac=5, znak_na_konci_radku=6)