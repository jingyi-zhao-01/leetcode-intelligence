# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flip-equivalent-binary-trees
# source_path: LeetCode-Solutions-master/Python/flip-equivalent-binary-trees.py
# solution_class: Solution
# submission_id: dd9756fa37c6eeeea474a4920a3aa201869b9353
# seed: 1355301153

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


# bfs solution

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        dq1, dq2 = collections.deque([root1]), collections.deque([root2])
        while dq1 and dq2:
            node1, node2 = dq1.pop(), dq2.pop()
            if not node1 and not node2:
                continue 
            if not node1 or not node2 or node1.val != node2.val:
                return False
            if (not node1.left and not node2.right) or \
               (node1.left and node2.right and node1.left.val == node2.right.val):
                dq1.extend([node1.right, node1.left])
            else:
                dq1.extend([node1.left, node1.right])
            dq2.extend([node2.left, node2.right])
        return not dq1 and not dq2