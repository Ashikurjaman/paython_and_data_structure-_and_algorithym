class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class stack:
    def __init__(self):
        self.top = None   
        self.count = 0         
    def isEmpty(self): #empty method
        return self.top == None
    def push(self,data): #push method
        new_node =  Node(data)
        new_node.next = self.top
        self.top = new_node 
        self.count +=1 
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
            self.count -= 1   
            return (data) 
    def size(self):
        return self.count    
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


def text_editor(text,pattern):
    u=stack()
    r=stack()

    for i in text:
        u.push(i)
    for i in pattern:
        if i =='u':
            data = u.pop()
            r.push(data)
        if i=='r':
            data = r.pop()
            u.push(data)
    res =''        
    while not u.isEmpty():
        res = u.pop() + res
    print(res) 
    #find the celebrity  
L =[[0,0,1,1],
    [0,0,1,1],
    [0,0,0,0],
    [0,0,1,1]]
def find_the_celebrity(L):
    s =stack()
    for i in range(len(L)):
        s.push(i)
    while s.size()>=2:
        i =s.pop()
        j =s.pop()
        if L[i][j] == 0:
            s.push(i) 
        else:
            s.push(j)
    celeb = s.pop()
    for i in range(len(L)):
        if  i != celeb:
            if L[i][celeb] == 0 or L[celeb][i]==1:
                print("no one is a celebrity")
    print("The celebrity is",celeb)            
    



text_editor('Bangladesh','uuurrr')
find_the_celebrity(L)
ll = stack()

ll.push(4)
ll.push(55)
ll.push(8)
# ll.traverse() 
ll.pop()
ll.pop()
ll.pop()
print(ll.size())
# print(ll.peek())
ll.traverse()
reverse('hello')

