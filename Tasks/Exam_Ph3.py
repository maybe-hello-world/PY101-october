import networkx as nx

node = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edge = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('F', 'G')]
a = node[0]
graph = nx.Graph()
graph.add_nodes_from(node)
graph.add_edges_from(edge)
visited = []
n = len(node)
stack = []
cnt = 0


def dfs():
    tmp = []
    tprev = []
    cnt=0
    for v in node:
        visited = [v]
        stack.append(v)
        while len(stack) > 0:
            a = stack.pop()
            for j in graph.neighbors(a):
                if j not in visited:
                    stack.append(j)
                    visited.append(j)
        tmp = sorted(visited)
        # print(tprev)
        if tmp not in tprev:
            cnt+=1
            tprev.append(tmp)
            # print(tprev)
        else:
            pass
    return cnt
print(dfs())