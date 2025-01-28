def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)  

arr=[100,15,18,170,19]
bubble_sort(arr)              


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None       
    def add(self,data):
        new_node = Node(data)
        new_node.next =self.head
        self.head = new_node
    def insert_in_last(self,data):
        if self.head == None:
            self.head =  Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
            
         
            
        
    def traverse(self):
        current = self.head
        while current:
            print(current.value,end='------>')
            current = current.next
        # print(current.data)
s = LinkList()    
s.add(25)
s.add(26)
s.insert_in_last(29)
s.traverse()
