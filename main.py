from graph import NonOrientedGraph
from utils.logger import log_matrix

vertices = [0, 1, 2, 3, 4]
edges = [[0, 1], [0, 2], [0, 4], [1, 3], [1, 2], [2, 4], [2, 3]]
graph = NonOrientedGraph(vertices, edges)

graph.build_adjacency_matrix()
log_matrix(graph.get_adjacency_matrix())
