class Edge:
    def __init__(self, item, weight, dest):
        self.item = item
        self.weight = weight
        self.next = dest


# Graph class for the Adjacency List
class GraphAL:

    # Initializes graph
    def __init__(self, vertices, directed, weighted= False):
        self.al = [None] * vertices
        self.directed = directed
        self.weighted = weighted
        self.representation = 'AL'

    # Checks if a vertex is valid
    def is_valid_vertex(self, u):
        return 0 <= u < len(self.al)

    # Adds a vertex to the graph
    def add_vertex(self):
        self.al.append(None)

        return len(self.al) - 1  # Return new vertex id

    # Adds edge to the graph
    def insert_edge(self, src, dest, weight=1.0):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        self.al[src] = Edge(dest, weight, self.al[src])

        if not self.directed:
            self.al[dest] = Edge(src, weight, self.al[dest])

    # Removes edge from graph
    def delete_edge(self, src, dest):
        self.__delete_edge(src, dest)

        if not self.directed:
            self.__delete_edge(dest, src)

    # Removes a directed edge from graph
    def __delete_edge(self, src, dest):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        if self.al[src] is None:
            return

        if self.al[src].item == dest:
            self.al[src] = self.al[src].next
        else:
            prev = self.al[src]
            cur = self.al[src].next

            while cur is not None:
                if cur.item == dest:
                    prev.next = cur.next
                    return

                prev = prev.next
                cur = cur.next

        return len(self.al)

    # Returns the number of vertices
    def num_vertices(self):
        return len(self.al)

    # Returns all vertices that can be reached from a specific vertex
    def vertices_reachable_from(self, src):
        reachable_vertices = set()

        temp = self.al[src]

        while temp is not None:
            reachable_vertices.add(temp.item)
            temp = temp.next

        return reachable_vertices

    # Return all vertices that point to a specific vertex
    def get_vertices_that_point_to(self, dest):
        vertices = set()

        for i in range(len(self.al)):
            temp = self.al[i]

            while temp is not None:
                if temp.item == dest:
                    vertices.add(i)
                    break

                temp = temp.next

        return vertices

    # Return the number of vertices that point to a specific vertex
    def vertex_indegree(self, v):
        if not self.is_valid_vertex(v):
            return

        in_degree_count = 0

        for i in range(len(self.al)):
            temp = self.al[i]

            while temp is not None:
                if temp.item == v:
                    in_degree_count += 1
                    break

                temp = temp.next

        return in_degree_count

    # Return the indegree for every vertex in the graph
    def indegree_all_vertex(self):

        indegrees = []
        for i in range(len(self.al)):
            indegrees.append(self.vertex_indegree(i))

        return indegrees
