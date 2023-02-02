class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def zipLinkedList(head):
    if head.next is None:
        return head
    s ,f = head, head
    firstHead = head
    while f and f.next:
        s = s.next
        f = f.next.next
    head2 = s.next
    s.next = None
    #reverse the second half
    prev = None
    while head2:
        nxt = head2.next
        head2.next = prev
        prev = head2
        head2 = nxt
    return merge(firstHead, prev)

def merge(l1 , l2):
    firstHead = l1
    reverseLL2 = l2
    while reverseLL2 and firstHead:
        nxt1 = firstHead.next
        nxt2 = reverseLL2.next
        firstHead.next = reverseLL2
        reverseLL2.next = nxt1
        firstHead = nxt1
        reverseLL2 = nxt2
    return l1
