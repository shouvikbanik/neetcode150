def has_cycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    slow_ptr, fast_ptr = head, head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            return True
    return False
