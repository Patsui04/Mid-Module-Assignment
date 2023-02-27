from index import floydNew
from test_cases import (graph_1, output_1, graph_2,
                        output_2, graph_3)
from sample import floyd


import unittest


class Test_Code(unittest.TestCase):

    def test_floydNew_1(self):
        self.assertEqual(floydNew(graph_1), output_1)

    def test_floydNew_2(self):
        self.assertEqual(floydNew(graph_2), output_2)

    def test_floydNew_4(self):
        self.assertEqual(floydNew(graph_3), floyd(graph_3))


if __name__ == "__main__":
    unittest.main()
