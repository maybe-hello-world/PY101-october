import networkx as nx

g = nx.Graph()

nodes = list("ABCDEFG")
g.add_nodes_from(nodes)

edges = [
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
    ('F', 'G'),

]

g.add_edges_from(edges)


# def count_sv(g:nx.Graph):
#     return len(g.nodes) % len(g.edges)


# merged = 0
# nei_list = []
# visited_list = []
#
# def add_nei(x):
#     nei_list.append(x)
#     for i in g.neighbors(x):
#         nei_list.append(i)
#     return
#
# # for x in g.nodes:
# #     if any(g.neighbors(x)) == False:
# #         merged += 1
# #
# #     # if x not in visited_list:
# #     #     if x not in nei_list:
# #     #         add_nei(x)
# #     #     else:
# #     #         merged +=1
# #     #         nei_list.clear()
# #     #     visited_list.append(x)
# #     else:
# #         nei_list.append(x)
# #         for i in g.neighbors(x):
# #             nei_list.append(i)
# #         for y in range(1,len(nei_list)):
# #             if y not in
# #
# #
# #
# #
# #
# # print(merged)
# # print(nei_list)
# # print(visited_list)

x = 
