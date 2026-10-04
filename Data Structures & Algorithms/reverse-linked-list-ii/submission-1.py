# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left>=right:
            return head
        # find left
        first = head
        cnt = 1
        prevFirst = None
        while cnt != left and first:
            prevFirst = first
            first = first.next
            cnt += 1
        # find right
        last = first
        while cnt != right and last.next:
            last = last.next
            cnt += 1
        nxtLast = last.next
        last = last.next

        # make reversed list
        prev = None
        tail = first
        while first != nxtLast:
            temp = first.next
            first.next = prev
            prev = first
            first = temp

        # reattach seperated reversed list
        tail.next = nxtLast
        if prevFirst:
            prevFirst.next = prev
            return head
        return prev
