"""
This module implements some functions based on linear search algo
"""
import networkx as nx

def min_search(arr) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	min = arr[0]
	for i in range(1,len(arr)):
		if arr[i] < min:
			min = arr[i]
	return min


def min_weight_search(Graph:nx.Graph) -> tuple:
	"""
	Function that find edge in graph with minimal weight of all

	:param Graph: NetworkX Graph (or digraph) with weighted edges
	:return: tuple of nodes (node, node) the weight of edge between which is minimal (any occurrence)
	"""
	key = list()
	weight = float('0')
	for (u, v) in Graph.edges:
		if Graph[u][v]['weight'] <= weight:
			weight = Graph[u][v]['weight']
	for (u, v) in Graph.edges:
		if Graph[u][v]['weight'] == weight:
			key.append((u, v))

	return tuple(key)
