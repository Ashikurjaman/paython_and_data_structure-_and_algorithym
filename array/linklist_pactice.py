# class Node:
#     def __init__(self,data=None,next=None):
#         self.data = data
#         self.next = next
# class LinkList:
#     def __init__(self):
#         self.head = None
#     def insert_in_begining(self,data):  #insert data in begining
#         node = Node(data)
#         node.next=self.head
#         self.head = node
#     def display(self): #printing output
#         current=self.head
#         while current:
#             print(current.data,end='--->')
#             current =current.next
#         print("None")                   
#     def insert_in_end(self,data): #insert data in the end 
        
#         if self.head is None:
#             self.head=Node(data,None)
#             return
#         itr = self.head
#         while itr.next:
#             itr=itr.next
#         itr.next=Node(data,None)   
#     def insert_values(self,data_values): #insert data multiple values
#         self.head=None
#         for i in data_values:
#             self.insert_in_end(i)
#     def get_len(self): #get length
#         count = 0
#         itr = self.head
#         while itr:
#             count +=1
#             itr = itr.next
#         return count            



# myList = LinkList()
# # myList.insert_in_begining(4)
# # myList.insert_in_begining(3)
# # myList.insert_in_begining(2)
# # myList.insert_in_end(86)
# # myList.insert_in_end(87)
# # myList.insert_in_end(88)
# myList.insert_values(['apple','banana','orange'])
# # myList.get_len()
# myList.display()
# print(myList.get_len())




class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkList:
    def __init__(self):
        # Empty link list 
        self.head = None
        # no f nodes in the list
        self.n= 0
    def __len__(self):
        return self.n  
    def insert_head(self,value):
        #new node
        new_node = Node(value)
        # create connection
        new_node.next = self.head
        #reassign head
        self.head = new_node
        #length 
        self.n = self.n +1  
    

    # append 
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n = self.n +1
            return
        
        curr = self.head
        while curr.next !=None :
            curr = curr.next
       # you are in last node 
        curr.next = new_node
        self.n = self.n +1 

    # add node after a node
    def insert_in_middle(self,index,value):
        if index < 0 or index >= self.n: 
            return "Index out of bounds"
        new_node = Node(value) 
        curr =self.head
        while curr !=None:
            if curr.value == index:
                break
            curr=curr.next
        if curr != None:
            new_node.next=curr.next
            curr.next = new_node
            self.n = self.n +1 
        else:
           return "item not found"





    def __str__(self):
        result = ''
        curr = self.head
        while curr != None:
            result = result +str(curr.value) +' ---> '
            # print(curr.value,end=' -----> ')
            curr= curr.next
        return result[:-5]
    
L =LinkList()
# L.insert_head(5)
# L.insert_head(4)
# L.insert_head(3)
# L.insert_head(2)
L.append(1)
L.append(2)
L.append(3)
L.insert_in_middle(6,200)
# print(len(L))  
print(L)     






