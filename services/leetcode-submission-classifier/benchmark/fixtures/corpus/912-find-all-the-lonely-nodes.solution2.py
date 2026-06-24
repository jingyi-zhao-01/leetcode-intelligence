# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-all-the-lonely-nodes
# source_path: LeetCode-Solutions-master/Python/find-all-the-lonely-nodes.py
# solution_class: Solution2
# submission_id: 5365d49f91e85260a3ac4f1393564af554890538
# seed: 2494639687

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution2(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node, result):
            if not node:
                return
            if node.left and not node.right:
                result.append(node.left.val)
            elif node.right and not node.left:
                result.append(node.right.val)
            dfs(node.left, result)
            dfs(node.right, result)

        result = []
        dfs(root, result)
        return result