from pydantic import validate_call

class Buffer:
    @validate_call
    def __init__(self,device_num : int,block_num : int,data=None):
        self.data = data  
        self.pre = None
        self.next = None
        self.device_num = device_num
        self.block_num = block_num
        self.status = "Free"

class LinkedList(Buffer):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    @property
    def isEmpty(self):
        if self.size == 0:
            return True
        return False
    
    @validate_call
    def append(self,device_num : int,block_num : int,data=None):
        new_node = Buffer(device_num,block_num,data)
        if self.isEmpty:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.pre = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size+=1
        new_node.status = "Busy"
        print("Changed status from Free to Busy")
     
    @validate_call
    def search_append(self,device_num : int,block_num : int,data=None):
        # search block in the LL
        temp = self.head
        while (temp != None):
            if temp.device_num == device_num and temp.block_num == block_num:
                print("Buffer found")
                print(f"Status: {temp.status}, Block num: {temp.block_num}, Device num: {temp.device_num}, Data: {temp.data}")
                return temp
            else:
                temp = temp.next
        self.append(device_num,block_num,data)
        print("New buffer added")
        return self.tail
    
    @property
    def printLL(self):
        temp = self.head
        i = 1
        if self.isEmpty:
            print("Empty hash queue")
        while(temp != None):
            print(f"Buffer num {i}, Block num: {temp.block_num}, Device num: {temp.device_num}, Data: {temp.data}")
            temp = temp.next
            i += 1 
        
class HashQueue(LinkedList):
    def __init__(self):
        self.hash_queue0 = LinkedList()
        self.hash_queue1 = LinkedList()
        self.hash_queue2 = LinkedList()

    def hash_func(self,device_num : int,block_num : int):
        return (device_num+block_num)%3
    
    @validate_call
    def getblk(self,device_num : int,block_num : int ,data=None):
        hash = self.hash_func(device_num,block_num)
        if hash == 0:
            print("quene no ",0)
            bqueue0 = self.hash_queue0.search_append(device_num,block_num,data)
        elif hash == 1:
            print("quene no ",1)
            bqueue1 = self.hash_queue1.search_append(device_num,block_num,data)
        elif hash == 2:
            print("quene no ",2)
            bqueue2 = self.hash_queue2.search_append(device_num,block_num,data)
        print()

    @property
    def printAll(self):
        print(f"Queue no.: {0}")
        self.hash_queue0.printLL
        print()
        print(f"Queue no.: {1}")
        self.hash_queue1.printLL
        print()
        print(f"Queue no.: {2}")
        self.hash_queue2.printLL
        print()





hq1 = HashQueue()

hq1.getblk(1,1,3)
hq1.getblk(7,2,555)
hq1.getblk(8,2,555)
hq1.getblk(7,2,555)
hq1.getblk(1,1,3)
hq1.getblk(8,9,555)
hq1.printAll


