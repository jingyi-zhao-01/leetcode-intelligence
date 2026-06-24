# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-interval
# source_path: LeetCode-Solutions-master/Python/remove-interval.py
# solution_class: Solution
# submission_id: d2174bb223017ad3c09f3995ddaba6269eeac359
# seed: 3317796669

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        A, B = toBeRemoved
        return [[x, y] for a, b in intervals
                for x, y in ((a, min(A, b)), (max(a, B), b))
                if x < y]