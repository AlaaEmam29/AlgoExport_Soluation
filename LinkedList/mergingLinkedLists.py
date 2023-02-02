# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    # O(N + M)Time O(N)Space.
    hashMap = {}
    dummy = LinkedList(0)
    head = dummy
    l1 , l2 = linkedListOne, linkedListTwo
    while l1:
        hashMap[l1] =  True
        l1 = l1.next
    while l2:
        if l2 in hashMap:
            head.next = l2
            break
        l2 = l2.next
    return dummy.next