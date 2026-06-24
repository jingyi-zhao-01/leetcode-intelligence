# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: two-furthest-houses-with-different-colors
# source_path: LeetCode-Solutions-master/Python/two-furthest-houses-with-different-colors.py
# solution_class: Solution
# submission_id: 8535018f2f85ab21494c48ec51c2876032bc521a
# seed: 3037538375

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        result = 0
        for i, x in enumerate(colors):
            if x != colors[0]:
                result = max(result, i)
            if x != colors[-1]:
                result = max(result, len(colors)-1-i)
        return result