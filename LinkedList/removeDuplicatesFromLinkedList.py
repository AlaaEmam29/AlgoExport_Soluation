# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currNode = linkedList
    while currNode:
        nxtNode = currNode.next
        while nxtNode and currNode.value == nxtNode.value :
            nxtNode = nxtNode.next
        currNode.next=nxtNode
        currNode = nxtNode
    return linkedList
    