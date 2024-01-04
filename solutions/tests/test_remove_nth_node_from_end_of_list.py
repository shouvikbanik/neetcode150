from unittest import TestCase

from remove_nth_node_from_end_of_list import ListNode, remove_nth_from_end


class Test(TestCase):
    def test_remove_nth_from_end(self):
        self.assertEqual([1, 2, 3, 5],
                         self.create_list_from_ll(remove_nth_from_end(self.create_linked_list([1, 2, 3, 4, 5]), 2)))

    @staticmethod
    def create_linked_list(elements):
        head = ListNode()
        temp = head
        for element in elements:
            node = ListNode(element)
            node.next = None
            temp.next = node
            temp = node
        return head.next

    @staticmethod
    def create_list_from_ll(ll):
        return_list = []
        while ll is not None:
            return_list.append(ll.val)
            ll = ll.next
        return return_list
