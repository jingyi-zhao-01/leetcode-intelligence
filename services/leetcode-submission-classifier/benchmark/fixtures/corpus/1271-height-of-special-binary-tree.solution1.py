# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: height-of-special-binary-tree
# source_path: LeetCode-Solutions-master/Python/height-of-special-binary-tree.py
# solution_class: Solution
# submission_id: d49470aab055a52c430b83e03866ba32383dea8e
# seed: 2393363065

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# dfs

class Solution(object):
    def heightOfTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        result = -1
        stk = [(root, 0)]
        while stk:
            u, d = stk.pop()
            result = max(result, d)
            if u.right and u.right.left != u:
                stk.append((u.right, d+1))
            if u.left and u.left.right != u:
                stk.append((u.left, d+1))
        return result