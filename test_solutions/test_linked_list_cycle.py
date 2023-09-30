from unittest import TestCase

from linked_list_cycle import has_cycle


class ListNode(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None


class Test(TestCase):
    def test_has_cycle_positive(self):
        ll = self.create_linked_list([10, 20, 30, 40], True)
        self.assertEqual(True, has_cycle(ll))

    def test_has_cycle_negative(self):
        ll = self.create_linked_list([10, 20, 30, 40], False)
        self.assertEqual(False, has_cycle(ll))

    def create_linked_list(self, elements, is_cyclic):
        head = ListNode()
        temp = head
        for element in elements:
            node = ListNode(element)
            if is_cyclic == True:
                node.next = head.next
            temp.next = node
            temp = node
        return head.next
