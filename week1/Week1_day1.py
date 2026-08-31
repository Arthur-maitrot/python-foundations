def ex1_age_dans_5_ans():
    prenom = input("Quel est votre prénom ? ")
    age = int(input("Quel est votre âge ? "))
    print(f"Bonjour {prenom}, vous aurez {age + 5} ans dans 5 ans.")



def ex2_calculatrice():
    a = float(input("Nombre 1 : "))
    b = float(input("Nombre 2 : "))
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")



def ex3_temps(): 
    depart = int(input("Quel est votre nombre de départ ? "))
    if depart < 60:
        print(f"votre temps es de {depart} secondes")
    elif depart > 60:
        minutes = depart // 60
        secondes = depart % 60
        print(f"votre temps est de {minutes} minutes et {secondes} secondes")   
    elif depart == 60: 
        print(f"votre temps est de 1 minute et 0 secondes")


def ex4_prix():    
    prix = float(input("Prix : "))
    reduction = int(input("Réduction : "))  
    redfinale = prix * reduction
    prixred = redfinale / 100
    print(f"votre prix finale est de : {prix - prixred }")



def main():
    print("=== Day 1 ===")
    print("1) Âge dans 5 ans")
    print("2) Calculatrice")
    print("3) Temps")
    print("0) Quitter")

    choix = input("Choix : ").strip()

    if choix == "1":
        ex1_age_dans_5_ans()
    elif choix == "2":
        ex2_calculatrice()
    elif choix == "3":
        ex3_temps()
    elif choix == "4":
        ex4_prix()
    elif choix == "0":
        print("Bye.")
    else:
        print("Choix invalide.")


if __name__ == "__main__":
    main()