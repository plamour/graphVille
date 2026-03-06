import json
import math
import matplotlib.pyplot as plt
import networkx as nx

def jsonToGraph(jsName):
    """
        Charge un graphe depuis un fichier JSON.

        :param jsName: nom du fichier JSON (sans l'extension).
        :return: dictionnaire contenant les listes de noeuds et d'arêtes.
    """
    with open("json/"+jsName+".json", "r") as f:
        listes = json.load(f)
    return listes


def getGraph():
    """
        Construit un graphe NetworkX à partir d'un fichier JSON.

        :return: graphe MultiGraph contenant les villes et les routes.
    """
    listes = jsonToGraph(input("Name of the file ? : \n"))
    nodes = listes['nodes']
    edges = listes['edges']
    G = nx.MultiGraph()
    for node in nodes:
        G.add_node(node)
    for edge in edges:
        G.add_edge(
            edge["node1"],
            edge["node2"],
            id=edge["id"],
            weight=edge["distance"]
        )

    return G



def Djikstra(G, start):
    """
        Applique l'algorithme de Dijkstra sur un graphe.

        :param G: graphe NetworkX.
        :param start: noeud de départ.
        :return: graphe avec les poids minimum et les prédécesseurs calculés.
    """
    for node in G.nodes:
        G.nodes[node]['weight'] = math.inf
        G.nodes[node]['pred'] = None

    G.nodes[start]['weight'] = 0

    X = set(G.nodes)
    E = set()

    while X:
        x = min(X, key=lambda n: G.nodes[n]['weight'])
        X.remove(x)
        E.add(x)

        for y in G.neighbors(x):
            if y in X:
                w = G[x][y][0]['weight']

                if G.nodes[y]['weight'] > G.nodes[x]['weight'] + w:
                    G.nodes[y]['weight'] = G.nodes[x]['weight'] + w
                    G.nodes[y]['pred'] = x

    return G

def multi_target_path(G, source, targets):
    """
        Calcule un chemin passant par plusieurs villes cibles.

        :param G: graphe NetworkX.
        :param source: ville de départ.
        :param targets: liste des villes à visiter dans l'ordre.
        :return: liste représentant le chemin complet.
    """

    def shortest_path(G, target):
        """
            Reconstruit le chemin le plus court vers une cible.

            :param G: graphe NetworkX avec prédécesseurs calculés.
            :param target: ville cible.
            :return: liste représentant le chemin.
        """
        path = []
        current = target

        while current is not None:
            path.append(current)
            current = G.nodes[current]['pred']

        path.reverse()
        return path

    full_path = []
    current = source

    for target in targets:
        Djikstra(G, current)
        segment = shortest_path(G, target)
        if full_path:
            segment = segment[1:]
        full_path.extend(segment)
        current = target
    return full_path



def drawGraph(G,path):
    """
        Affiche le graphe et met en évidence le chemin trouvé.

        :param G: graphe NetworkX.
        :param path: liste représentant le chemin calculé.
    """
    plt.figure(figsize=(25, 18))

    pos = nx.kamada_kawai_layout(G)

    path_edges = list(zip(path, path[1:]))
    edge_colors = []
    for u, v, data in G.edges(data=True):
        if (u, v) in path_edges or (v, u) in path_edges:
            edge_colors.append("red")
        else:
            edge_colors.append("lightgray")
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color="blue")
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(G, pos, width=2.5, edge_color=edge_colors)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

    plt.axis("off")
    plt.tight_layout()
    plt.show()


def main():
    """ Menu interactif permettant de calculer un chemin entre plusieurs villes. L'utilisateur choisit :

    - un fichier JSON contenant le graphe
    - une ville de départ
    - une ou plusieurs villes cibles

    Le programme calcule ensuite le chemin le plus court et affiche le graphe.
    """
    G = getGraph()

    print("\n--- MENU CHEMIN ENTRE VILLES ---\n")

    print("Villes disponibles :")
    print(", ".join(G.nodes))
    print()

    while True:
        start = input("Ville de départ : ")
        if start in G.nodes:
            break
        else:
            print("Ville invalide, réessaie.")

    targets = []

    while True:
        while True:
            city = input("Ville suivante : ")
            if city in G.nodes:
                targets.append(city)
                break
            else:
                print("Ville invalide, réessaie.")

        add_more = input("Ajouter une autre ville ? (o/n) : ").lower()

        if add_more != "o":
            break

    path = multi_target_path(G, start, targets)

    print("\nChemin trouvé avec distances :")
    total_distance = 0
    for i in range(len(path)-1):
        u = path[i]
        v = path[i+1]
        w = min([edata['weight'] for edata in G.get_edge_data(u, v).values()])
        total_distance += w
        print(f"{u} -> {v} : {w} km")
    print(f"Distance totale : {total_distance} km\n")

    drawGraph(G, path)
if __name__ == "__main__": main()