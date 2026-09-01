def ex1_majeur_mineur():
    age = int(input("quelle est ton age ?"))
    if age >= 18:
        print("tu es majeur")
    elif age < 18:
        print("tu es mineur")


def ex2_mot_de_passe():
    MotDePasse = "attila"
    verification = input("quelle est le mot de passe ?  ")
    if MotDePasse == verification:
        print("mot de passe corect")
    else :
        print("mot de passe incorect")


def ex3_note(): 
    note = int(input("quelle est votre note ?"))
    if note < 10 and note >= 0 :
        print("mention : Insuffisant")
    elif note < 12 and note >= 10 :
        print("mention : Passable")
    elif note < 14 and note >= 12 :
        print("mention : assez bien")
    elif note < 16 and note >= 14 :
        print("mention : bien")
    elif note <= 20 and note >= 16 : 
        print("mention : très bien")
    else :
        print("Votre note doit être compris entre 0 et 20, veuillez réessayer")


def ex4_nombres():    
    nombre1 = int(input("quelle est le 1er nombre ?"))
    nombre2 = int(input("quelle est le 2eme nombre ?"))
    nombre3 = int(input("quelle est le 3eme nombre ?"))
    if nombre1 > nombre2 and nombre1 > nombre3:
            print(nombre1,"est le plus grand")
    elif nombre2 > nombre1 and nombre2 > nombre3:
            print(nombre2,"est le plus grand") 
    else :
        print(nombre3,"est le plus grand")


def main():
    print("=== Day 2 ===")
    print("1) majeur / mineur")
    print("2) mot de passe ")
    print("3) note ")
    print("4) nombres ")
    print("0) Quitter")

    choix = input("Choix : ").strip()

    if choix == "1":
        ex1_majeur_mineur()
    elif choix == "2":
        ex2_mot_de_passe()
    elif choix == "3":
        ex3_note()
    elif choix == "4":
        ex4_nombres()
    elif choix == "0":
        print("Bye.")
    else:
        print("Choix invalide.")


if __name__ == "__main__":
    main()