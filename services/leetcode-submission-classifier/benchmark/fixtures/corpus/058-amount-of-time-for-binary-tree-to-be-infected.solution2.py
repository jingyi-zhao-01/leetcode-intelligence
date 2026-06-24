# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: amount-of-time-for-binary-tree-to-be-infected
# source_path: LeetCode-Solutions-master/Python/amount-of-time-for-binary-tree-to-be-infected.py
# solution_class: Solution2
# submission_id: 2b930ff01756cf8f59a520689de8646325b5773e
# seed: 2512656997

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# iterative dfs, tree dp

class Solution2(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        def dfs(curr, start, result):
            if curr is None:
                return [-1, -1]
            left = dfs(curr.left, start, result)
            right = dfs(curr.right, start, result)
            d = -1
            if curr.val == start:
                d = 0
                result[0] = max(left[0], right[0])+1
            elif left[1] >= 0:
                d = left[1]+1
                result[0] = max(result[0], right[0]+1+d)
            elif right[1] >= 0:
                d = right[1]+1
                result[0] = max(result[0], left[0]+1+d)
            return [max(left[0], right[0])+1, d]  # [height, dist_to_start]

        result = [-1]
        dfs(root, start, result)
        return result[0]