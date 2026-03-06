import json

OPTION = "1)Rajouter une ville\n2)Rajouter des route\n3)Générer le JSON\n"


def addNode(listVille):
    """
        Ajoute une ville à la liste des villes via une saisie utilisateur.

        L'utilisateur saisit le nom d'une ville qui est ensuite ajouté
        à la liste des villes du graphe.

        :param listVille: liste contenant les villes du graphe.
        """
    nomVille = input("Nom de la ville : ")
    listVille.append(nomVille)


def addArc(listVille, listeRoute):
    """
        Ajoute une route entre deux villes existantes.

        L'utilisateur sélectionne deux villes dans la liste et indique
        la distance (en kilomètres) entre celles-ci. La route est ensuite
        ajoutée à la liste des arêtes du graphe.

        :param listVille: liste des villes disponibles.
        :param listeRoute: liste des routes du graphe.
    """
    option = ""
    for i in range(len(listVille)):
        option += "\n" + str(i + 1) + ") " + listVille[i]
    option += "\n"
    tmp = input("ville 1 : " + option)
    node1 = listVille[int(tmp) - 1]
    option = ""
    for i in range(len(listVille)):
        if i != int(tmp) - 1:
            option += "\n" + str(i + 1) + ") " + listVille[i]

    node2 = listVille[int(input("ville 2 : " + option)) - 1]
    while node1 == node2:
        node2 = listVille[int(input("Ne pas choisir la même ville que la ville 1 : " + option)) - 1]
    distance = int(input("Distance en km entre les deux ville : "))
    listeRoute.append({
        "id": len(listeRoute),
        "node1": node1,
        "node2": node2,
        "distance": distance
    })


def createJson(listVille, listRoute):
    """
        Génère un fichier JSON contenant les données du graphe.

        Le fichier JSON contient :
        - la liste des villes (nodes)
        - la liste des routes avec leurs distances (edges)

        :param listVille: liste des villes.
        :param listeRoute: liste des routes reliant les villes.
    """
    listes = {"nodes": listVille, "edges": listRoute}
    jsName = input("Nom du fichier .json ?\n")
    with open("json/" + jsName + ".json", "w") as f:
        json.dump(listes, f, indent=4)


def main():
    """
        Programme principal permettant de créer ou modifier un fichier JSON
        représentant un graphe de villes et de routes.

        Au lancement, l'utilisateur peut :
        - créer un nouveau fichier JSON
        - charger un fichier JSON existant

        Une fois le graphe chargé ou créé, un menu interactif permet :
        - d'ajouter des villes
        - d'ajouter des routes entre les villes
        - de générer le fichier JSON final.
    """

    listVille = []
    listRoute = []

    print("1) Créer un nouveau fichier")
    print("2) Charger un fichier JSON existant")

    choix = int(input("Choix : "))

    if choix == 2:
        jsName = input("Nom du fichier JSON à charger : ")
        with open("json/" + jsName + ".json", "r") as f:
            data = json.load(f)
            listVille = data["nodes"]
            listRoute = data["edges"]

    opt = 0

    while opt != 3:
        opt = int(input(OPTION))

        while opt < 1 or opt > 3:
            opt = int(input(OPTION))

        if opt == 1:
            addNode(listVille)

        elif opt == 2:
            if len(listVille) > 1:
                addArc(listVille, listRoute)
            else:
                print("Il faut au moins deux villes pour créer une route.")

    createJson(listVille, listRoute)


if __name__ == "__main__": main()