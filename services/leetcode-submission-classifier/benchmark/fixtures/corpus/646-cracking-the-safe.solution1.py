# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: cracking-the-safe
# source_path: LeetCode-Solutions-master/Python/cracking-the-safe.py
# solution_class: Solution
# submission_id: 1eca8aea81c3ba852ef72945c9d246acd77d7c52
# seed: 3091354552

# Time:  O(k^n)
# Space: O(k^n)

class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        M = k**(n-1)
        P = [q*k+i for i in xrange(k) for q in xrange(M)]  # rotate: i*k^(n-1) + q => q*k + i
        result = [str(k-1)]*(n-1)
        for i in xrange(k**n):
            j = i
            # concatenation in lexicographic order of Lyndon words
            while P[j] >= 0:
                result.append(str(j//M))
                P[j], j = -1, P[j]
        return "".join(result)