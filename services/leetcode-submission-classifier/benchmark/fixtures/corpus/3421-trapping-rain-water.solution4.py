# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: trapping-rain-water
# source_path: LeetCode-Solutions-master/Python/trapping-rain-water.py
# solution_class: Solution4
# submission_id: ff2c7b29d9c2d035d042dc5ebd3966cd5c576493
# seed: 347356782

# Time:  O(n)
# Space: O(1)

class Solution4(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        stk = []
        for i in xrange(len(height)):
            prev = 0
            while stk and height[stk[-1]] <= height[i]:
                j = stk.pop()
                result += (height[j] - prev) * (i - j - 1)
                prev = height[j]
            if stk:
                result += (height[i] - prev) * (i - stk[-1] - 1)
            stk.append(i)
        return result