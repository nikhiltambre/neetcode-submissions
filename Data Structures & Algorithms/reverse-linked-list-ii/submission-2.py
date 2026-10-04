# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ## using for loops(for better syntax)
        ## go till left
        dummy=ListNode(0,head)
        first = head
        prevFirst = dummy
        for _ in range(left-1):
            prevFirst = first
            first = first.next
        ##go right reversing nodes
        prev=None
        for _ in range(right-left+1):
            temp=first.next
            first.next=prev
            prev,first=first,temp
        prevFirst.next.next=first
        prevFirst.next=prev
        return dummy.next