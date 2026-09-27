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
        def dfs(temp):
           if not temp:
            return
           dfs(temp.left)        
           result.append(temp.val)
           dfs(temp.right)

        dfs(root) 
        return result