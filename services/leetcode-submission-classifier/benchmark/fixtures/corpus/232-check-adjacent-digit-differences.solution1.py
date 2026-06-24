# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-adjacent-digit-differences
# source_path: LeetCode-Solutions-master/Python/check-adjacent-digit-differences.py
# solution_class: Solution
# submission_id: 527293a7a6ffc06a8e062a2ce041ed64c7f6ba97
# seed: 277336316

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def isAdjacentDiffAtMostTwo(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return all(abs(ord(s[i])-ord(s[i+1])) <= 2 for i in xrange(len(s)-1))