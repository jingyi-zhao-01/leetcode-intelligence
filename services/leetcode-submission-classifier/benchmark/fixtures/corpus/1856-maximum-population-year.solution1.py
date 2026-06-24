# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-population-year
# source_path: LeetCode-Solutions-master/Python/maximum-population-year.py
# solution_class: Solution
# submission_id: 64fc9543b76abfb8372e73905e85af4273456ba0
# seed: 1624058754

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        MIN_YEAR, MAX_YEAR = 1950, 2050
        years = [0]*(MAX_YEAR-MIN_YEAR+1)
        for s, e in logs:
            years[s-MIN_YEAR] += 1
            years[e-MIN_YEAR] -= 1
        result = 0
        for i in xrange(len(years)):
            if i:
                years[i] += years[i-1]
            if years[i] > years[result]:
                result = i
        return result+MIN_YEAR