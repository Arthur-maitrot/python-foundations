def ex1_liste():
    nombres = []

    for i in range(5):
        nombre = int(input("Entrez un nombre : "))
        nombres.append(nombre)

    print(nombres)


def ex2_moyenne():
    nombres = []

    for i in range(5):
        nombre = int(input("Entrez un nombre : "))
        nombres.append(nombre)

    somme = 0

    for nombre in nombres:
        somme = somme + nombre

    moyenne = somme / len(nombres)

    print("La moyenne est :", moyenne)


def ex3_max(): 
    nombres = []

    for i in range(5):
        nombre = int(input("Entrez un nombre : "))
        nombres.append(nombre)
    plus_grand = nombres[0]
    for nombre in nombres:
        if nombre > plus_grand :
            plus_grand = nombre
    print("le nombre le plus grand est : ",plus_grand)



def ex4_pairs():    
    nombres = []
    compteur = 0
    
    for i in range(5):
        nombre = int(input("Entrez un nombre : "))
        nombres.append(nombre)
        

    for nombre in nombres:
        if nombre % 2 == 0:
            compteur = compteur + 1
    print("il y a : ",compteur, "nombres pairs")
   

def main():
    print("=== Day 2 ===")
    print("1) liste ")
    print("2) moyenne ")
    print("3) max ")
    print("4) pairs ")
    print("0) Quitter")

    choix = input("Choix : ").strip()

    if choix == "1":
        ex1_liste()
    elif choix == "2":
        ex2_moyenne()
    elif choix == "3":
        ex3_max()
    elif choix == "4":
        ex4_pairs()
    elif choix == "0":
        print("Bye.")
    else:
        print("Choix invalide.")


if __name__ == "__main__":
    main()