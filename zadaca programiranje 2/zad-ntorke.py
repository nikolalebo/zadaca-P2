import csv

studenti = []

datoteka = open('rezultati.csv', encoding='utf-8')
reader = csv.reader(datoteka)

for red in reader:
    ime, prezime, bodovi = red
    studenti.append((prezime, ime, int(bodovi)))

datoteka.close()

studenti.sort()

ocjene = {"Nedovoljan": 0, "Dovoljan": 0, "Dobar": 0, "Vrlodobar": 0, "Izvrstan": 0}

for prezime, ime, bodovi in studenti:
    if bodovi <= 49:
        ocjene["Nedovoljan"] += 1
    elif bodovi <= 65:
        ocjene["Dovoljan"] += 1
    elif bodovi <= 80:
        ocjene["Dobar"] += 1
    elif bodovi <= 90:
        ocjene["Vrlodobar"] += 1
    else:
        ocjene["Izvrstan"] += 1

print("Sortirani studenti:", studenti)
print("\nBroj ocjena:", ocjene)