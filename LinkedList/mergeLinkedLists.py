# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    # O(N + M)Time || O(1)Space.
    currOne , currTwo = headOne, headTwo
    dummy = LinkedList(0)
    temp = dummy
    while currOne and currTwo:
        if currOne.value < currTwo.value:
            temp.next = currOne
            currOne = currOne.next
        else:
            temp.next = currTwo
            currTwo = currTwo.next
        temp = temp.next
    if currOne :
        temp.next = currOne
    if currTwo:
        temp.next = currTwo
    return dummy.next