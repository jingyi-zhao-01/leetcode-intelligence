# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-split-of-positive-even-integers
# source_path: LeetCode-Solutions-master/Python/maximum-split-of-positive-even-integers.py
# solution_class: Solution
# submission_id: e439e656a52cf27a7891f667ed1dbb95412bcdca
# seed: 755301280

# Time:  O(sqrt(n))
# Space: O(1)

# greedy

class Solution(object):
    def maximumEvenSplit(self, finalSum):
        """
        :type finalSum: int
        :rtype: List[int]
        """
        if finalSum%2:
            return []
        result = []
        i = 2
        while i <= finalSum:
            result.append(i)
            finalSum -= i
            i += 2
        result[-1] += finalSum
        return result