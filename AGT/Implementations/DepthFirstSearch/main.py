import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    G = nx.Graph()

    G.add_nodes_from(range(0, 9))

    # Creating edges
    # G.add_edge(0, 1)
    # G.add_edge(0, 7)
    G.add_edge(1, 2)
    G.add_edge(1, 7)
    G.add_edge(2, 3)
    G.add_edge(2, 5)
    # G.add_edge(2, 8)
    G.add_edge(3, 4)
    G.add_edge(3, 5)
    G.add_edge(5, 4)
    G.add_edge(6, 5)
    G.add_edge(7, 6)
    # G.add_edge(7, 8)
    # G.add_edge(8, 6)

    return G

def draw_graph(G):
    nx.draw(G)
    plt.show()

def DFS(G, v, discovered):
 
    # Marking current node as discovered
    discovered.append(v)

    # Executing DFS for all neighbors of v that are not discovered
    for neighbor in list(G.neighbors(v)):
        if neighbor not in discovered:
            DFS(G, neighbor, discovered)

if __name__ == "__main__":

    G = create_graph()

    # Stores all known nodes
    nodes = []

    # Executing DFS
    DFS(G, 1, nodes)

    # Printing all discovered nodes
    print("Nodes found in G: {}".format(sorted(nodes)))

    # Drawing graph
    draw_graph(G)