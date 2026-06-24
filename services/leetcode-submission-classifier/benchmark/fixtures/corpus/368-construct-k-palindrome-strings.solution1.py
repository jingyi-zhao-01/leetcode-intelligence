# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: construct-k-palindrome-strings
# source_path: LeetCode-Solutions-master/Python/construct-k-palindrome-strings.py
# solution_class: Solution
# submission_id: b8db6bdd222a0e1ddff9b3f28e6c4b240de45a44
# seed: 3587785949

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        count = collections.Counter(s)
        odd = sum(v%2 for v in count.itervalues())
        return odd <= k <= len(s)