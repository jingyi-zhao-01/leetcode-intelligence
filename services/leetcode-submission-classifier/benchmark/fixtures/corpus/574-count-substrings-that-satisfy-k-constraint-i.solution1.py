# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-substrings-that-satisfy-k-constraint-i
# source_path: LeetCode-Solutions-master/Python/count-substrings-that-satisfy-k-constraint-i.py
# solution_class: Solution
# submission_id: 6d16225878fb73bb71e1f27b21c59c980b70e416
# seed: 1544049032

# Time:  O(n)
# Space: O(1)

# two pointers, sliding window

class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = cnt = left = 0
        for right in xrange(len(s)):
            cnt += int(s[right] == '1')
            while not (cnt <= k or (right-left+1)-cnt <= k):
                cnt -= int(s[left] == '1')
                left += 1
            result += right-left+1
        return result