import networkx as nx

# Поиск в ширину\
def width():
    G1 = nx.Graph()
    nodes_my = ['a', 'b', 'c', 'd', 'e', 'f']
    G1.add_nodes_from(nodes_my)
    edge_my = [('a','b'), ('a','d'), ('b','c'), ('b','d'), ('c','d'),('d','e'), ('d','f'), ('f','e')]
    G1.add_edges_from(edge_my)

    arr = [] # добавляем посещенные вершины
    queue = ['a'] # добавляем начальную вершину
    while queue!=[]:
        vertex = list(G1.neighbors(queue[0]))
        arr.append(queue[0])
        del queue[0]
        for it in range(len(vertex)):
            if (vertex[it] in arr) or (vertex[it] in queue):
                continue
            else:
                queue.append(vertex[it])
    return arr

print(width())

# Поиск в глубину
def depth():
    G1 = nx.Graph()
    nodes_my = ['a', 'b', 'c', 'd', 'e', 'f']
    G1.add_nodes_from(nodes_my)
    edge_my = [('a','b'), ('a','d'), ('b','c'), ('b','d'), ('c','d'),('d','e'), ('d','f'), ('f','e')]
    G1.add_edges_from(edge_my)

    arr = [] # добавляем посещенные вершины
    stack = ['a'] # добавляем начальную вершину
    while stack!=[]:
        vertex = list(G1.neighbors(stack[-1]))
        arr.append(stack[-1])
        stack.pop()
        for it in range(len(vertex)):
            if (vertex[it] in arr) or (vertex[it] in stack):
                continue
            else:
                stack.append(vertex[it])
    return arr

print(depth())

