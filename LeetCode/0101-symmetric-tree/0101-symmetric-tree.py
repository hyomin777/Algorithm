# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_symmetric(tree1, tree2):
            queue1 = [tree1]
            queue2 = [tree2]

            while queue1 and queue2:
                node1 = queue1.pop(0)
                node2 = queue2.pop(0)

                if (node1 is None) != (node2 is None):
                    return False

                if node1 is None and node2 is None:
                    continue

                if node1.val != node2.val:
                    return False

                queue1.append(node1.left)
                queue2.append(node2.right)
                queue1.append(node1.right)
                queue2.append(node2.left)

            return len(queue1) == len(queue2)

        return check_symmetric(root.left, root.right)