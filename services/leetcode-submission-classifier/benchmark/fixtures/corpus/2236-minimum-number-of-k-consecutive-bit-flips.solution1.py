# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-k-consecutive-bit-flips
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-k-consecutive-bit-flips.py
# solution_class: Solution
# submission_id: f9eece97b52456cb25ad1299886844022e354f8b
# seed: 3945425429

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        result, curr = 0, 0
        for i in xrange(len(A)):
            if i >= K:
                curr -= A[i-K]//2
            if curr & 1 ^ A[i] == 0:
                if i+K > len(A):
                    return -1
                A[i] += 2
                curr, result = curr+1, result+1
        return result