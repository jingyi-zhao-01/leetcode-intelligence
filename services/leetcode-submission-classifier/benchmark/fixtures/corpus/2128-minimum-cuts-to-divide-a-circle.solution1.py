# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cuts-to-divide-a-circle
# source_path: LeetCode-Solutions-master/Python/minimum-cuts-to-divide-a-circle.py
# solution_class: Solution
# submission_id: 25a222859bf43d16cf02325c9c191c80879813a5
# seed: 1194466914

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def numberOfCuts(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 1 else n if n%2 else n//2