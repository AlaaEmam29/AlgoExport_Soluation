# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    dummy = LinkedList(0)
    dummy.next = head
    first = dummy
    second = head
  
    while k > 0 and second:
        second = second.next
        k -=1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return 
    while second:
        second = second.next
        first = first.next
    first.next = first.next.next
    return dummy.next
