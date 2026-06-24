# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: replace-all-s-to-avoid-consecutive-repeating-characters
# source_path: LeetCode-Solutions-master/Python/replace-all-s-to-avoid-consecutive-repeating-characters.py
# solution_class: Solution
# submission_id: b91f7ac017a8b05c1d039a484ff4b2f2883af965
# seed: 3540868905

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for i in xrange(len(s)):
            if s[i] != '?':
                continue
            for c in ('a', 'b', 'c'):
                if (i == 0 or s[i-1] != c) and (i == len(s)-1 or c != s[i+1]):
                    break
            s[i] = c
        return "".join(s)