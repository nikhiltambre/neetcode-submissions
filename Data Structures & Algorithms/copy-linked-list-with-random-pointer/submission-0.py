"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # adding nodes in between
        if not head: 
            return None
        dummy=Node(0,head)
        current=dummy.next
        while current:
            temp=Node(current.val,current.next)
            current.next=temp
            current=temp.next
        
        # connecting random 
        current=dummy.next
        while current:
            if current.random:
                current.next.random=current.random.next
            current=current.next.next
        copy_head=dummy.next.next
        # connecting next 
        prev=dummy.next
        curr=dummy.next.next
        while prev:
            nxt=curr.next
            prev.next=nxt
            curr.next=nxt.next if nxt else None
            prev=nxt
            curr=curr.next
        return copy_head
        