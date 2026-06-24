# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: add-minimum-number-of-rungs
# source_path: LeetCode-Solutions-master/Python/add-minimum-number-of-rungs.py
# solution_class: Solution
# submission_id: 962e24687926d6ec29f375c1434475a126eb5663
# seed: 1687850242

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+(b-1))//b

        result = prev = 0
        for curr in rungs:
            result += ceil_divide(curr-prev, dist)-1
            prev = curr
        return result