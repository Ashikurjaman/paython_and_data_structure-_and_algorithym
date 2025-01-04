class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkList:
    def __init__(self):
        self.head = None
    def insert_in_begining(self,data):  #insert data in begining
        node = Node(data)
        node.next=self.head
        self.head = node
    def display(self): #printing output
        current=self.head
        while current:
            print(current.data,end='--->')
            current =current.next
        print("None")                   
    def insert_in_end(self,data): #insert data in the end 
        
        if self.head is None:
            self.head=Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)   
    def insert_values(self,data_values): #insert data multiple values
        self.head=None
        for i in data_values:
            self.insert_in_end(i)
    def get_len(self): #get length
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count            



myList = LinkList()
# myList.insert_in_begining(4)
# myList.insert_in_begining(3)
# myList.insert_in_begining(2)
# myList.insert_in_end(86)
# myList.insert_in_end(87)
# myList.insert_in_end(88)
myList.insert_values(['apple','banana','orange'])
# myList.get_len()
myList.display()
print(myList.get_len())