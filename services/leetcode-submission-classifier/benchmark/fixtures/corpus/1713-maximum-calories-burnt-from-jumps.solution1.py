# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-calories-burnt-from-jumps
# source_path: LeetCode-Solutions-master/Python/maximum-calories-burnt-from-jumps.py
# solution_class: Solution
# submission_id: e9b9dfd6992547e0d91cc7f30a9d5f906cc428f0
# seed: 3789969770

# Time:  O(nlogn)
# Space: O(1)

# sort, greedy

class Solution(object):
    def maxCaloriesBurnt(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.sort()
        left, right = 0, len(heights)-1
        result = (0-heights[right])**2
        while left != right:
            result += (heights[right]-heights[left])**2
            right -= 1
            if left == right:
                break
            result += (heights[left]-heights[right])**2
            left += 1
        return result