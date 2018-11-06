import networkx as nx


def dijkstra_algo(G, starting_node) -> dict:
	"""
	Count shortest paths from starting node to all nodes of graph G

	:param G: Graph from NetworkX
	:param starting_node: starting node from G
	:return: dict like {'node1': 0, 'node2': 10, '3': 33, ...}, where nodes are nodes from G
	"""
	visited = []
	stoimost = {i: float("inf") for i in list(G.nodes)}
	stoimost[starting_node] = 0
	while len(visited) != len(G.nodes):
		def min_n():
			key = ""
			value = float('inf')
			for j in stoimost:
				if j not in visited and stoimost[j] <= value:
						key = j
						value = stoimost[j]
			return key

		miv = min_n()
		for i in G.neighbors(miv):
			if stoimost[i] > stoimost[miv] + G[miv][i]['weight']:
				stoimost[i] = stoimost[miv] + G[miv][i]['weight']
		visited.append(miv)
	return stoimost

	# return dict()
