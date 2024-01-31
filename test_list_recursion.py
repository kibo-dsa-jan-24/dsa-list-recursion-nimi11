import unittest
from list_recursion import ListRecursion

class TestListRecursion(unittest.TestCase):
    def test_reverse(self):
        val = ListRecursion.reverse(['The', 'quick', 'brown', 'fox'])
        assert val == ['fox', 'brown', 'quick', 'The']

    def test_remove_every_other(self):
        val = ListRecursion.remove_every_other(['The', 'quick', 'brown', 'fox'])
        assert val == ['The', 'brown']

    def test_maximum(self):
        val = ListRecursion.maximum([5, 10, 20, 99, 2, 3, 6])
        assert val == 99
