from unittest import TestCase

from minstack import MinStack


class TestMinStack(TestCase):
    def test_push(self):
        obj = MinStack()
        obj.push(10)
        self.assertEqual([10], obj.stack_of_values)

    def test_pop(self):
        obj = MinStack()
        obj.push(10)
        self.assertEqual(10, obj.pop())

    def test_top(self):
        obj = MinStack()
        obj.push(10)
        obj.push(20)
        self.assertEqual(20, obj.top())

    def test_get_min(self):
        obj = MinStack()
        obj.push(10)
        obj.push(20)
        self.assertEqual(10, obj.get_min())
