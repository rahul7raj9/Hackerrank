"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
counter=0
def has_cycle(head):
    global counter
    counter+=1
    first=head
    head_2=head
    while(head and head_2 and head.next):
            head=head.next
            head_2=head.next.next
            if head==head_2:
                return 1
                break
           
