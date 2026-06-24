# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: merge-operations-to-turn-array-into-a-palindrome
# source_path: LeetCode-Solutions-master/Python/merge-operations-to-turn-array-into-a-palindrome.py
# solution_class: Solution
# submission_id: 3a9fa86d78838cec66bb8ba2dbb923862fd70119
# seed: 3484459400

# Time:  O(n)
# Space: O(1)

# constructive algorithms, greedy, two pointers

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        left, right = 0, len(nums)-1
        l, r = nums[left], nums[right]
        while left < right:
            if l == r:
                left += 1
                right -= 1
                l, r = nums[left], nums[right]
                continue
            if l < r:
                left += 1
                l += nums[left]
            else:
                right -= 1
                r += nums[right]
            result += 1
        return result