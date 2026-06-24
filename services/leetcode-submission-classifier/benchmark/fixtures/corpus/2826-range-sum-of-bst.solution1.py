# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: range-sum-of-bst
# source_path: LeetCode-Solutions-master/Python/range-sum-of-bst.py
# solution_class: Solution
# submission_id: 7bac243bdff08ed8cb0f4cbf9a9ac83f7b25f3ac
# seed: 1455298767

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        result = 0
        s = [root]
        while s:
            node = s.pop()
            if node:
                if L <= node.val <= R:
                    result += node.val
                if L < node.val:
                    s.append(node.left)
                if node.val < R:
                    s.append(node.right)
        return result