# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-3-same-digit-number-in-string
# source_path: LeetCode-Solutions-master/Python/largest-3-same-digit-number-in-string.py
# solution_class: Solution2
# submission_id: 463c9b298a076c71a3505f61fd135f4baadcaacc
# seed: 3701517174

# Time:  O(n)
# Space: O(1)

# string

class Solution2(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        return max(num[i] if num[i] == num[i+1] == num[i+2] else '' for i in xrange(len(num)-2))*3