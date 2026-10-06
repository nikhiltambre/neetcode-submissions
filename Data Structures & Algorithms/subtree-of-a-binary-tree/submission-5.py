# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def subtree(r: Optional[TreeNode]) -> str:
            if not r:
                return ",#"
            stack = [r]
            result = []
            while stack:
                curr = stack.pop()
                if not curr:
                    result.append(",#")
                else:
                    result.append(f",{curr.val}")
                    stack.append(curr.right)
                    stack.append(curr.left)
            return "".join(result)

        r1 = subtree(root)
        r2 = subtree(subRoot)
        return r2 in r1
