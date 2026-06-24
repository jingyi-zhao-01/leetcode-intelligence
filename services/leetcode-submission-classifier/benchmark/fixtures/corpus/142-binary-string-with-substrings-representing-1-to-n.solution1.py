# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-string-with-substrings-representing-1-to-n
# source_path: LeetCode-Solutions-master/Python/binary-string-with-substrings-representing-1-to-n.py
# solution_class: Solution
# submission_id: ec8e702f48a7dd360bd6e9c22e27a6e5cf9e4ea2
# seed: 2101354142

# Time:  O(n^2), n is the length of S
# Space: O(1)

class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        # since S with length n has at most different n-k+1 k-digit numbers
        # => given S with length n, valid N is at most 2(n-k+1)
        # => valid N <= 2(n-k+1) < 2n = 2 * S.length
        return all(bin(i)[2:] in S for i in reversed(xrange(N//2, N+1)))