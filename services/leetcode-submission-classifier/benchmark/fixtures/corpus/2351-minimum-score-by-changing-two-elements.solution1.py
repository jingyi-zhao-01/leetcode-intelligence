# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-score-by-changing-two-elements
# source_path: LeetCode-Solutions-master/Python/minimum-score-by-changing-two-elements.py
# solution_class: Solution
# submission_id: 10c4d8b1824f2a193e247cf512bfc6f8f70f114d
# seed: 34933900

# Time:  O(nlogn)
# Space: O(1)

# sort, greedy

class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return min(nums[-3+i]-nums[i] for i in xrange(3))