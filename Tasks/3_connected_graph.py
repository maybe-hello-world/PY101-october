import networkx as nx

def con_graf():
    # Описание графа
    my_graph = nx.Graph()
    my_vertex = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    my_edge = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('f', 'g')]
    my_graph.add_nodes_from(my_vertex)
    my_graph.add_edges_from(my_edge)

    connected = 1 # счетчик для числа компонентов
    passed_tops = []
    stack = ['a']
    i = 0

    while len(passed_tops)!=len(my_vertex): # пока длина пройденных вершин не будет равна дл. всех вершин
        if stack == []: # проверка связности графа
            if my_vertex[i] in passed_tops: # содержатся ли вершины в пройденных
                i += 1
                continue
            else:
                stack.append(my_vertex[i]) # если нет, добавляем вершину в стек
                connected += 1 # подсчет заходов = числу компонентов связности
                continue

        while stack!=[]: # поиск в глубину
            neib = list(my_graph.neighbors(stack[-1])) #соседи вершин
            passed_tops.append(stack[-1])
            stack.pop()
            for it in range(len(neib)): # итерация по списку соседей
                if (neib[it] in stack) or (neib[it] in passed_tops): # проверка их наличия в стеке и проверенных вершинах
                    continue
                else:
                    stack.append(neib[it])
    return connected

print("число компонент связности = ", con_graf())