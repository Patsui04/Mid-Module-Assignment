import cProfile

# Importing functions that will be use the performance tests
from index import floydNew
from sample import floyd

# Importing test cases for the performance tests
from test_cases import (graph_1, graph_2, graph_3)

# Function to test the performance of the index file (author code)


def testAuthorCode(data):
    # Testing scability by creating a loop with a range of 50
    for a in range(50):
        floydNew(data)

# Function to test the performance of the sample file (PDF code)


def testPDFCode(data):
    # Testing scability by creating a loop with a range of 50
    for a in range(50):
        floyd(data)


if __name__ == "__main__":
    # Please remember to delete the "#" to run the test

    # TEST CASE 1:
    # Performance test of the author's code
    cProfile.run('testAuthorCode(graph_1)')

    # Performance test of the sample code
    # cProfile.run('testPDFCode(graph_1)')

    # TEST CASE 2:
    # Performance test of the author's code
    # cProfile.run('testAuthorCode(graph_2)')

    # Performance test of the sample code
    # cProfile.run('testPDFCode(graph_2)')

    # TEST CASE 3:
    # Performance test of the author's code
    # cProfile.run('testAuthorCode(graph_3)')

    # Performance test of the sample code
    # cProfile.run('testPDFCode(graph_3)')
