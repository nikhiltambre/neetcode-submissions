# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive solution
        result=[]
        current=root
        stack=deque()
        while current or stack:
            while current:
                stack.append(current)
                current=current.left
            current=stack.pop()
            result.append(current.val)
            current=current.right

        return result