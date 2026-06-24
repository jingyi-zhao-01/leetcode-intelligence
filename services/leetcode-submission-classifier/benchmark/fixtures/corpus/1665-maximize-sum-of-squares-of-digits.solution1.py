# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-sum-of-squares-of-digits
# source_path: LeetCode-Solutions-master/Python/maximize-sum-of-squares-of-digits.py
# solution_class: Solution
# submission_id: a7782d8fcaa28b1c332e14eda175069cd7ce39c6
# seed: 4289798972

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if num*9 < sum:
            return ""
        q, r = divmod(sum, 9)
        result = ['0']*num
        for i in xrange(q):
            result[i] = '9'
        if r:
            result[q] = str(r)
        return "".join(result)