# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    #O(N) Time | O(1) Space
    curr = head
    prevs = None
    while curr:
        nxt = curr.next
        curr.next = prevs
        prevs = curr
        curr = nxt
    return prevs
