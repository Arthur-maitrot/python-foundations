taches = []
def ajouter_tache(taches):
    nouvelle_tache = input("ajouter votre tache :")
    taches.append(nouvelle_tache)
def afficher_taches(taches):
    for tache in taches:
        print(tache)

print("choix 1 : ajouter une tache ")
print("choix 2 : afficher une / les tache(s) ")
print("choix 3 : quitter")

choix = int(input("Choix : "))

while choix != 3:
    if choix == 1: 
        ajouter_tache(taches)
    elif choix == 2:
        afficher_taches(taches)
    print("choix 1 : ajouter une tache ")
    print("choix 2 : afficher une / les tache(s) ")
    print("choix 3 : quitter")
    choix = int(input("Choix : "))

    