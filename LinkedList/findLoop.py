# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
  
    #O(N) T || O(1)Space
    first , second = head.next , head.next.next
    while first != second:
        first = first.next 
        second =second.next.next
    first = head
    while second != first:
        second = second.next
        first = first.next
    return first
