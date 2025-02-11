# class ListNode():
#     def __init__(self,value=0,next=None):
#         self.value = value
#         self.next = next

# def array_to_linkList(arr):
#     if not arr:
#         return None
#     head = ListNode(arr[0])
#     current = head

#     for value in arr[1:]:
#         current.next = ListNode(value)
#         current = current.next

#     return head

# def reverseLinkList()

# def print_linkList(head):
#     current = head
#     while current:
#         print(current.value,end='------->')
#         current = current.next
#     print(None)    
# arr = [1,2,3,4,5,6,7]

# print_linkList(array_to_linkList(arr))        




class ListNode():
    def __init__(self,value=0,next=None):

        self.value = value
        self.next = next
class heading():
    def __init__(self):
        self.head = None    
        
    def array_to_linkList(self,arr):
        if not arr:
            return None
        self.head = ListNode(arr[0])
        current = self.head

        for value in arr[1:]:
            current.next = ListNode(value)
            current = current.next
        return self.head
    def reverse(self):
        prv_node = None
        curr_node = self.head
        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prv_node
            prv_node = curr_node
            curr_node = next_node
        self.head = prv_node
        return self.head    
    
    
    def printLinkList(self):
        current = self.head
        while current:
            print(current.value,end='--->')
            current = current.next
        print(None)


linkList = ListNode()
arr = [1,2,3,4,5,6,7]
link=linkList.array_to_linkList(arr)
rev = linkList.reverse()
linkList.printLinkList(rev)
        


