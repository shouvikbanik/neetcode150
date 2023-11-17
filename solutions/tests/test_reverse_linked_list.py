from unittest import TestCase

from reverse_linked_list import reverse_list


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Test(TestCase):
    def test_reverse_list(self):
        ll = self.create_linked_list([10, 20, 30, 40])
        reversed_head = reverse_list(ll)
        reversed_head_list = self.create_list_from_ll(reversed_head)
        self.assertEqual([40, 30, 20, 10], reversed_head_list)

    def create_list_from_ll(self, ll):
        return_list = []
        while (ll != None):
            return_list.append(ll.val)
            ll = ll.next
        return return_list

    def create_linked_list(self, elements):
        head = ListNode()
        temp = head
        for element in elements:
            node = ListNode(element)
            node.next = None
            temp.next = node
            temp = node
        return head.next
