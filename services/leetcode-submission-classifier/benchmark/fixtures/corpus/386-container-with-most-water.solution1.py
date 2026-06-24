# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: container-with-most-water
# source_path: LeetCode-Solutions-master/Python/container-with-most-water.py
# solution_class: Solution
# submission_id: 18e8341829f192c761d56e0fd346b0ea21784c8b
# seed: 3011204217

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @return an integer
    def maxArea(self, height):
        max_area, i, j = 0, 0, len(height) - 1
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area