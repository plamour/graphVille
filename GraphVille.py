import json
import math
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



def Djikstra(G, start):
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

    def shortest_path(G, target):
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
    plt.figure(figsize=(25, 18))

    pos = nx.kamada_kawai_layout(G)

    path_edges = list(zip(path, path[1:]))
    edge_colors = []
    for u, v, data in G.edges(data=True):
        if (u, v) in path_edges or (v, u) in path_edges:
            edge_colors.append("red")
        else:
            edge_colors.append("lightgray")  # arête normale
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color="blue")
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(G, pos, width=2.5, edge_color=edge_colors)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

    plt.axis("off")
    plt.tight_layout()
    plt.show()


def main():
    G = getGraph()
    Djikstra(G,"Paris")
    path = multi_target_path(G,"Paris",("Nice","Strasbourg"))
    drawGraph(G,path)

if __name__ == "__main__": main()