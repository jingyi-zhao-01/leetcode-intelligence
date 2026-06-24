# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: trapping-rain-water
# source_path: LeetCode-Solutions-master/Python/trapping-rain-water.py
# solution_class: Solution3
# submission_id: 92d975723344c96d96a2ae99c2dad39b7411a23a
# seed: 980195774

# Time:  O(n)
# Space: O(1)

class Solution3(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right = [0]*len(height)
        mx = 0
        for i in reversed(xrange(len(height))):
            right[i] = mx
            mx = max(mx, height[i])
        result = left = 0
        for i in xrange(len(height)):
            left = max(left, height[i])
            result += max(min(left, right[i])-height[i], 0)
        return result