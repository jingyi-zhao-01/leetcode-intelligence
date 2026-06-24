# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-operations-with-the-same-score-i
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-operations-with-the-same-score-i.py
# solution_class: Solution
# submission_id: b340ff817a10b4a107743798b55bc38feafcc772
# seed: 3775381802

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 1
        target = nums[0]+nums[1]
        for i in xrange(2, len(nums)-1, 2):
            if nums[i]+nums[i+1] != target:
                break
            result += 1
        return result