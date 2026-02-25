import json

OPTION = "1)Rajouter une ville\n2)Rajouter des route\n3)Générer le JSON\n"


def addNode(listVille):
    """
        Rajoute des Ville à la liste interactivement.

        :param listVille: liste des villes.
        """
    nomVille = input("\nNom de la ville : ")
    listVille.append(nomVille)


def addArc(listVille,listeRoute):
    """
    Rajoute des routes à la liste interactivement.

    :param listVille: liste des villes.
    :param listeRoute: liste des Routes.
    """
    option = ""
    for i in range(len(listVille)):
        option += "\n"+str(i+1)+") " +listVille[i]
    option += "\n"
    node1 = listVille[int(input("ville 1 : " + option))-1]
    node2 = listVille[int(input("ville 2 : " + option))-1]
    while node1 == node2:
        node2 = listVille[int(input("Ne pas choisir la même ville que la ville 1 : " + option)) - 1]
    distance = int(input("Distance en km entre les deux ville : "))
    listeRoute.append({
        "id": len(listeRoute),
        "node1": node1,
        "node2": node2,
        "distance": distance
    })

def createJson(listVille,listRoute):
    """
        Crée le fichier JSON avec les listes.

        :param listVille: liste des ville.
        :param listeRoute: liste des Route.
        """
    listes = { "nodes": listVille, "edges": listRoute }
    jsName = input("Nom du fichier .json ?\n")
    with open(jsName+".json", "w") as f:
        json.dump(listes, f, indent=4)

def main():
    """
        Menu de sélection des option pour la création du JSON.

        :param listVille: liste des ville.
        :param listeRoute: liste des Route.
    """
    listVille = []
    listRoute = []
    opt = 0
    while opt != 3:
        opt = int(input(OPTION))
        while opt < 1 or opt > 3:
            opt = int(input(OPTION))
        if opt == 1:
            addNode(listVille)
        elif opt == 2:
            addArc(listVille,listRoute)
    createJson(listVille,listRoute)

if __name__ == "__main__": main()