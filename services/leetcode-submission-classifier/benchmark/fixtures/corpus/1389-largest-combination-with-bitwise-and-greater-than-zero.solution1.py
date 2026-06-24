# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-combination-with-bitwise-and-greater-than-zero
# source_path: LeetCode-Solutions-master/Python/largest-combination-with-bitwise-and-greater-than-zero.py
# solution_class: Solution
# submission_id: fe42e5a93e6d527f9b44963418b3550445c2bc17
# seed: 2119452608

# Time:  O(nlogr), r is the max of candidates
# Space: O(logr)

# bit manipulation, freq table

class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        cnt = []
        base, mx = 1, max(candidates)
        while base <= mx:
            cnt.append(sum(x&base > 0 for x in candidates))
            base <<= 1
        return max(cnt)