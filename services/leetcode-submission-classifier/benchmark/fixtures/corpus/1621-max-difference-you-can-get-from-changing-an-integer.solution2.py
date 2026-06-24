# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: max-difference-you-can-get-from-changing-an-integer
# source_path: LeetCode-Solutions-master/Python/max-difference-you-can-get-from-changing-an-integer.py
# solution_class: Solution2
# submission_id: e866ebb632b6102ed1d6fc6eaea07a71cdb9609b
# seed: 452679186

# Time:  O(logn)
# Space: O(1)

# greedy

class Solution2(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = str(num)
        b = next((x for x in digits if x < '9'), '0')
        a = next((x for x in digits if x > '1'), '0')
        return int(digits.replace(b, '9'))-int(digits.replace(a, '1' if digits[0] != '1' else '0'))