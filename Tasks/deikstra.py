import math
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
nodes = ['a','b','c','d','e']
edges = [('a','d',60),('a','c',12),('b','a',10),('c','b',20),('c','d',32),('e','a',7)]
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

visited_list = []
path = {i:math.inf for i in nodes}
path["e"] = 0
#print(path)


def min_nod_search(slov:dict):
    result = -1
    min = math.inf
    for my_node in slov.keys():
        if my_node not in visited_list:
            if slov[my_node] <= min:
                min = slov[my_node]
                result = my_node
        else:
            continue
    return result



def route_cost(table:dict,stop = -1):
#    while min_nod_search(table) != -1:
    while len(nodes) != len(visited_list):
        min_nod = min_nod_search(table)
        if min_nod == stop:
            break
        for nei in G.neighbors(min_nod):
            my_cost = table[min_nod] + int(G.get_edge_data(min_nod,nei)['weight'])
            if table[nei] > my_cost:
                table[nei] = my_cost
        visited_list.append(min_nod)
    return table


print(route_cost(path))
#print(visited_list)




#nx.draw(G, with_labels=True)
#plt.show()
