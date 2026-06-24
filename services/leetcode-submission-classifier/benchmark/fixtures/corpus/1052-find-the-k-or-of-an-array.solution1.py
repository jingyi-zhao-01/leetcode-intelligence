# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-k-or-of-an-array
# source_path: LeetCode-Solutions-master/Python/find-the-k-or-of-an-array.py
# solution_class: Solution
# submission_id: 17da75b3e0282087f8b664e51d883e95a8e15fb6
# seed: 198790694

# Time:  O(nlogr)
# Space: O(1)

# bit manipulation

class Solution(object):
    def findKOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sum(1<<i for i in xrange(max(nums).bit_length()) if sum((x&(1<<i)) != 0 for x in nums) >= k)