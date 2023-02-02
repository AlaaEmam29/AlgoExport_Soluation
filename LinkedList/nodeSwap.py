# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#O(N)T | O(1)Space
def nodeSwap(head):
    dummy = LinkedList(0)
    dummy.next = head
    prev = dummy
    while prev.next and prev.next.next:
        f , s = prev.next , prev.next.next
        f.next = s.next
        s.next = f
        prev.next = s

        prev = f

    return dummy.next
