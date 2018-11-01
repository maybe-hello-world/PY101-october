import networkx as nx

node = ['a', 'b', 'c', 'd', 'e']
line = [('e', 'a', 7), ('a', 'd', 60), ('a', 'c', 12), ('c', 'd', 32), ('c', 'b', 20), ('b', 'a', 10)]


def find():
    g = nx.DiGraph()
    g.add_nodes_from(node)
    g.add_weighted_edges_from(line)  # передаем сразу ребра с весом из line
    visited = []
    stoimost = {node[0]: float("inf"), node[1]: float('inf'), node[2]: float('inf'), node[3]: float('inf'), node[4]: 0}
    # можно реализовывать через сравнение множества node и visited
    # ....
    # а можно через сравнение длины списка посещенных вершин с заданным списком
    while len(visited) != len(node):
        def min_n():
            key = ""
            value = float('inf')
            for j in node:
                if j not in visited:
                    if stoimost[j] < value:
                        key = j
                        value = stoimost[j]
            return key
        miv = min_n()
        for i in g.neighbors(miv):
            if stoimost[i] > stoimost[miv] + g[miv][i]['weight']:
                stoimost[i] = stoimost[miv] + g[miv][i]['weight']
        visited.append(miv)
    return stoimost


print(find())
