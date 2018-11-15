"""
This module implements some functions based on linear search algo
"""
import networkx as nx


G = nx.Graph()
nodes = list("ABCDEFGH")
G.add_nodes_from(nodes)

edges = [
    ('A', 'B', 1),
    ('A', 'C', 17),
    ('A', 'D', -3),
    ('A', 'E', 14),
    ('A', 'F', 2),
    ('B', 'C', 99),
    ('B', 'E', 132),
    ('C', 'D', 21),
    ('C', 'F', 331),
    ('E', 'D', 14),
    ('E', 'F', -36),
    ('G', 'F', -36),
    ('H', 'F', -36),
    ('G', 'H', -35.9999999)
]

G.add_weighted_edges_from(edges)

def min_search(arr) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    my_min = arr[0]
    for i in arr:
        if i <= my_min:
            my_min = i
        else:
            continue
    return my_min


def min_weight_search(Graph):
    """
    Function that find edge in graph with minimal weight of all

    :param Graph: NetworkX Graph (or digraph) with weighted edges
    :return: tuple of nodes (node, node) the weight of edge between which is minimal (any occurrence)
    """
    my_min = Graph.get_edge_data(*list(Graph.edges)[0])['weight']
    for gr in Graph.edges:
        my_cost = int(Graph.get_edge_data(*gr)['weight'])
        if my_cost < my_min:
            my_min = my_cost
            res = gr

    return res

print(min_weight_search(G))
