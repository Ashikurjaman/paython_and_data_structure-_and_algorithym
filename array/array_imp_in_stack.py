class Stack:
    def __init__(self,size):
        self.size = size
        self._stack = [None] * self.size
        self.top = -1

    def push(self,val):
        if self.top == self.size -1:
            return "overflow"
        else:
            self.top +=1
            self._stack[self.top]=val

    def pop(self):
        if self.top == -1:
            return "stack empty"
        else:
            data = self._stack[self.top]
            self.top-=1
            print(data) 
    def traverse(self):
         for i in range(self.top +1):
             print(self._stack[i],end=' ')              
s=Stack(3)
s.push(5)    
s.push(6)    
s.push(9) 
  
s.pop()   
s.pop()   
s.pop()   
    
s.traverse()
# print(s.stack)