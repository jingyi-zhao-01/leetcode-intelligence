# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-beautiful-substrings-i
# source_path: LeetCode-Solutions-master/Python/count-beautiful-substrings-i.py
# solution_class: Solution2
# submission_id: 4c2a6708fce1b02c4c7bde40ef17a43c7a19fb74
# seed: 527431617

# Time:  O(n + sqrt(k))
# Space: O(n)

# number theory, prefix sum, freq table

class Solution2(object):
    def beautifulSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        VOWELS = set("aeiou")
        result = 0
        for i in xrange(len(s)):
            c = v = 0
            for j in xrange(i, len(s)):
                if s[j] in VOWELS:
                    v += 1
                else:
                    c += 1
                if c == v and (c*v)%k == 0:
                    result += 1
        return result