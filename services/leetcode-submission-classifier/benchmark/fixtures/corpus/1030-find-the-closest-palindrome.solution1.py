# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-closest-palindrome
# source_path: LeetCode-Solutions-master/Python/find-the-closest-palindrome.py
# solution_class: Solution
# submission_id: 81e7f99dba0c5bb9e5d4a4669102197b5464e252
# seed: 215391642

# Time:  O(l)
# Space: O(l)

class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        l = len(n)
        candidates = set((str(10**l + 1), str(10**(l - 1) - 1)))
        prefix = int(n[:(l + 1)/2])
        for i in map(str, (prefix-1, prefix, prefix+1)):
            candidates.add(i + [i, i[:-1]][l%2][::-1])
        candidates.discard(n)
        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))