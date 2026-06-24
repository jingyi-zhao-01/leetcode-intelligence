# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-average-subtree
# source_path: LeetCode-Solutions-master/Python/maximum-average-subtree.py
# solution_class: Solution
# submission_id: aee0108fb151f0f9cd3ed62068521151336ec1eb
# seed: 1297057759

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        def maximumAverageSubtreeHelper(root, result):
            if not root:
                return [0.0, 0]
            s1, n1 = maximumAverageSubtreeHelper(root.left, result)
            s2, n2 = maximumAverageSubtreeHelper(root.right, result)
            s = s1+s2+root.val
            n = n1+n2+1
            result[0] = max(result[0], s / n)
            return [s, n]

        result = [0]
        maximumAverageSubtreeHelper(root, result)
        return result[0]