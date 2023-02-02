# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
def shiftLinkedList(head, k):
    #O(N) Time |O(1) Space
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length +=1
    offset = abs(k) % length
    if offset == 0:
        return head
    put = length - offset if k > 0 else offset
    newTail = head
    for _ in range(1 , put):
        newTail = newTail.next
    newHead = newTail.next
    newTail.next = None
    tail.next= head
    return newHead