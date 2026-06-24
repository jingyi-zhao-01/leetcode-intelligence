# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-digits-that-divide-a-number
# source_path: LeetCode-Solutions-master/Python/count-the-digits-that-divide-a-number.py
# solution_class: Solution
# submission_id: 74ab07fb9b2f9e6b94009c9e446aefca3b9ca1ad
# seed: 37577512

# Time:  O(logn)
# Space: O(1)

# math

class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        curr = num
        while curr:
            result += int(num%(curr%10) == 0)
            curr //= 10
        return result