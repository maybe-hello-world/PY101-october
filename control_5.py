import networkx as nx
import Tasks.my_queue as que

G = nx.Graph()

nodes = list("ABCDEFG")
G.add_nodes_from(nodes)

edges = [
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
    ('F', 'G'),

]

G.add_edges_from(edges)

slist = []
prev_slist = []
my_con = 0

for i in G.nodes:
    visited_list = [i]
    que.enqueue(i)

    while que.len_que() > 0:
           verch = que.dequeue()
           for i in G.neighbors(verch):
               if i not in visited_list:
                   visited_list.append(i)
                   que.enqueue(i)
    slist = sorted(visited_list)
    #print(slist)
    if slist != prev_slist:
        my_con += 1
        prev_slist = slist
    else:
        continue
print(my_con)
