# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: trapping-rain-water
# source_path: LeetCode-Solutions-master/Python/trapping-rain-water.py
# solution_class: Solution
# submission_id: 0f3cc6931456b59fec51079799ba29cb81091131
# seed: 3859708001

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result, left, right, level = 0, 0, len(height)-1, 0
        while left < right:
            if height[left] < height[right]:
                lower = height[left]
                left += 1
            else:
                lower = height[right]
                right -= 1
            level = max(level, lower)
            result += level-lower
        return result