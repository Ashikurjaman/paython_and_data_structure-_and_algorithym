def detectCycle(head):
    slow,fast = head,head
    while fast and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False    

val=[3,2,0,-4]
print(detectCycle(val))