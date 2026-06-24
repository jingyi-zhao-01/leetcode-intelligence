# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: consecutive-characters
# source_path: LeetCode-Solutions-master/Python/consecutive-characters.py
# solution_class: Solution
# submission_id: b850c03d8b47829fedc51ae7d2685d5608f5597b
# seed: 2716816386

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, count = 1, 1
        for i in xrange(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            result = max(result, count)
        return result