import sys
import itertools

NO_PATH = sys.maxsize

graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]

MAX_LENGTH = len(graph)


# Not part of the requirements of the assignment but added for better visual of result


def printSolution(dist):
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(MAX_LENGTH):
        for j in range(MAX_LENGTH):
            if (dist[i][j] == NO_PATH):
                print("%7s" % ("NO_PATH"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == MAX_LENGTH-1:
                print()

# Recursive version of the code


def floydNew():
    def shortestPath(i, j, k):
        length = MAX_LENGTH-1
        if k < length:
            shortestPath(i, j, k + 1)
        if i < length:
            shortestPath(i + 1, j, k)
        if j < length:
            shortestPath(i, j + 1, k)

        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    shortestPath(0, 0, 0)
    return printSolution(graph)


floydNew()
