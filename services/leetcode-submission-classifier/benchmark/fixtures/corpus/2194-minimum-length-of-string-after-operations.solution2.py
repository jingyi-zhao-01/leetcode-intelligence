# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-length-of-string-after-operations
# source_path: LeetCode-Solutions-master/Python/minimum-length-of-string-after-operations.py
# solution_class: Solution2
# submission_id: fea2f762ef159d3b5f16512c57fb9293a09cc108
# seed: 1571595531

# Time:  O(n + 26)
# Space: O(26)

# freq table

class Solution2(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(2-x%2 for x in collections.Counter(s).itervalues())