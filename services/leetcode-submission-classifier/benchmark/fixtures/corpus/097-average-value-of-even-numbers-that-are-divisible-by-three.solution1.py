# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: average-value-of-even-numbers-that-are-divisible-by-three
# source_path: LeetCode-Solutions-master/Python/average-value-of-even-numbers-that-are-divisible-by-three.py
# solution_class: Solution
# submission_id: 2ea0652286625ecb0ea9ffd3b108e79592015d47
# seed: 483740287

# Time:  O(n)
# Space: O(1)

# math

class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = cnt = 0
        for x in nums:
            if x%6:
                continue
            total += x
            cnt += 1
        return total//cnt if cnt else 0