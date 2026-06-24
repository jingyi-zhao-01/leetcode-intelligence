# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: path-sum-iii
# source_path: LeetCode-Solutions-master/Python/path-sum-iii.py
# solution_class: Solution
# submission_id: 099304f1a6041c1997263179b130173e96707420
# seed: 2490476132

# Time:  O(n)
# Space: O(h)

import collections

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def pathSumHelper(root, curr, sum, lookup):
            if root is None:
                return 0
            curr += root.val
            result = lookup[curr-sum] if curr-sum in lookup else 0
            lookup[curr] += 1
            result += pathSumHelper(root.left, curr, sum, lookup) + \
                      pathSumHelper(root.right, curr, sum, lookup)
            lookup[curr] -= 1
            if lookup[curr] == 0:
                del lookup[curr]
            return result

        lookup = collections.defaultdict(int)
        lookup[0] = 1
        return pathSumHelper(root, 0, sum, lookup)