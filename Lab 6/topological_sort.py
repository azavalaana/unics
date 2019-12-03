from Queue import Queue
from graph_al import GraphAL


# Sorts vertices following the topological sort algorithm
def topological_sort(graph):

    all_in_degrees = graph.indegree_all_vertex()
    sort_result = []

    q = Queue()

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            q.enqueue(i)

    while not q.is_empty():
        u = q.dequeue()

        sort_result.append(u)

        for adj_vertex in graph.vertices_reachable_from(u):
            all_in_degrees[adj_vertex] -= 1

            if all_in_degrees[adj_vertex] == 0:
                q.enqueue(adj_vertex)

    if len(sort_result) != graph.num_vertices():
        return None

    return sort_result
