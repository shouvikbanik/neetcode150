# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    return_head=ListNode()
    return_head.next=head
    target_element_index = -1
    len_of_list = 0
    slow_ptr = return_head
    current_index = -1
    fast_ptr = head
    while slow_ptr:
        current_index += 1
        if target_element_index == -1:
            temp_n = 0
            while temp_n < n and fast_ptr:
                temp_n += 1
                fast_ptr = fast_ptr.next
            len_of_list+=temp_n
            if fast_ptr is None:
                target_element_index = len_of_list - (n - 1)
        else:
            target_element_index = len_of_list - (n - 1)
        if current_index == target_element_index - 1:
            slow_ptr.next = slow_ptr.next.next
            return return_head.next
        else:
            slow_ptr = slow_ptr.next
