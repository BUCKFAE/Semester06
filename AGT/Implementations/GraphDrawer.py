import networkx as nx
import matplotlib.pyplot as plt

from graph_creator import create_circle, create_example_graph_01,remove_edges_to

def draw_graph(G):
    nx.draw(G, with_labels=True)
    plt.show()

if __name__ == "__main__":

    G = create_circle(node_count=7)
    remove_edges_to(G, [2, 3])
    draw_graph(G)