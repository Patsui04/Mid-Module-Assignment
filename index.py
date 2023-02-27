# Import section
import sys

# Defined the Floyd Algorithm code based on the recursive method.
# Function receiving graph as parameter.
# Graph parameter needs to be a given edge-weighted directed graph.


def floydNew(graph):

    # Function to find the shortest path.
    # i = start node
    # j = end node
    # k = intermediate
    def shortestPath(i, j, k):

        # Defined the length of the parameter "graph".
        # Needed to subtract 1 from the len(graph).
        # because the function len() will count the 0 index as 1.
        length = len(graph)-1

        # Conditions phase to call the shortestPath function.
        # It will be calling shortestPath() until they
        # achieve the last vertice (defined by length variable)
        # by adding +1 in all the parameters.
        if k < length:
            shortestPath(i, j, k + 1)
        if i < length:
            shortestPath(i + 1, j, k)
        if j < length:
            shortestPath(i, j + 1, k)

        # Finding the minimum value between the start and end node
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # Calling the function shortestPath for the first time.
    # Declaring the start point where the function need to check by declaring i = 0, j = 0 and i = 0.
    shortestPath(0, 0, 0)

    # Print and return the final graph with the shortest path from the parameter "graph".
    print(graph)
    return graph


# Driver's code
if __name__ == "__main__":

    # Defined the NO_PATH variable
    # Define infinity as the large
    # enough value.
    NO_PATH = sys.maxsize

    # Defined the INPUT variable
    input = [[0, 7, NO_PATH, 8],
             [NO_PATH, 0, 5, NO_PATH],
             [NO_PATH, NO_PATH, 0, 2],
             [NO_PATH, NO_PATH, NO_PATH, 0]]

    # Function call
    floydNew(input)
