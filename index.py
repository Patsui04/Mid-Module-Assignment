import sys
NO_PATH = sys.maxsize

input = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]

# Recursive version of the code


def floydNew(graph):
    def shortestPath(i, j, k):
        length = len(graph)-1
        if k < length:
            shortestPath(i, j, k + 1)
        if i < length:
            shortestPath(i + 1, j, k)
        if j < length:
            shortestPath(i, j + 1, k)

        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    shortestPath(0, 0, 0)
    print(graph)
    return graph


floydNew(input)
