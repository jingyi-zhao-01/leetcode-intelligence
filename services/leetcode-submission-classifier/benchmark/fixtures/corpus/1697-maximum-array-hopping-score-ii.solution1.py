# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-array-hopping-score-ii
# source_path: LeetCode-Solutions-master/Python/maximum-array-hopping-score-ii.py
# solution_class: Solution
# submission_id: 3d9bee022db45e109085be101dd22f4b431dd013
# seed: 2833436762

# Time:  O(n)
# Space: O(1)

# prefix sum, greedy

class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = mx = 0
        for i in reversed(xrange(1, len(nums))):
            mx = max(mx, nums[i])
            result += mx
        return result