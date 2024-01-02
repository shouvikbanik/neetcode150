from unittest import TestCase

from add_two_nums import add_two_numbers, ListNode


class Test(TestCase):
    def test_add_two_numbers(self):
        self.assertEqual([8, 9, 9, 9, 0, 0, 0, 1],
                         self.create_list_from_ll(add_two_numbers(self.create_linked_list([9, 9, 9, 9, 9, 9, 9]),
                                                                  self.create_linked_list([9, 9, 9, 9]))))

    def create_linked_list(self, elements):
        head = ListNode()
        temp = head
        for element in elements:
            node = ListNode(element)
            node.next = None
            temp.next = node
            temp = node
        return head.next

    def create_list_from_ll(self, ll):
        return_list = []
        while (ll != None):
            return_list.append(ll.val)
            ll = ll.next
        return return_list
