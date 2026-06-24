# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-number
# source_path: LeetCode-Solutions-master/Python/largest-number.py
# solution_class: Solution
# submission_id: 61696a3aa781a44c562d5a1b01d91b3410e0c705
# seed: 732684624

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = [str(x) for x in num]
        num.sort(cmp=lambda x, y: cmp(y + x, x + y))
        largest = ''.join(num)
        return largest.lstrip('0') or '0'