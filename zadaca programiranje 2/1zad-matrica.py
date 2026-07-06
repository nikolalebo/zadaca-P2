import random

matrica = []
for i in range(7):
    red = []
    for j in range(7):
        broj = random.randint(1, 9)
        red.append(broj)
    matrica.append(red)

print("matrica:")
for red in matrica:
    print(red)

zbroj = 0

for j in range(7):
    zbroj += matrica[0][j]

for j in range(7):
    zbroj += matrica[6][j]

for i in range(1, 6):
    zbroj += matrica[i][0]

for i in range(1, 6):
    zbroj += matrica[i][6]

print("zbroj je :", zbroj)
