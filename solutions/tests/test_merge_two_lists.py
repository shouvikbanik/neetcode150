from unittest import TestCase

from merge_two_lists import merge_two_lists


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Test(TestCase):
    def test_merge_two_lists(self):
        ll1 = self.create_linked_list([1, 2, 8])
        ll2 = self.create_linked_list([5, 9])
        return_value = merge_two_lists(ll1, ll2)
        return_list = self.create_list_from_ll(return_value)
        self.assertEqual([1, 2, 5, 8, 9], return_list)

    def create_list_from_ll(self, ll):
        return_list = []
        while (ll != None):
            return_list.append(ll.val)
            ll=ll.next
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
