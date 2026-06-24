# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-nodes-equal-to-sum-of-descendants
# source_path: LeetCode-Solutions-master/Python/count-nodes-equal-to-sum-of-descendants.py
# solution_class: Solution2
# submission_id: cd4c3aa1e0f500352117f42a57c4bfdcbe080e65
# seed: 3582034632

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass

class Solution2(object):
    def equalToDescendants(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, result):
            if not node:
                return 0
            total = dfs(node.left, result) + dfs(node.right, result)
            if node.val == total:
                result[0] += 1
            return total+node.val

        result = [0]
        dfs(root, result)
        return result[0]