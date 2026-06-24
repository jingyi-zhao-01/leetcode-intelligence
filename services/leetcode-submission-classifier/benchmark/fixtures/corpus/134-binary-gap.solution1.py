# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-gap
# source_path: LeetCode-Solutions-master/Python/binary-gap.py
# solution_class: Solution
# submission_id: eb7f0e973a52e78f6f1e8384c4215359adfa20ab
# seed: 3691248936

# Time:  O(logn) = O(1) due to n is a 32-bit number
# Space: O(1)

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = 0
        last = None
        for i in xrange(32):
            if (N >> i) & 1:
                if last is not None:
                    result = max(result, i-last)
                last = i
        return result