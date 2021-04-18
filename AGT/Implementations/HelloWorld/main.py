import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    # Creating new graph
    G = nx.Graph()

    # Adding one node
    G.add_node(1)  # Number is the ID of the node

    # Adding multiple nodes
    G.add_nodes_from([2, 3])

    # Adding nodes with attributes
    G.add_nodes_from([
        (4, {"color": "red"}),
        (5, {"color": "green"}),
    ])

    # Adding one edge
    G.add_edge(1, 2)

    # Adding multiple edges
    G.add_edges_from([(3, 2), (4, 2), (1, 4)])

    # Adding edges with attributes
    G.add_edges_from([
        (5, 2, {"weight": 3})
    ])

    # List of nodes / edges
    print("Nodes of G: {}".format(G.nodes))
    print("Edges of G: {}".format(G.edges))

    # Getting adjacent nodes
    print("Nodes adjacent to 2: {}".format(list(G.neighbors(2))))

    # Getting degree of node
    print("Degree of node 2: {}".format(G.degree[2]))

    # Edges of multiple nodes
    print("Edges of nodes 2 and 3: {}".format(G.edges([2, 3])))

    # Degree of multiple nodes
    print("Degree of nodes 2 and 3: {}".format(list(G.degree([2, 3]))))

    # Removing a node

    # Plotting
    nx.draw(G)
    plt.show()