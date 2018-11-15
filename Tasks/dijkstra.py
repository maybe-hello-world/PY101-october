import networkx as nx
import math



def min_nod_search(slov:dict,vis_list):
    result = -1
    my_min = math.inf
    for my_node in slov.keys():
        if my_node not in vis_list:
            if slov[my_node] <= my_min:
                my_min = slov[my_node]
                result = my_node
        else:
            continue
    return result


def dijkstra_algo(G, starting_node, stop = -1) -> dict:
    """
    Count shortest paths from starting node to all nodes of graph G

    :param G: Graph from NetworkX
    :param starting_node: starting node from G
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...}, where nodes are nodes from G
    """
    visited_list = []
    nodes = G.nodes
    path = {i: math.inf for i in nodes}
    path[starting_node] = 0

    while len(nodes) != len(visited_list):
        min_nod = min_nod_search(path,visited_list)
        if min_nod == stop:
            break
        for nei in G.neighbors(min_nod):
            my_cost = path[min_nod] + int(G.get_edge_data(min_nod, nei)['weight'])
            if path[nei] > my_cost:
                path[nei] = my_cost
        visited_list.append(min_nod)
    return path
