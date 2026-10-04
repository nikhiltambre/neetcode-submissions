# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # level wise traversal
        if not root :
            return None
        stack = deque()
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.left and node.right:
             node.right, node.left = node.left, node.right
             stack.append(node.left)
             stack.append(node.right)
            else:
             if node.left:
                node.right=node.left
                node.left=None
                stack.append(node.right)
             elif node.right:
                node.left=node.right
                node.right=None
                stack.append(node.left)
        return root
