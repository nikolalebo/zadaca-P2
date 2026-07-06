def pozdrav(ime):
    print("Pozdrav " + ime + "!")

dobrodosao = lambda ime: print("Dobrodošao " + ime + "!")

def ispisi_dobrodoslicu(funkcija, ime):
    funkcija(ime)

ispisi_dobrodoslicu(pozdrav, "Ana")
ispisi_dobrodoslicu(dobrodosao, "Ivan")