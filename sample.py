# Import section
import sys
import itertools

# Defined the NO_PATH value by using the sys.maxsize
NO_PATH = sys.maxsize

# Defined the number of the vertices
V = 4

graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]


# Floyd Warshall Algorithm from the PDF file


def floyd(distance):
    MAX_LENGTH = len(distance)
    for intermediate, start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):

        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        distance[start_node][end_node] = min(
            distance[start_node][end_node], distance[start_node][intermediate] + distance[intermediate][end_node])

    print(distance)
    return distance

# Floyd Warshall Algorithm from the Geeksforgeeks website


def floydWarshall(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    printSolution(dist)


# A utility function to print the solution


def printSolution(dist):
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if (dist[i][j] == NO_PATH):
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == V-1:
                print()


if __name__ == "__main__":
    floyd(graph)
    floydWarshall(graph)
