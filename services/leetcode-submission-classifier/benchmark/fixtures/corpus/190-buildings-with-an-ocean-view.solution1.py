# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: buildings-with-an-ocean-view
# source_path: LeetCode-Solutions-master/Python/buildings-with-an-ocean-view.py
# solution_class: Solution
# submission_id: c4b49fd1b3ae769300a0df398b827405f3d0b86d
# seed: 249714545

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        result = []
        for i, h in enumerate(heights):
            while result and heights[result[-1]] <= h:
                result.pop()
            result.append(i)
        return result