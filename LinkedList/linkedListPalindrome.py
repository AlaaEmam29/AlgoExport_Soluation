# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    #O(N)TS
    stack = []
    tail = head 
    while tail:
        stack.append(tail.value)
        tail = tail.next
    while head:
        if head.value != stack.pop():
            return False
        head = head.next
    return True
