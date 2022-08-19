class NonOrientedGraph:
    """
    Non-oiented graph class
    """

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_matrix = None

    @classmethod
    def generate_with_adjacency_matrix(cls, matrix):
        pass

    def adjacent(self, vrtx1, vrtx2):
        """
        Are to vertices neighbors?
        :param vrtx1:
        :param vrtx2:
        :return: boolean
        """
        for k in self.edges:
            if k == [vrtx1, vrtx2] or k == [vrtx2, vrtx1]:
                return True
        return False

    def build_adjacency_matrix(self):
        """
        Create the adjacency matrix corresponding to this graph.
        :return:
        """
        number_vertices = len(self.vertices)
        self.adjacency_matrix = []
        for i in range(number_vertices):
            potential_neighbors = []
            for j in range(number_vertices):
                if self.adjacent(self.vertices[i], self.vertices[j]):
                    potential_neighbors.append(1)
                else:
                    potential_neighbors.append(0)
            self.adjacency_matrix.append(potential_neighbors)

    def get_adjacency_matrix(self):
        """
        Return the adjacency matrix
        :return: matrix (list of list)
        """
        return self.adjacency_matrix

    def adjacency_list(self):
        """
        Return dictionary representing adjacency list.
        Keys => vertices
        Values => list of adjacent vertices
        :return: dict
        """
        dic = dict()
        for vertex in self.vertices:
            neighbors = []
            for edge in self.edges:
                if edge[0] == vertex:
                    neighbors.append(edge[1])
                elif edge[1] == vertex:
                    neighbors.append(edge[0])
                dic[vertex] = neighbors

        return dic
