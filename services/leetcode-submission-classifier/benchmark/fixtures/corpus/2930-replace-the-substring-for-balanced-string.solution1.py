# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: replace-the-substring-for-balanced-string
# source_path: LeetCode-Solutions-master/Python/replace-the-substring-for-balanced-string.py
# solution_class: Solution
# submission_id: 6c6599d375e9cf4375daca7ec9c35dfa4e654c5b
# seed: 3961383032

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        result = len(s) 
        left = 0
        for right in xrange(len(s)):
            count[s[right]] -= 1
            while left < len(s) and \
                  all(v <= len(s)//4 for v in count.itervalues()):
                result = min(result, right-left+1)
                count[s[left]] += 1
                left += 1
        return result