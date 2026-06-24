# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: super-palindromes
# source_path: LeetCode-Solutions-master/Python/super-palindromes.py
# solution_class: Solution
# submission_id: 67d1e8b278bad91aba6075f2bc7986ff161f6f55
# seed: 3824543249

# Time:  O(n^0.25 * logn)
# Space: O(logn)

class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        def is_palindrome(k):
            return str(k) == str(k)[::-1]

        K = int((10**((len(R)+1)*0.25)))
        l, r = int(L), int(R)

        result = 0

        # count odd length
        for k in xrange(K):
            s = str(k)
            t = s + s[-2::-1]
            v = int(t)**2
            if v > r:
                break
            if v >= l and is_palindrome(v):
                result += 1

        # count even length
        for k in xrange(K):
            s = str(k)
            t = s + s[::-1]
            v = int(t)**2
            if v > r:
                break
            if v >= l and is_palindrome(v):
                result += 1

        return result