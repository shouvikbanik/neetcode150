class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    return_list = ListNode()
    temp = return_list
    while list1 != None and list2 != None:
        if list1.val < list2.val:
            temp.next = list1
            list1 = list1.next
            temp=temp.next
        else:
            temp.next = list2
            list2 = list2.next
            temp = temp.next
    if (list1 != None):
        temp.next = list1
    if (list2 != None):
        temp.next = list2
    return return_list.next
