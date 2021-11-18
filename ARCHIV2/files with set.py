files = []

while True:
    new_file = input("Zadej jméno souboru: ")
    if new_file == "quit":
        break
    files.append(new_file)

print(files)

content = []

for file in files:
    with open(file) as f:
        content.append("".join(f.readlines()))

unique_letters = set(content[0])

for i in range(1, len(content)):
    unique_letters &= set(content[i])

print(unique_letters)