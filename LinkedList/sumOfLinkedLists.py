# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    #O(max(n ,m ))TS n-firstlinkedlist , m-secondlinkedlist
    carry = 0
    dummy = LinkedList(0)
    temp = dummy
    nodeOne = linkedListOne
    nodeTwo = linkedListTwo
    while nodeOne or nodeTwo or carry !=0:
        v1 = nodeOne.value if nodeOne is not None else 0
        v2 = nodeTwo.value if nodeTwo is not None else 0
        sums = ((v1 + v2) %10 )+carry
        carry =(v1 + v2) // 10
        temp.next = LinkedList(sums)
        temp = temp.next
        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None

    return dummy.next
        