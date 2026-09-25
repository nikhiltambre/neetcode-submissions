# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # find middle
        slow=head 
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        ##slow is the middle:
        second=slow.next
        slow.next=None

        # reverse from middle(slow ) -> tail
        prev=None
        current=second
        while current:
            nxt=current.next
            current.next=prev
            prev=current
            current=nxt
        
        current=head
        second=prev
        while second:
            nxtC=current.next
            nxtS=second.next
            current.next=second
            second.next=nxtC
            current=nxtC
            second=nxtS