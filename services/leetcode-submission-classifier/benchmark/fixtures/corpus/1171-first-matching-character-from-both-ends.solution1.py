# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: first-matching-character-from-both-ends
# source_path: LeetCode-Solutions-master/Python/first-matching-character-from-both-ends.py
# solution_class: Solution
# submission_id: 1f12cc53580aeeef72e6ea36d3be3ed4ba8d2e93
# seed: 1157852431

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def firstMatchingIndex(self, s):
        """
        :type s: str
        :rtype: int
        """
        return next((i for i in xrange(len(s)) if s[i] == s[~i]), -1)