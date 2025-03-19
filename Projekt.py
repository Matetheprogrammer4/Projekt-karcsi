import random

def szam_kitalalo():
    print("Udvozollek a jatekban!")
    print("Gondoltam egy szamra 1 es 1000000 kozott.")

    random_szam = random.randint(1, 1000000)
    probalkozasok = 0

    while True:
        try:
            tipp = int(input("Tippelj egy szamot: "))
            probalkozasok += 1

            if tipp < random_szam:
                print("A tipped tul alacsony, probald ujra!")
            elif tipp > random_szam:
                print("A tipped tul magas, probald ujra!")
            else:
                print("Eltalaltad, gratulalok!")
                print(f"Ennyi probalkozasod volt: {probalkozasok}")
                break
        except ValueError:
            print("Ide csak szamokat irhatsz!")

def jatek_ujra():
    while True:
        valasz = input("Akarsz ujra jatszani? (igen/nem): ")
        if valasz == "igen":
            szam_kitalalo()
        elif valasz == "nem":
            print("Koszonjuk a jatekot! Szia!")
            break
        else:
            print("Kerlek igen-t vagy nem-et irj!")

szam_kitalalo()
jatek_ujra()