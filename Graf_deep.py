import networkx as nx
import Tasks.my_stack as st
import matplotlib.pyplot as plt

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

visited_list = ['A']
st.push('A')
result = []


while st.len_stack() > 0:
       verch = st.pop()
       for nei in G.neighbors(verch):
           if nei not in visited_list:
               my_cost = int(G.get_edge_data(verch, nei)['weight'])
               result.append((verch, nei, my_cost))
               visited_list.append(nei)
               st.push(nei)

print(result)


# nx.draw(G,with_labels=True)
# plt.show()
