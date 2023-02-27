import sys
NO_PATH = sys.maxsize

# Test case 1 - Using the given from the assignment
graph_1 = [[0, 7, NO_PATH, 8],
           [NO_PATH, 0, 5, NO_PATH],
           [NO_PATH, NO_PATH, 0, 2],
           [NO_PATH, NO_PATH, NO_PATH, 0]]

output_1 = [[0, 7, 12, 8],
            [NO_PATH, 0, 5, 7],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]]

# # Test case 2 - Given that there are only 3 nodes
graph_2 = [[0, NO_PATH, 8],
           [NO_PATH, 0, NO_PATH],
           [NO_PATH, 2, 0]]

output_2 = [[0, 10, 8],
            [NO_PATH, 0, NO_PATH],
            [NO_PATH, 2, 0]]


# Test case 3 - Compairing the recursive function versus the given code solution
graph_3 = [[0, 7, NO_PATH, 8],
           [NO_PATH, 0, 5, NO_PATH],
           [NO_PATH, NO_PATH, 0, 2],
           [NO_PATH, NO_PATH, NO_PATH, 0]]
