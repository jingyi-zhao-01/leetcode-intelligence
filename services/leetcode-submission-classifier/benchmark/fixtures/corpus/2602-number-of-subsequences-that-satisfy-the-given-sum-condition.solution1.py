# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-subsequences-that-satisfy-the-given-sum-condition
# source_path: LeetCode-Solutions-master/Python/number-of-subsequences-that-satisfy-the-given-sum-condition.py
# solution_class: Solution
# submission_id: ce394deab7f8410a58c5333fa39f004960933090
# seed: 2132299317

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        nums.sort()
        result = 0
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left]+nums[right] > target:
                right -= 1
            else:
                result = (result+pow(2, right-left, MOD))%MOD
                left += 1
        return result