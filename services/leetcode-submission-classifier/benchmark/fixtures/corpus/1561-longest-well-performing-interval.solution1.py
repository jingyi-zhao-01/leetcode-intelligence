# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-well-performing-interval
# source_path: LeetCode-Solutions-master/Python/longest-well-performing-interval.py
# solution_class: Solution
# submission_id: 4d7b3612b0ffa810bec855c5097d24eb1effd48b
# seed: 2728760800

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        result, accu = 0, 0
        lookup = {}
        for i, h in enumerate(hours):
            accu = accu+1 if h > 8 else accu-1
            if accu > 0:
                result = i+1
            elif accu-1 in lookup:
                # lookup[accu-1] is the leftmost idx with smaller accu,
                # because for i from 1 to some positive k,
                # lookup[accu-i] is a strickly increasing sequence
                result = max(result, i-lookup[accu-1])
            lookup.setdefault(accu, i)
        return result