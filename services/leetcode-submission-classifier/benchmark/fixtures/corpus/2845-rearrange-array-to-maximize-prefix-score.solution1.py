# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rearrange-array-to-maximize-prefix-score
# source_path: LeetCode-Solutions-master/Python/rearrange-array-to-maximize-prefix-score.py
# solution_class: Solution
# submission_id: 4be700f3a494d8bfc2cb520d8601d609abef5e33
# seed: 2932270887

# Time:  O(nlogn)
# Space: O(1)

# sort, greedy

class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        curr = 0
        for i, x in enumerate(nums):
            curr += x
            if curr <= 0:
                return i
        return len(nums)