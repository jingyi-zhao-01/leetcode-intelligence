# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: apply-operations-to-make-two-strings-equal
# source_path: LeetCode-Solutions-master/Python/apply-operations-to-make-two-strings-equal.py
# solution_class: Solution
# submission_id: b1ffdae8eaac3b810d38ab5a713a2c17026ce9eb
# seed: 2181277508

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def minOperations(self, s1, s2, x):
        """
        :type s1: str
        :type s2: str
        :type x: int
        :rtype: int
        """
        parity = curr = prev = 0
        j = -1
        for i in xrange(len(s1)):
            if s1[i] == s2[i]:
                continue
            curr, prev = min(curr+x, prev+(i-j)*2 if j != -1 else float("inf")), curr
            j = i
            parity ^= 1
        return curr//2 if parity == 0 else -1