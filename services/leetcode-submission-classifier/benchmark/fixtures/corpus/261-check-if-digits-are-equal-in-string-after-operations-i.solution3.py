# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-digits-are-equal-in-string-after-operations-i
# source_path: LeetCode-Solutions-master/Python/check-if-digits-are-equal-in-string-after-operations-i.py
# solution_class: Solution3
# submission_id: 7efb64078117273e915050b80417efa9a0752f27
# seed: 2671538250

# Time:  O(nlogn)
# Space: O(1)

# fast exponentiation

class Solution3(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = map(int, s)
        for l in reversed(xrange(3, len(s)+1)):
            for i in xrange(l-1):
                s[i] = (s[i]+s[i+1])%10
        return s[0] == s[1]