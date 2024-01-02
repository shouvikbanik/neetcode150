class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    sum_ll = ListNode()
    carry = 0
    ptr = sum_ll
    while l1 or l2:
        new_node = ListNode()
        ptr.next = new_node
        ptr = ptr.next
        if l1 and l2:
            ptr.val = (l1.val + l2.val + carry) % 10
            carry = 1 if (l1.val + l2.val + carry) > 9 else 0
            l1 = l1.next
            l2 = l2.next
        elif l1 == None and l2:
            ptr.val = (l2.val + carry) % 10
            carry = 1 if (carry + l2.val) > 9 else 0
            l2 = l2.next
        else:
            ptr.val = (l1.val + carry) % 10
            carry = 1 if (carry + l1.val) > 9 else 0
            l1 = l1.next
    if carry == 1:
        ptr.next = ListNode()
        ptr = ptr.next
        ptr.val = carry
    return sum_ll.next
