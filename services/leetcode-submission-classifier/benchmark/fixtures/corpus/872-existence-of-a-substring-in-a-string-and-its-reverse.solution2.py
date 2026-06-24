# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: existence-of-a-substring-in-a-string-and-its-reverse
# source_path: LeetCode-Solutions-master/Python/existence-of-a-substring-in-a-string-and-its-reverse.py
# solution_class: Solution2
# submission_id: cb252e4d483cd2fa4457a709b9091fedee0d4e54
# seed: 3786894849

# Time:  O(n)
# Space: O(min(n, 26^2))

# hash table

class Solution2(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = collections.defaultdict(set)
        for i in xrange(len(s)-1):
            lookup[s[i]].add(s[i+1])
        return any(s[i] in lookup[s[i+1]] for i in xrange(len(s)-1))