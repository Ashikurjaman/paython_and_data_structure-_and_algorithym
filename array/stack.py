class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class stack:
    def __init__(self):
        self.top = None            
    def isEmpty(self): #empty method
        return self.top == None
    def push(self,data): #push method
        new_node =  Node(data)
        new_node.next = self.top
        self.top = new_node  
    def peek(self):
        if(self.isEmpty()):
            return "stack is Empty"
        else:
            return self.top.val
    def pop(self):
        if(self.isEmpty()):
            return "empty"
        else:
            data =self.top.val
            self.top = self.top.next   
            return data 
    def traverse(self): #print method
        temp= self.top
        while temp != None:
            print(temp.val,end='---->')
            temp = temp.next

def reverse(data):
    s=stack()
    for i in data:
        s.push(i)
    res=''
    while not s.isEmpty():
        res = res + s.pop()    
    print(res)

ll = stack()

ll.push(4)
ll.push(55)
ll.push(8)
# ll.traverse() 
ll.pop()
ll.pop()
ll.pop()
# print(ll.peek())
ll.traverse()
reverse('hello')

