# read animals.txt
# and write animals_new.txt
with open("animals.txt", "r") as f:
    lista = f.readlines()
with open("animals_new.txt", "w") as f:
    for line in lista:
        f.write(line.strip() + " ")
