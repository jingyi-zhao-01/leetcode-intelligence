# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: buildings-with-an-ocean-view
# source_path: LeetCode-Solutions-master/Python/buildings-with-an-ocean-view.py
# solution_class: Solution2
# submission_id: 7f889365f138386b2a549c8d6b9f7269f73d028b
# seed: 4079312023

# Time:  O(n)
# Space: O(n)

class Solution2(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        result = []
        for i in reversed(xrange(len(heights))):
            if not result or heights[result[-1]] < heights[i]:
                result.append(i)
        result.reverse()
        return result