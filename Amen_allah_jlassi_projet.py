def saisir_entier(message):
    while True:
        try:
            nombre = int(input(message))
            return nombre
        except ValueError:
            print("Erreur : veuillez saisir un nombre entier.")
def saisir_texte(message):
    texte = input(message).strip()
    while texte == "":
        print("Erreur : ce champ ne peut pas etre vide.")
        texte = input(message).strip()
    return texte
def saisir_priorite():
    p = saisir_entier("Priorite (1=basse, 2=moyenne, 3=haute) : ")
    while p < 1 or p > 3:
        print("Erreur : choisissez 1, 2 ou 3.")
        p = saisir_entier("Priorite (1=basse, 2=moyenne, 3=haute) : ")
    return p
def afficher_tache(numero, tache):
    print(numero, "-", tache[0], "| priorite :", tache[2])
    print("     ", tache[1])
def ajouter_tache(taches):
    titre = saisir_texte("Titre : ")
    description = saisir_texte("Description : ")
    priorite = saisir_priorite()
    taches.append([titre, description, priorite])
    print("Tache ajoutee.")
def afficher_taches(taches):
    if len(taches) == 0:
        print("Aucune tache.")
    else:
        for i in range(len(taches)):
            afficher_tache(i + 1, taches[i])
def rechercher_tache(taches):
    mot = saisir_texte("Mot-cle a chercher : ").lower()
    trouve = False
    for i in range(len(taches)):
        titre = taches[i][0].lower()
        description = taches[i][1].lower()
        if mot in titre or mot in description:
            afficher_tache(i + 1, taches[i])
            trouve = True
    if not trouve:
        print("Aucune tache ne correspond.")
def modifier_tache(taches):
    if len(taches) == 0:
        print("Aucune tache a modifier.")
        return
    numero = saisir_entier("Numero de la tache a modifier : ")
    if numero < 1 or numero > len(taches):
        print("Erreur : ce numero n'existe pas.")
    else:
        taches[numero - 1][0] = saisir_texte("Nouveau titre : ")
        taches[numero - 1][1] = saisir_texte("Nouvelle description : ")
        taches[numero - 1][2] = saisir_priorite()
        print("Tache modifiee.")
def afficher_menu():
    print()
    print("GESTIONNAIRE DE TACHES")
    print("1 : ajouter une tache")
    print("2 : afficher les taches")
    print("3 : rechercher une tache")
    print("4 : modifier une tache")
    print("0 : quitter")



def main():
    taches = []
    choix = -1
    while choix != 0:
        afficher_menu()
        choix = saisir_entier("Votre choix : ")
        if choix == 1:
            ajouter_tache(taches)
        elif choix == 2:
            afficher_taches(taches)
        elif choix == 3:
            rechercher_tache(taches)
        elif choix == 4:
            modifier_tache(taches)
        elif choix == 0:
            print("Au revoir !")
        else:
            print("Erreur : choix inexistant (0 a 4).")