class linkedlist:
    class __Node:
         def __init__(self,data):
            self.data = data  
            self.pre = None
            self.next = None

    def __init__(self,data):
        self.head = self.__Node(data)
        self.size = 1

    def insertAtBegin(self,data):
        new_node = self.__Node(data)
        self.head.pre = new_node
        new_node.next = self.head
        self.head = new_node
        self.size+=1
     
    def insertAtEnd(self,data):
        temp = self.head
        while(temp.next!=None):
            temp = temp.next
        new_node = self.__Node(data)
        new_node.pre = temp
        temp.next = new_node

    def insertAtPosition(self,data,position):
        temp = self.head
        new_node = self.__Node(data)
        for _ in range(position-1):
            temp = temp.next
        temp.pre.next = new_node
        new_node.pre = temp.pre
        new_node.next = temp
        temp.pre = new_node

    def printLL(self):
        temp = self.head
        while(temp!=None):
            print(temp.data)
            temp = temp.next

l1 = linkedlist(1)
l1.insertAtBegin(2)
l1.insertAtEnd(3)
l1.insertAtBegin(5)
l1.insertAtEnd(8)
l1.insertAtPosition(4,3)
l1.printLL()



