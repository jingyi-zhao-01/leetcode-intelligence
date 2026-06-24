# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-happy-prefix
# source_path: LeetCode-Solutions-master/Python/longest-happy-prefix.py
# solution_class: Solution2
# submission_id: f69036b5db68482872a2cdba5a7bec49cca4aace
# seed: 3426875401

# Time:  O(n)
# Space: O(n)

# kmp solution

class Solution2(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        M = 10**9+7
        D = 26
        def check(l, s):
            for i in xrange(l):
                if s[i] != s[len(s)-l+i]:
                    return False
            return True
    
        result, prefix, suffix, power = 0, 0, 0, 1
        for i in xrange(len(s)-1):
            prefix = (prefix*D + (ord(s[i])-ord('a'))) % M
            suffix = (suffix + (ord(s[len(s)-(i+1)])-ord('a'))*power) % M
            power = (power*D)%M
            if prefix == suffix:
                # we assume M is a very large prime without hash collision
                # assert(check(i+1, s))
                result = i+1
        return s[:result]