# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def rearrangeLinkedList(head, k):
    #O(N)Time || O(1)Space
    small = LinkedList(0)
    large = LinkedList(0)
    smallHead = small
    largeHead = large
    equal = LinkedList(0)
    equalHead = equal
    curr = head    
    while curr:
        if curr.value == k:
            equal.next = curr
            equal = equal.next
        elif curr.value < k:
            small.next = curr
            small = small.next
        else:
            large.next = curr
            large = large.next
        curr = curr.next
    small.next = equalHead.next if equalHead.next else largeHead.next
    equal.next = largeHead.next if largeHead.next else None
    large.next = None
    return smallHead.next
