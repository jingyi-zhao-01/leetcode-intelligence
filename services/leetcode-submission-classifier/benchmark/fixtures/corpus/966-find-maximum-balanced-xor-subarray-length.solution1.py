# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-maximum-balanced-xor-subarray-length
# source_path: LeetCode-Solutions-master/Python/find-maximum-balanced-xor-subarray-length.py
# solution_class: Solution
# submission_id: eb92e55f6e84f7eb6a6d86e6fac3ff230dcb6d19
# seed: 2979853722

# Time:  O(n)
# Space: O(n)

# hash table, prefix sum

class Solution(object):
    def maxBalancedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = total = bal = 0
        lookup = collections.defaultdict(int)
        lookup[(total, bal)] = -1
        for i, x in enumerate(nums):
            total ^= x
            bal += (1 if x%2 else -1)
            if (total, bal) not in lookup:
                lookup[total, bal] = i
            else:
                result = max(result, i-lookup[total, bal])
        return result