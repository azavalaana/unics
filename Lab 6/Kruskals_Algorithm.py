# This class have a generic graph and dsf methods
class Generic_Graph:

    edges = []
    weight = []
    vertices = []

    def __init__(self, edge_list, weight):
        self.edges.append(edge_list)
        self.weight.append(weight)

    # This method sorts the edges and the weights
    def __sort(self):
        if len(self.edges) != len(self.weight):
            return
        for i in range(1, len(self.weight)):
            temp_weight = self.weight[i]
            temp_edge = self.edges[i]
            current = i - 1
            while current >= 0 and temp_weight < self.weight[current]:
                self.weight[current + 1] = self.weight[current]
                self.edges[current + 1] = self.edges[current]
                current -= 1
            self.weight[current + 1] = temp_weight
            self.edges[current + 1] = temp_edge

    # Creates the sets used for the kruskal's algorithm
    def make_set(self):
        for i in range(len(self.edges)):
            for j in range(len(self.edges[i])):
                if self.edges[i][j] not in self.vertices:
                    self.vertices.append(self.edges[i][j])

        for k in range(len(self.vertices)):
            self.vertices[k] = [self.vertices[k]]

    # Finds the set to which a vertex belongs
    def find_set(self, vertex):
        for i in range(len(self.vertices)):
            for element in self.vertices[i]:
                if element == vertex:
                    return i
        return None

    # Unite two vertices together
    def __union(self, vertex1, vertex2):
        index1 = self.find_set(vertex1)
        index2 = self.find_set(vertex2)
        for element in self.vertices[index2]:
            self.vertices[index1].append(element)
        self.vertices.pop(index2)

    # Adds an edge to the graph
    def add(self, edge_list, weight):
        self.edges.append(edge_list)
        self.weight.append(weight)

    # Kruskal's Algorithm
    def kruskal_alg(self):
        self.__sort()
        self.make_set()
        count, i = 0, 0
        while len(self.vertices) > 1:
            if self.find_set(self.edges[i][0]) != self.find_set(self.edges[i][1]):
                print("(%d %d) edge selected." % (self.edges[i][0], self.edges[i][1]))
                count += 1
                self.__union(self.edges[i][0], self.edges[i][1])
            i += 1

    # Prints all edges and their corresponding edges
    def print_graph(self):
        print("Edges:")
        print(self.edges)
        print("Weights for Edges:")
        print(self.weight)
