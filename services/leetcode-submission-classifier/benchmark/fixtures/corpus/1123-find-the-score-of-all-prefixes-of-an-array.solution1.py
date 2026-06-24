# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-score-of-all-prefixes-of-an-array
# source_path: LeetCode-Solutions-master/Python/find-the-score-of-all-prefixes-of-an-array.py
# solution_class: Solution
# submission_id: 74d6b1d0455a7dbb3f4df8197551a12e64e7669d
# seed: 1166098402

# Time:  O(n)
# Space: O(1)

# prefix sum

class Solution(object):
    def findPrefixScore(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        curr = 0
        for i in xrange(len(nums)):
            curr = max(curr, nums[i])
            nums[i] += (nums[i-1] if i-1 >= 0 else 0)+curr
        return nums