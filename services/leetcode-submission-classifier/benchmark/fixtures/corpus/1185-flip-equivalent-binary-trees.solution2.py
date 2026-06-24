# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flip-equivalent-binary-trees
# source_path: LeetCode-Solutions-master/Python/flip-equivalent-binary-trees.py
# solution_class: Solution2
# submission_id: 3c0719b30113832b869babcf2079269f073eff7b
# seed: 3229956213

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

class Solution2(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        stk1, stk2 = [root1], [root2]
        while stk1 and stk2:
            node1, node2 = stk1.pop(), stk2.pop()
            if not node1 and not node2:
                continue 
            if not node1 or not node2 or node1.val != node2.val:
                return False
            if (not node1.left and not node2.right) or \
               (node1.left and node2.right and node1.left.val == node2.right.val):
                stk1.extend([node1.right, node1.left])
            else:
                stk1.extend([node1.left, node1.right])
            stk2.extend([node2.left, node2.right])
        return not stk1 and not stk2