class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        values = [str(node.val) for node in self]
        return '->'. join(values)

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next

    def insertNode(self, nodeValue, location):
        newNode = ListNode(nodeValue)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                currNode = self.head
                index = 0
                while index < location - 1:
                    currNode = currNode.next
                    index += 1
                nextNode = currNode.next
                currNode.next = newNode
                newNode.next = nextNode


if __name__ == "main":
    singlyLL = LinkedList()
    singlyLL.insertNode(10, 0)
    singlyLL.insertNode(20, 1)
    singlyLL.insertNode(30, 1)

    print(singlyLL)