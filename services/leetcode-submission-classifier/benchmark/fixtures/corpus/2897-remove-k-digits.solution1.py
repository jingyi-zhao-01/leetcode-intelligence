# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-k-digits
# source_path: LeetCode-Solutions-master/Python/remove-k-digits.py
# solution_class: Solution
# submission_id: 59b906772b797e882ad323c37dce6cbef8bb89a6
# seed: 2140826132

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        result = []
        for d in num:
            while k and result and result[-1] > d:
                result.pop()
                k -= 1
            result.append(d)
        return ''.join(result).lstrip('0')[:-k or None] or '0'