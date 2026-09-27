# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self,head:Optional[ListNode])->Optional[ListNode]:
        current=head
        prev=None
        while current: 
            nxt=current.next
            current.next=prev
            prev=current
            current=nxt
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #reverse sum of two lists
        # reverse that sum into list
        h1=self.reverseList(l1)
        h2=self.reverseList(l2)

        sum1=0
        c1=h1
        while c1:
            sum1=sum1*10+c1.val
            c1=c1.next
            
        sum2=0
        c2=h2
        while c2:
            sum2=sum2*10+c2.val
            c2=c2.next

        total_sum=str(sum1+sum2)
        reversed_sum=total_sum[::-1]
        dummy=ListNode(0)

        prev=dummy
        for s in reversed_sum:
            temp=ListNode(int(s))
            prev.next=temp
            prev=temp
        return dummy.next

        

        