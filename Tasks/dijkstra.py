import networkx as nx

def dijkstra_algo(G, starting_node) -> dict:
    """
    Count shortest paths from starting node to all nodes of graph G

    :param G: Graph from NetworkX
    :param starting_node: starting node from G
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...}, where nodes are nodes from G
    """
    visited = []
    nodes = dict(G.nodes)
    for v in nodes:
        nodes[v] = float("inf")

    def getmincostnode():
        nodewtmin = None
        wtmin = float("inf")
        for x in nodes.items():
            if (x[1] < wtmin) and (x[0] not in visited):
                wtmin = x[1]
                nodewtmin = x[0]
        return nodewtmin

    node = starting_node
    endnode = None

    nodes[node] = 0
    while node != endnode:
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

    # print("visited", visited)
    # print("nodes", nodes)
    return nodes
