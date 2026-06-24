# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: get-equal-substrings-within-budget
# source_path: LeetCode-Solutions-master/Python/get-equal-substrings-within-budget.py
# solution_class: Solution
# submission_id: 860eb8642aa8de9c6a776e65275bb6bc1115b33b
# seed: 2542709212

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        left = 0
        for right in xrange(len(s)):
            maxCost -= abs(ord(s[right])-ord(t[right]))
            if maxCost < 0:
                maxCost += abs(ord(s[left])-ord(t[left]))
                left += 1
        return (right+1)-left