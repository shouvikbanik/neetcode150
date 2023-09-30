from unittest import TestCase

from reverse_linked_list import reverse_list


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Test(TestCase):
    def test_reverse_list(self):
        node1 = ListNode(10)
        node2 = ListNode(20)
        node3 = ListNode(30)
        node4 = ListNode(40)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        reversed_head = reverse_list(node1)
        self.assertEqual(reversed_head.val, 40)
        self.assertEqual(reversed_head.next.val, 30)
        self.assertEqual(reversed_head.next.next.val, 20)
        self.assertEqual(reversed_head.next.next.next.val, 10)
        self.assertEqual(reversed_head.next.next.next.next, None)
