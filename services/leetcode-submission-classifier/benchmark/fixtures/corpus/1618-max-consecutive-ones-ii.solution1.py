# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: max-consecutive-ones-ii
# source_path: LeetCode-Solutions-master/Python/max-consecutive-ones-ii.py
# solution_class: Solution
# submission_id: f1987fb6981398d9573acb8b1f2fc6c051c5381c
# seed: 3005377141

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, prev, curr = 0, 0, 0
        for n in nums:
            if n == 0:
                result = max(result, prev+curr+1)
                prev, curr = curr, 0
            else:
                curr += 1
        return min(max(result, prev+curr+1), len(nums))