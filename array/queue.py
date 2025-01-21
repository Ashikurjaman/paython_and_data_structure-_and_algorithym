class Node:
    def __init__(self,value):
        self.data=value;
        self.next = None 
class Queue:
    def __init__(self):
        self.front=None
        self.rare =None

    def enqueue(self,value):
        new_node = Node(value)
        if  self.rare ==None:
            self.front = new_node
            self.rare = self.front
        else:
            self.rare.next = new_node
            self.rare = new_node  
    def dequeue(self):
        if self.front == None:
            return"Empty"
        else:
            self.front = self.front.next
    def is_empty(self):
        return self.front == None    
    def front_item(self):
        if self.front == None:
            return "Empty"
        else:
            return self.front.data 
    def rear_item(self):
        if self.front == None:
            return "Empty"
        else:
            return self.rare.data

    def traverse(self):
        temp = self.front
        while temp !=None:
            print(temp.data,end='--->') 
            temp=temp.next                


q = Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.dequeue()
q.dequeue()
# q.dequeue() 
print(q.is_empty())

q.traverse()

