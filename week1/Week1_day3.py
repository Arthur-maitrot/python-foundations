def ex1_1_a_20():
    for i in range(1, 21):
        print(i)


def ex2_1_a_n():
    N = int(input("Jusqu'à quel nombre ? "))

    somme = 0

    for i in range(1, N + 1):
        somme = somme + i

    print("La somme est :", somme)


def ex3_pairs(): 
    somme = 2
    while somme < 31:
        print(somme)
        somme = somme + 2


def ex4_nombre_mystere():    
nombreC = 256
nombreJ = int(input("choisissez votre premier nombre : "))
while nombreC != nombreJ:
    if nombreJ < nombreC :
        print("votre nombre est inférieur !")
    elif nombreJ > nombreC :
        print("votre nombre est supérieur !")
    nombreJ = int(input("choisissez votre nombre :"))
print("vous avez trouver le nombre était bien",nombreC)


def main():
    print("=== Day 2 ===")
    print("1) 1 a 20")
    print("2) 1 a n ")
    print("3) pairs ")
    print("4) nombre mystère ")
    print("0) Quitter")

    choix = input("Choix : ").strip()

    if choix == "1":
        ex1_1_a_20()
    elif choix == "2":
        ex2_1_a_n()
    elif choix == "3":
        ex3_pairs()
    elif choix == "4":
        ex4_nombre_mystere()
    elif choix == "0":
        print("Bye.")
    else:
        print("Choix invalide.")


if __name__ == "__main__":
    main()