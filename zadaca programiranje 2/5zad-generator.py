def parni(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
def neparni(n):
    for i in range(n):
        if i % 2 != 0:
            yield i
broj = int(input("Unesi broj: "))
print("Parni brojevi:")
for x in parni(broj):
    print(x)
print("Neparni brojevi:")
for x in neparni(broj):
    print(x)