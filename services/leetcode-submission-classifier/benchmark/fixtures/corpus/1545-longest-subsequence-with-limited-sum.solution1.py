# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-subsequence-with-limited-sum
# source_path: LeetCode-Solutions-master/Python/longest-subsequence-with-limited-sum.py
# solution_class: Solution
# submission_id: 1d2ff47082e6fc771a2c9d6388bb9fafca6ee95a
# seed: 3867617156

# Time:  O(nlogn + qlogn)
# Space: O(1)

import bisect


# greedy, sort, binary search

class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        for i in xrange(len(nums)-1):
            nums[i+1] += nums[i]
        return [bisect.bisect_right(nums, q) for q in queries]