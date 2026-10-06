# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def subtree(node: Optional[TreeNode]) -> str:
            if not node:
                return ",#"
            return f"{node.val}"+subtree(node.right)+subtree(node.left)
        r1 = subtree(root)
        r2 = subtree(subRoot)
        return r2 in r1
