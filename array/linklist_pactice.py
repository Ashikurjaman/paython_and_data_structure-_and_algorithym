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
            print("Index out of bounds")
        new_node = Node(value) 
        curr =self.head
        for _ in range(0,index - 1): #set node using index
            curr = curr.next
        # while curr !=None:
        #     if curr.self.n == index:
        #         break
        #     curr=curr.next
        if curr != None:
            new_node.next=curr.next
            curr.next = new_node
            self.n = self.n +1 
        else:
           print("item not found")

    def clear(self):
        self.head =None
        self.n=0

    #delete first value
    def delete_head(self):
        if self.head == None:
            return "Empty list"
        self.head = self.head.next
        self.n -=1

    def pop(self): #delete last item
        if self.head == None:
           return "empty list"
        curr = self.head
        if curr.next == None:
            return self.delete_head()
            
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n -=1  


    # Delete by value     
    def remove(self,value):
        curr = self.head
        if curr == None:
            return "empty list"
        if curr.value == value:
            return self.delete_head()
        while curr.next != None:
            if curr.next.value == value:
                    break
            curr=curr.next
        if curr.next == None:
            return "item not found"
        else:
            curr.next = curr.next.next
            self.n -=1    

    # search by value
    def search(self,item):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.value == item:
                return pos
            curr = curr.next
            pos +=1
        return "not found"
    def __getitem__(self,index): # get item value by index number
        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.value
            curr = curr.next
            pos +=1   
        return 'indexError'  
    def replace_max(self,value):
        temp =self.head
        max = temp
        while temp != None:
            print(f"Current node value: {temp.value}")
            if temp.value > max.value:
                max = temp
                print(f"New max found: {max.value}")
            temp = temp.next
            print(f"Replacing max value {max.value} with {value}")
        max.value = value



        # problem solving        
    def sum_odd_num(self):
        temp = self.head
        count =0
        result= 0
        while temp != None:
            if count % 2 != 0:
                result = result + temp.value
            temp = temp.next
            count +=1
        print(result)        
    def reverse(self):
        prv_node =None
        curr_node = self.head #2


        # while curr_node != None:
        #     next_node = curr_node.next #3 4 none
        #     curr_node.next = prv_node #none 2 3
        #     prv_node = curr_node #2 3 4
        #     curr_node = next_node #3 4 none
        # self.head = prv_node 
        # return self.head  
        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prv_node
            prv_node = curr_node
            curr_node = next_node 
        self.head = prv_node  
        return self.head
    # string

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
L.insert_head(4)
L.insert_head(3)
L.insert_head(2)
# L.append(55)
# L.append(100)
# L.append(19)
# # L.pop() 
# L.pop() 
# L.pop()  
# L.pop() 
# L.remove(3) 
# L.remove(1) 

L.insert_in_middle(3,200)
# L.insert_in_middle(2,100)
# L.replace_max(2)
# print(L.search(200))
L.reverse()
print(L)
# L.sum_odd_num()

# print(len(L))  
  
# print(L[15])   



  


