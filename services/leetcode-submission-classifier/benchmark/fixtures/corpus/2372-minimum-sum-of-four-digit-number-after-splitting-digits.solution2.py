# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-sum-of-four-digit-number-after-splitting-digits
# source_path: LeetCode-Solutions-master/Python/minimum-sum-of-four-digit-number-after-splitting-digits.py
# solution_class: Solution2
# submission_id: bf74535a1e396860a50a8e922d8ab5ccda15f250
# seed: 1141070439

# Time:  O(d) = O(1), d is the number of digits
# Space: O(d) = O(1)

# greedy

class Solution2(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = sorted(map(int, list(str(num))))
        a = b = 0
        for x in nums:
            a = a*10+x
            a, b = b, a
        return a+b