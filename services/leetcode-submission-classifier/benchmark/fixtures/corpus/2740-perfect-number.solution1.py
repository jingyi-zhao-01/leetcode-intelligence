# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: perfect-number
# source_path: LeetCode-Solutions-master/Python/perfect-number.py
# solution_class: Solution
# submission_id: 9d4afac0bd90cd03ce48024e8265a1e8a7d556af
# seed: 1557145699

# Time:  O(sqrt(n))
# Space: O(1)

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        sqrt_num = int(num ** 0.5)
        total = sum(i+num//i for i in xrange(1, sqrt_num+1) if num%i == 0)
        if sqrt_num ** 2 == num:
            total -= sqrt_num
        return total - num == num