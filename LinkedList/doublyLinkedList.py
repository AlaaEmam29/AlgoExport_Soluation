# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head == None and self.tail == None
    def setHead(self, node):
        isEmpty = self.isEmpty()
        if isEmpty:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head , node)
    def setTail(self, node):
        isEmpty = self.isEmpty()
        if isEmpty:
            self.setHead(node)
            return
        self.insertAfter(self.tail , node)
    

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        prevsNode = node.prev
        nodeToInsert.prev = prevsNode
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            prevsNode.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nxtNode = node.next
        nodeToInsert.prev = node
        nodeToInsert.next = nxtNode
        if node.next is None:
            self.tail = nodeToInsert
        else:
            nxtNode.prev = nodeToInsert
        
        node.next = nodeToInsert
        


    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position == 1:
            self.setHead(nodeToInsert)
            return
        currentPosition = 1
        currentNode = self.head
        while currentNode is not None and currentPosition != position:
            currentNode = currentNode.next
            currentPosition +=1
        if currentNode is not None:
            self.insertBefore(currentNode , nodeToInsert)
        else:
            self.setTail(nodeToInsert)
            

    def removeNodesWithValue(self, value):
        # Write your code here.
        node = self.head
        while node is not None:
            removedNode = node
            node = node.next
            if removedNode.value == value:
                self.remove(removedNode)

    def remove(self, node):
        # Write your code here.
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.helperRemove(node)
    def helperRemove(self , node):
        prevsNode = node.prev
        nxtNode = node.next
        if node.prev:
            prevsNode.next = nxtNode
        if node.next:
            nxtNode.prev = prevsNode
        node.prev = None
        node.next = None
        

    def containsNodeWithValue(self, value):
        # Write your code here.
        #O(n) time and O(1) space
        left = self.head
        right = self.tail
        while left != right:
            if left.value == value or right.value == value:
                return True
            left = left.next
            right = right.prev
        return False
