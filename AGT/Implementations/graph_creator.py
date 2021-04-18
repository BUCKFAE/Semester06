"""Used to create different graphs"""

from typing import List

import networkx as nx


def create_circle(node_count=7) -> nx.Graph:
    """Creates a circle

    Keyword arguments:
    node_count -- amount of nodes present in the circle
    """

    # Creating the blank graph
    graph = nx.Graph()

    # Adding nodes
    graph.add_nodes_from(range(0, node_count - 1))

    # Adding edges of the circle
    graph.add_edges_from([(start, start + 1) for start in range(node_count - 1)])
    graph.add_edge(node_count - 1, 0)

    # Returning the graph
    return graph

def create_example_graph_01() -> nx.Graph:
    """Creates the first example graph"""

    # Creating the blank graph
    graph = nx.Graph()

    # Adding nodes
    graph.add_nodes_from(range(0, 9))

    # Stores all edges
    edges = [
        (0, 1), (0, 7),
        (1, 2), (1, 7),
        (2, 3), (2, 5), (2, 8),
        (3, 4), (3, 5),
        (5, 4),
        (6, 5),
        (7, 6),
        (7, 8),
        (8, 6)]

    # Adding the edges
    graph.add_edges_from(edges)

    # Returning the graph
    return graph

def remove_edges_to(graph: nx.Graph, edge_list: List[int]) -> None:
    """Removes all edges to and from the given list from the graph"""

    # Getting the edges that should be removed
    edges_to_remove = [edge for edge in graph.edges if edge[0] in edge_list or edge[1] in edge_list]

    # Removing the edges
    graph.remove_edges_from(edges_to_remove)
