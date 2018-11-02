import networkx as nx

visited = []

infx = float("inf")
nodes = {'a': infx, 'b': infx, 'c': infx, 'd': infx, 'e': infx}

G = nx.DiGraph()
G.add_nodes_from(nodes.keys())  # nodes
G.add_weighted_edges_from([('a', 'd', 60), ('a', 'c', 12),
                           ('b', 'a', 10),
                           ('c', 'd', 32), ('c', 'b', 20),
                           ('e', 'a', 7)])

def getmincostnode():

    nodewtmin = None
    wtmin = infx
    for x in nodes.items():
        if (x[1] < wtmin) and (x[0] not in visited):
            wtmin = x[1]
            nodewtmin = x[0]

    return nodewtmin


def run(node='a', endnode = None):
    """
        node : начальная вершина
        endnode : конечная вершина; если не задана (None), то получаем стоимость до каждой

    """
    nodes[node] = 0

    while node!= endnode:
        visited.append(node)
        for nbr in G.neighbors(node):
            wt = G[node][nbr]['weight']
            newcost = nodes[node] + wt
            if nodes[nbr] > newcost:
                nodes[nbr] = newcost
        node = getmincostnode()

    else:
        if node != None:
            visited.append(node)

    return visited

run()
# run('e')
# run('e', 'c')
print("nodes", nodes)
print("visited", visited)
