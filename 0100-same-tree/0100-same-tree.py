# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def bfs(tree):
            result = []
            queue = [tree]

            while queue:
                node = queue.pop(0)
                if node:
                    result.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    result.append(None)
            return result

        tree1 = bfs(p)
        tree2 = bfs(q)

        return tree1 == tree2

            