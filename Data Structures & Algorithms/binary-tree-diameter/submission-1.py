# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        stack = deque()
        heights = {None: 0}
        stack.append(root)
        while stack:
            node = stack[-1]
            if node.left and node.left not in heights:
                stack.append(node.left)
            elif node.right and node.right not in heights:
                stack.append(node.right)

            else:
                stack.pop()
                lh = heights[node.left]
                rh = heights[node.right]

                res = max(res, lh + rh)

                heights[node] = 1 + max(lh, rh)

        return res
