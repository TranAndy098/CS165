# explanations for these functions are provided in requirements.py

from graph import Graph
import random

def BFS(graph: Graph, node: int):
	level = -1
	explored = [0] * graph.get_num_nodes()
	need_to = [node]
	last_exp = None
	while len(need_to) > 0:
		new_nodes = []
		for n in need_to:
			for i in graph.get_neighbors(n):
				if explored[i] == 0:
					new_nodes.append(i)
					explored[i] = 1
		last_exp = n
		need_to = new_nodes
		level += 1
	return level, last_exp

def get_diameter(graph: Graph) -> int:
	d = 0
	node = random.randint(0, graph.get_num_nodes()-1)
	stop = False
	while not stop:
		distance, furthest = BFS(graph, node)
		if distance > d:
			d = distance
			node = furthest
		else:
			stop = True
	return d


def old_get_clustering_coefficient(graph: Graph) -> float:
	denominator = 0
	for node in range(graph.get_num_nodes()):
		degree = len(graph.get_neighbors(node))
		denominator += ((degree) * (degree -1)) / 2
	
	dict_neighbors = []
	for i in range(graph.get_num_nodes()):
		indiv = {}
		i_neighbors = graph.get_neighbors(i)
		for j in i_neighbors:
			indiv[j] = 1
		dict_neighbors.append(indiv)
	
	numerator = 0
	for i in range(graph.get_num_nodes()):
		for j in range(i+1,graph.get_num_nodes()):
			for k in range(j+1,graph.get_num_nodes()):
				if j in dict_neighbors[i] and k in dict_neighbors[i] and k in dict_neighbors[j]:
					print(i,j,k)
					numerator += 3
	print(numerator)
	return numerator/denominator


def get_degree_distribution(graph: Graph) -> dict[int, int]:
	count = {}
	for node in range(graph.get_num_nodes()):
		degree = len(graph.get_neighbors(node))
		if degree in count:
			count[degree] += 1
		else:
			count[degree] = 1
	return count

def get_clustering_coefficient(graph: Graph) -> float:
	num = graph.get_num_nodes()

	denominator = 0
		
	each_node_degree = {}

	dict_neighbors = []
	for i in range(graph.get_num_nodes()):
		indiv = {}
		i_neighbors = graph.get_neighbors(i)
		for j in i_neighbors:
			indiv[j] = 1
		dict_neighbors.append(indiv)

	ol = []
	l = {}
	d = {}
	n = {}

	for node in range(num):
		
		degree = len(graph.get_neighbors(node))
		denominator += ((degree) * (degree -1)) / 2

		n[node] = []
		each_node_degree[node] = degree
		if degree in d:
			d[degree].append(node)
		else:
			d[degree] = [node]

	#print(d)
	#print(n)
	#print("\n")

	k = 0

	for _ in range(num):
		i = min(d.keys())
		k = max(k,i)
		v = d[i][0]
		if i in d:
			if len(d[i]) == 1:
				d.pop(i)
			else:
				d[i].pop(0)
		ol = [v] + ol
		print("vertex: ", v)
		print(graph.get_neighbors(v))
		if v not in l:
			for w in graph.get_neighbors(v):
				if w not in l:
					print("neighbor: ", w)
					dw = each_node_degree[w]
					print("before: ", dw)
					if dw in d:
						if len(d[dw]) == 1:
							d.pop(dw)
						else:
							d[dw].remove(w)
					each_node_degree[w] -= 1
					dw -= 1
					if dw in d:
						d[dw].append(w)
					elif dw >= 0:
						d[dw] = [w]
					print("after: ", dw)
					n[v].append(w)
				
			
			print(d)
			print(n)
			print("\n")

		l[v] = 1
		if len(d.keys()) == 0:
			break

	numerator = 0

	print(ol)
	for u in ol:
		for i in range(len(n[u])):
			v = n[u][i]
			for j in range(i, len(n[u])):
				w = n[u][j]

				if v in dict_neighbors[u] and w in dict_neighbors[u] and w in dict_neighbors[v]:
					#print(u,v,w)
					numerator += 3
	
	#print(numerator)
	return numerator / denominator



	


g = Graph(10, {(0, 3), (0, 7), (1, 4), (1, 5), (1, 6), (2, 3), (2, 7), (3, 4), (3, 8), (3, 9), (4, 5), (4, 9), (5, 6), (8, 9)})

get_clustering_coefficient(g)
old_get_clustering_coefficient(g)
