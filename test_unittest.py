# import test cases and functions
from index import floydNew
from test_cases import (graph_1, graph_2, graph_3)
from sample import floyd

# import package
import unittest


class Test_Code(unittest.TestCase):
    # Checking if the outputs are the same
    # Compared with the author code and the PDF code

    # TEST CASE 1
    def test_floydNew_1(self):
        self.assertEqual(floydNew(graph_1), floyd(graph_1))

    # TEST CASE 2
    def test_floydNew_2(self):
        self.assertEqual(floydNew(graph_2), floyd(graph_2))

    # TEST CASE 3
    def test_floydNew_3(self):
        self.assertEqual(floydNew(graph_3), floyd(graph_3))


if __name__ == "__main__":
    unittest.main()
