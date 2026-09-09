def ex1_addition():
    def addition(a, b):
        return a + b

    a = int(input("Entrez un nombre : "))
    b = int(input("Entrez un nombre : "))

    print("La somme est :", addition(a, b))


def ex2_pair():
    def est_pair(n):
        return n % 2 == 0

    nombre = int(input("Entrez un nombre : "))

    print("Est pair :", est_pair(nombre))


def ex3_plus_grand():
    def plus_grand(a, b):
        if a > b:
            return a
        else:
            return b

    a = int(input("Entrez un nombre : "))
    b = int(input("Entrez un nombre : "))

    print("Le plus grand est :", plus_grand(a, b))


def ex4_moyenne():
    def moyenne(liste):
        if len(liste) == 0:
            return 0
        else:
            return sum(liste) / len(liste)

    nombres = []

    for i in range(5):
        nombre = int(input("Entrez un nombre : "))
        nombres.append(nombre)

    print("La moyenne est :", moyenne(nombres))


def main():
    print("=== Day 2 ===")
    print("1) addition ")
    print("2) pair ")
    print("3) plus grand ")
    print("4) moyenne ")
    print("0) Quitter")

    choix = input("Choix : ").strip()

    if choix == "1":
        ex1_addition()
    elif choix == "2":
        ex2_pair()
    elif choix == "3":
        ex3_plus_grand()
    elif choix == "4":
        ex4_moyenne()
    elif choix == "0":
        print("Bye.")
    else:
        print("Choix invalide.")


if __name__ == "__main__":
    main()