# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-digit-from-number-to-maximize-result
# source_path: LeetCode-Solutions-master/Python/remove-digit-from-number-to-maximize-result.py
# solution_class: Solution
# submission_id: 6cf45be570d868c9e34a615d71071e3baf3f3f42
# seed: 2357505628

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        i = next((i for i in xrange(len(number)-1) if digit == number[i] < number[i+1]), len(number)-1)
        if i+1 == len(number):
            i = next((i for i in reversed(xrange(len(number))) if digit == number[i]))
        return number[:i]+number[i+1:]