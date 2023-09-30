def reverse_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    ptr1 = None
    ptr2 = head
    while ptr2 != None:
        ptr3 = ptr2.next
        ptr2.next = ptr1
        ptr1 = ptr2
        ptr2 = ptr3
    return ptr1
