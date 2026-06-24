# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-calories-burnt-from-jumps
# source_path: LeetCode-Solutions-master/Python/maximum-calories-burnt-from-jumps.py
# solution_class: Solution2
# submission_id: 15c1055428c98934f51b226c40d70915b1499d28
# seed: 3156971181

# Time:  O(nlogn)
# Space: O(1)

# sort, greedy

class Solution2(object):
    def maxCaloriesBurnt(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.sort()
        d = 0
        left, right = 0, len(heights)-1
        result = (0-heights[right])**2
        while left != right:
            result += (heights[right]-heights[left])**2
            left += d
            d ^= 1
            right -= d
        return result