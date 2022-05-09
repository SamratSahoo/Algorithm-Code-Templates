# Detect cycle in Linked List: Turtoise and Hare Algorithm
def fast_and_slow_pointer(head):
    # Null Case
    if not head:
        return False 
    
    # Instantiate two nodes, one that goes fast, one that goes slow
    slow = head
    fast = head

    # Check if fast.next is not Null and fast.next.next is not null
    while fast.next and fast.next.next:
        
        # Slow pointer will go one forward
        slow = slow.next

        # Fast pointer will go two forward
        fast = fast.next.next

        # If slow and fast are equal
        if slow == fast:

            # There is a loop in the linked list
            return True

    # Else there is not a loop in the linked list
    return False