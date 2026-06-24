# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reduction-operations-to-make-the-array-elements-equal
# source_path: LeetCode-Solutions-master/Python/reduction-operations-to-make-the-array-elements-equal.py
# solution_class: Solution
# submission_id: 8958db36f1c9bdd7d066350e9d474347a0c05de8
# seed: 557061880

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = curr = 0
        for i in xrange(1, len(nums)): 
            if nums[i-1] < nums[i]:
                curr += 1
            result += curr
        return result