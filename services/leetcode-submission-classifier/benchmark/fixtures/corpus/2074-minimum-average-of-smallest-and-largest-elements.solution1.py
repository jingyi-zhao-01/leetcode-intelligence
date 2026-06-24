# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-average-of-smallest-and-largest-elements
# source_path: LeetCode-Solutions-master/Python/minimum-average-of-smallest-and-largest-elements.py
# solution_class: Solution
# submission_id: 3a722d4da2a1e17acc4020f84416b0891c46855d
# seed: 4084893092

# Time:  O(nlogn)
# Space: O(1)

# sort

class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums.sort()
        return min((nums[i]+nums[~i])/2.0 for i in xrange(len(nums)//2))