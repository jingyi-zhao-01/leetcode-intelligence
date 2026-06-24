# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-sum-bst-in-binary-tree
# source_path: LeetCode-Solutions-master/Python/maximum-sum-bst-in-binary-tree.py
# solution_class: Solution
# submission_id: 3dcca0796f88cc5dd3f160ad04fe4e042b707f53
# seed: 214305134

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# dfs solution with stack

class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        stk = [[root, None, []]]
        while stk:
            node, tmp, ret = stk.pop()
            if tmp:
                lvalid, lsum, lmin, lmax = tmp[0]
                rvalid, rsum, rmin, rmax = tmp[1]
                if lvalid and rvalid and lmax < node.val < rmin:
                    total = lsum + node.val + rsum
                    result = max(result, total)
                    ret[:] = [True, total, min(lmin, node.val), max(node.val, rmax)]
                    continue
                ret[:] = [False, 0, 0, 0]
                continue
            if not node:
                ret[:] = [True, 0, float("inf"), float("-inf")]
                continue
            new_tmp = [[], []]
            stk.append([node, new_tmp, ret])
            stk.append([node.right, None, new_tmp[1]])
            stk.append([node.left, None, new_tmp[0]])
        return result