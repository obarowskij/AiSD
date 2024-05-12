import unittest
from ..functions.is_connected import is_connected

class TestIsConnected(unittest.TestCase):
    def test_connected_graph(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F'],
            'F': ['C', 'E'],
        }
        self.assertTrue(is_connected(graph))

    def test_disconnected_graph(self):
        graph = {
            'A': ['B'],
            'B': ['A'],
            'C': ['D'],
            'D': ['C'],
        }
        self.assertFalse(is_connected(graph))

    def test_empty_graph(self):
        graph = {}
        self.assertFalse(is_connected(graph))

    def test_single_vertex_graph(self):
        graph = {
            'A': [],
        }
        self.assertTrue(is_connected(graph))

    def test_two_disconnected_vertices_graph(self):
        graph = {
            'A': [],
            'B': [],
        }
        self.assertFalse(is_connected(graph))

if __name__ == "__main__":
    unittest.main()