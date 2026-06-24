# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-kth-character-in-expanded-string
# source_path: LeetCode-Solutions-master/Python/find-kth-character-in-expanded-string.py
# solution_class: Solution
# submission_id: 60db824eef4fec7a60ff637ad3774eb9789cdc94
# seed: 1434295078

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def kthCharacter(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = 0
        for i in xrange(len(s)):
            if s[i] == ' ':
                l = 0
                k -= 1
            else:
                l += 1
                k -= l
            if k < 0:
                break
        return s[i]