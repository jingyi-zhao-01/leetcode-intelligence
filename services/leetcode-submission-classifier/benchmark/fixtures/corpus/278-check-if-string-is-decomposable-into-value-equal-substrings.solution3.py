# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-string-is-decomposable-into-value-equal-substrings
# source_path: LeetCode-Solutions-master/Python/check-if-string-is-decomposable-into-value-equal-substrings.py
# solution_class: Solution3
# submission_id: a07090afc5bd88ba7fe2c7fa7b1200b44b3ee23f
# seed: 416150061

# Time:  O(n)
# Space: O(1)

class Solution3(object):
    def isDecomposable(self, s):
        """
        :type s: str
        :rtype: bool
        """
        found, l = False, 0
        for i, c in enumerate(s):
            if not l or c != s[i-1]:
                if l:
                    return False
                l = 1
                continue
            l += 1
            if l == 2:
                if i == len(s)-1 or s[i] != s[i+1]:
                    if found:
                        return False
                    found, l = True, 0
            elif l == 3:
                 l =  0
        return found