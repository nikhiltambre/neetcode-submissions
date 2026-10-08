# Definition for a binary tree node.
# class TreeNode:
from types import coroutine
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr=root
        parent=None
        ##searching for the node to remove
        while curr and curr.val!=key:
            parent=curr
            curr=curr.left if key<curr.val else curr.right
        ##Not found return root
        if not curr:
          return root
        ##found .....check if it has child nodes:
        if curr.left and curr.right:
           succ=curr.right
           succParent=curr
           while succ.left:
            succParent=succ
            succ=succ.left

           curr.val=succ.val
           if succParent==curr:
            succParent.right=succ.right
           else:
            succParent.left=succ.right
            
           return root
           
        ## can have left or right or both Null
        else:
            child = curr.left or curr.right
            if not parent:
                return child
            elif parent.left==curr:
                parent.left=child
            else:
                parent.right =child
             
        return root

        