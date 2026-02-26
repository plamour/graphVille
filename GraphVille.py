import json

import matplotlib.pyplot as plt
import networkx as nx

def jsonToGraph(jsName):
    with open("json/"+jsName+".json", "r") as f:
        listes = json.load(f)
    return listes


def getGraph():
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


def main():
    # Assume you already have G = getGraph()
    G = getGraph()  # your MultiGraph

    plt.figure(figsize=(25, 18))
    pos = nx.kamada_kawai_layout(G)
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=800, node_color="skyblue")
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    plt.axis("off")
    plt.tight_layout()
    plt.show()





if __name__ == "__main__": main()