# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-numbers-with-unique-digits
# source_path: LeetCode-Solutions-master/Python/count-numbers-with-unique-digits.py
# solution_class: Solution
# submission_id: 388f39d19e3736500d232496295f85f9af0e017b
# seed: 1353508702

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        result = cnt = 1
        for i in xrange(n-1):
            cnt *= 9-i
            result += cnt
        return 1+9*result