# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-sum-with-threshold-constraints
# source_path: LeetCode-Solutions-master/Python/maximum-total-sum-with-threshold-constraints.py
# solution_class: Solution
# submission_id: accdd3dc41a0b47666d99b77830fa3632b962e3b
# seed: 505540238

# Time:  O(n)
# Space: O(n)

# counting sort, greedy

class Solution(object):
    def maxSum(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: List[int]
        :rtype: int
        """
        groups = [[] for _ in xrange(len(nums))]
        for i, x in enumerate(threshold):
            groups[x-1].append(i)
        sorted_idxs = []
        for i, g in enumerate(groups):
            sorted_idxs.extend(g)
        result = 0
        for step, i in enumerate(sorted_idxs, 1):
            if step < threshold[i]:
                break
            result += nums[i]
        return result