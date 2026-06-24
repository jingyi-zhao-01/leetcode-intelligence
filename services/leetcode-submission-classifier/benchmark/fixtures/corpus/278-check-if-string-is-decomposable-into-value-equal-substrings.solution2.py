# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-string-is-decomposable-into-value-equal-substrings
# source_path: LeetCode-Solutions-master/Python/check-if-string-is-decomposable-into-value-equal-substrings.py
# solution_class: Solution2
# submission_id: eca829ba219a163d5b142754fb3483270442b1e8
# seed: 1329532998

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def isDecomposable(self, s):
        """
        :type s: str
        :rtype: bool
        """
        found, i = False, 0
        while i < len(s):
            l = 1
            for j in xrange(i+1, min(i+3, len(s))):
                if s[j] != s[i]:
                    break
                l += 1
            if l < 2:
                return False
            if l == 2:
                if found:
                    return False
                found = True
            i += l  
        return found