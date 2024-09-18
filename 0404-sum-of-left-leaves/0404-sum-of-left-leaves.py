# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        result = 0

        while queue:
            node = queue.popleft()

            if node.left:
                left_node = node.left
                queue.append(left_node)

                if not left_node.left and not left_node.right:
                    result += left_node.val

            if node.right:
                queue.append(node.right)

        return result