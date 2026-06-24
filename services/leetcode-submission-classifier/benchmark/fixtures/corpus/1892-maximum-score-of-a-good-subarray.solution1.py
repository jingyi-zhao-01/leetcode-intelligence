# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-score-of-a-good-subarray
# source_path: LeetCode-Solutions-master/Python/maximum-score-of-a-good-subarray.py
# solution_class: Solution
# submission_id: 5ff970bffb9b7becca40e6ed53ea4b242fb24a8b
# seed: 396962184

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = curr = nums[k]
        left = right = k
        while left-1 >= 0 or right+1 < len(nums):
            # choosing larger one to expand is always better than or equal to choosing smaller one
            if (nums[left-1] if left-1 >= 0 else 0) <= (nums[right+1] if right+1 < len(nums) else 0):
                right += 1
            else:
                left -= 1
            curr = min(curr, nums[left], nums[right])
            result = max(result, curr*(right-left+1))
        return result