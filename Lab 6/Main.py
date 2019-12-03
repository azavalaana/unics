from graph_al import GraphAL
from topological_sort import topological_sort
from Kruskals_Algorithm import Generic_Graph


# Test cases for kruskal's and topological sorting
def main():
    print("\nTest Case for:")
    print("Kruskal's Algorithm")
    print("************************")

    # Regular graph with Disjointed Set Forest methods in the class
    graph_k = Generic_Graph([0, 1], 5)
    graph_k.add([0, 2], 4)
    graph_k.add([0, 4], 7)
    graph_k.add([1, 6], 3)
    graph_k.add([1, 7], 3)
    graph_k.add([2, 3], 2)
    graph_k.add([2, 5], 1)
    graph_k.add([3, 4], 2)
    graph_k.add([4, 5], 1)

    print("All edges with weights:")
    # method that prints all edges and their respective weights
    graph_k.print_graph()

    print("\nEdges in Minimum Spanning Tree:")
    # Method that prints the edges selected for the Minimum Spanning Tree
    graph_k.kruskal_alg()
    print()

    print("Test Case for:")
    print("Topological Sort")
    print("************************")
    # This initializes an Adjacency List Graph
    graph_t = GraphAL(8, True)

    graph_t.insert_edge(0, 1)
    graph_t.insert_edge(1, 6)
    graph_t.insert_edge(1, 2)
    graph_t.insert_edge(3, 5)
    graph_t.insert_edge(3, 4)
    graph_t.insert_edge(2, 5)
    graph_t.insert_edge(2, 3)
    graph_t.insert_edge(6, 7)
    graph_t.insert_edge(7, 5)

    # This prints all vertices in the graph
    print("Original vertices arrangement:")
    for i in range(len(graph_t.al)):
        print(i, sep=' ', end='', flush=True)
        print(" ", sep=' ', end=' ', flush=True)

    # This uses topological sort to sort the vertices
    top_sort = topological_sort(graph_t)
    # This prints sorted vertices
    print("\nTopological Sorted Vertices: ")
    for j in top_sort:
        print(j, sep=' ', end='', flush=True)
        print(" ", sep=' ', end=' ', flush=True)


main()
