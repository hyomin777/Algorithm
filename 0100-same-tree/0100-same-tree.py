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
                current = queue.pop(0)

                if current:
                    result.append(current.val)

                    if current.left:
                        left = current.left
                        queue.append(left)
                    else:
                        queue.append(None)

                    if current.right:
                        right = current.right
                        queue.append(right)
                    else:
                        queue.append(None)
                else:
                    result.append(None)

            return result

        tree1 = bfs(p)
        tree2 = bfs(q)

        return tree1 == tree2

            