# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: jump-game-ix
# source_path: LeetCode-Solutions-master/Python/jump-game-ix.py
# solution_class: Solution
# submission_id: a9d362914a74b753f0b8b396675273f4927b0763
# seed: 496424723

# Time:  O(n)
# Space: O(1)

# graph, prefix sum

class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0]*len(nums)
        result[0] = nums[0]
        for i in xrange(len(nums)-1):
            result[i+1] = max(result[i], nums[i+1])
        mn = float("inf")
        for i in reversed(xrange(len(nums))):
            if result[i] > mn:
                result[i] = result[i+1]
            mn = min(mn, nums[i])
        return result