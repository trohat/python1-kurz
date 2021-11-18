import random

def jeden_ukon():
    """
    tohle je funkce s časovou složitostí 1
    """
    3 + 4

def pet_ukonu():
    """
    tohle je funkce s časovou složitostí 5
    """
    3 + 4
    5 + 7
    5 - 2
    2 * 8
    8 / 2

seznam = [1, 3, 4]

for number in range(random.randint(1, 1000)):
    seznam.append(number)

#print(f"Délka seznamu je {len(seznam)}")
# mám seznam, u něhož nevím jak je dlouhý
# pojďme se dohodnout, že jeho délku budeme označovat N

jeden_ukon()
# časová složitost 1 = konstanta

pet_ukonu()
# časová složitost 5 = konstanta

for number in seznam:
    jeden_ukon()
# časová složitost n

for number in seznam:
    pet_ukonu()
# časová složitost 5 * n => n

for number in seznam:
    for number2 in seznam:
        print(number, number2)
        jeden_ukon()
# časová složitost n ** 2

for number in seznam:
    for number2 in seznam:
        jeden_ukon()
for number in seznam:
    pet_ukonu()
jeden_ukon()
# n ** 2 + 5000 * n + 1 => n ** 2

for number in seznam:
    pet_ukonu()
jeden_ukon()
# časová složitost 5 * n + 1 => n

for number in seznam:
    jeden_ukon()
pet_ukonu()
# n + 5 => n

for number in seznam:
    jeden_ukon()
for n in range(1000):
    pet_ukonu()
# n + 10 * 5 = n + 5000 => n

# notace velkého O neboli Big Oh notation:
# O(1) = konstantní časová složitost
# O(log n) = logaritmická
# O(n) = lineární
# O(n ** 2) = kvadratická
# O(n ** 3) = mocninná
# O(n ** 4) = mocninná
# O(2 ** n) = exponenciální

#O( n ** 2) == O( 3 * n ** 2 + 5)