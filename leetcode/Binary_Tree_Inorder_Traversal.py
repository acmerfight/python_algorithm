# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        result = []
        stack = []
        if root is None:
            return []
        while (root is not None or stack):
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                result.append(node.val)
                root = node.right
        return result
