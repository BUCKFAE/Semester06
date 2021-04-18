import networkx as nx
import matplotlib.pyplot as plt
import math


def create_graph():
    G = nx.Graph()

    G.add_nodes_from(range(0, 9))

    # Creating weighted edges
    G.add_edge(0, 1, weight=4)
    G.add_edge(0, 7, weight=8)
    G.add_edge(1, 2, weight=8)
    G.add_edge(1, 7, weight=11)
    G.add_edge(2, 3, weight=7)
    G.add_edge(2, 5, weight=4)
    G.add_edge(2, 8, weight=2)
    G.add_edge(3, 4, weight=9)
    G.add_edge(3, 5, weight=14)
    G.add_edge(5, 4, weight=10)
    G.add_edge(6, 5, weight=2)
    G.add_edge(7, 6, weight=1)
    G.add_edge(7, 8, weight=7)
    G.add_edge(8, 6, weight=6)

    return G

def draw_graph(G):
    pos=nx.spring_layout(G)
    nx.draw_networkx(G,pos)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.show()


def Dijkstra(G, start):

    Q = []

    distances = {}
    prev = {}

    # Initializing
    for vertex in G.nodes:
        distances[vertex] = math.inf
        prev[vertex] = None
        Q.append(vertex)

    # Distance for start node
    distances[start] = 0

    while Q:
        
        # Next node: Node closest to subgraph
        u = min(Q, key=lambda k: distances[k])
        Q.remove(u)
        
        # Is there a path from a to b via u which is shorter than the known one
        for neighbor in G.neighbors(u):
            # Path from a to b via u
            alt = distances[u] + G.get_edge_data(u, neighbor)["weight"]

            # Replacing shortest known path to neighbour if we found a better path
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                prev[neighbor] = u

    # Returning distances and path to all nodes
    return distances, prev

if __name__ == "__main__":
    Graph = create_graph()
    d, p = Dijkstra(Graph, 0)
    print(d)
    print(p)

    draw_graph(Graph)
