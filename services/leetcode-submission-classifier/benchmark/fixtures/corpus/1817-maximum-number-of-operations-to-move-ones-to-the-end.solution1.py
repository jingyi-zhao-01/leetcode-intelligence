# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-operations-to-move-ones-to-the-end
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-operations-to-move-ones-to-the-end.py
# solution_class: Solution
# submission_id: 471fc72cbf7b618be7ae08da088cc58af49f3b55
# seed: 2013529981

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = curr = 0
        for i in xrange(len(s)):
            if s[i] == '1':
                curr += 1
            elif i+1 == len(s) or s[i+1] == '1':
                result += curr
        return result