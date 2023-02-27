import sys
import itertools

NO_PATH = sys.maxsize

graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]


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


floyd(graph)
