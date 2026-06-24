# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-longest-balanced-substring-of-a-binary-string
# source_path: LeetCode-Solutions-master/Python/find-the-longest-balanced-substring-of-a-binary-string.py
# solution_class: Solution
# submission_id: 853f56acbc295ec7322a142c723833be634048da
# seed: 689079288

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in xrange(len(s)):
            left, right = i+1, i
            while left-1 >= 0 and right+1 < len(s) and s[left-1] == '0' and s[right+1] == '1':
                left -= 1
                right += 1
            result = max(result, right-left+1)
        return result