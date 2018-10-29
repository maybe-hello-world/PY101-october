import networkx as nx
import my_queue
import my_stack

tracker = []

def init():

    nodes = ['a', 'b', 'c', 'd', 'e', 'f']

    G = nx.Graph()
    G.add_nodes_from(nodes)

    G.add_edge('a', 'b')
    G.add_edge('a', 'd')

    G.add_edge('b', 'a')
    G.add_edge('b', 'c')
    G.add_edge('b', 'd')

    G.add_edge('c', 'b')
    G.add_edge('c', 'd')

    G.add_edge('d', 'a')
    G.add_edge('d', 'b')
    G.add_edge('d', 'c')
    G.add_edge('d', 'e')
    G.add_edge('d', 'f')

    G.add_edge('e', 'd')
    G.add_edge('e', 'f')

    G.add_edge('f', 'd')
    G.add_edge('f', 'e')
    return G


def initFromSlide30():

    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from([('a', 'b'), ('a', 'f'), ('b', 'g'), ('b', 'a'), ('f', 'g'), ('f', 'a'),
                      ('g', 'b'), ('g', 'c'), ('g', 'f'), ('g', 'i'), ('g', 'h'), ('g', 'c'),
                      ('c', 'g'), ('c', 'h'), ('a', 'f'), ('i', 'g'), ('i', 'h'),
                      ('h', 'c'), ('h', 'g'), ('h', 'i'),('h', 'j'), ('h', 'e'), ('h', 'd'),
                      ('d', 'h'), ('d', 'e'), ('a', 'f'),
                      ('j', 'h'),])


    return G


def runWideSearch(G):
    my_queue.clear()
    my_queue.enqueue('a')
    visited = ['a']

    while len(my_queue.queue) > 0:
        node = my_queue.dequeue()
        tracker.append(node)
        nd = list(G.neighbors(node))

        for x in nd:
            if x not in visited:
                visited.append(x)
                my_queue.enqueue(x)

    return tracker

def runDepthSearch(G):
    my_stack.clear()
    my_stack.push('a')
    visited = ['a']
    while len(my_stack.stack) > 0:
        node = my_stack.pop()
        # print('pop',node, my_stack.stack)
        tracker.append(node)

        nd = list(G.neighbors(node))  # G[node]

        for x in nd:
            if x not in visited:
                visited.append(x)
                my_stack.push(x)
                # print('push',x, my_stack.stack)
    return tracker


# print(runWideSearch(init()))
# print(runDepthSearch(init()))

tracker = []
print(runWideSearch(initFromSlide30()))

tracker = []
print(runDepthSearch(initFromSlide30()))

