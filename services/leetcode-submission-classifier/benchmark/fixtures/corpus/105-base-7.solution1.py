# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: base-7
# source_path: LeetCode-Solutions-master/Python/base-7.py
# solution_class: Solution
# submission_id: 6a68a54d92d16512091b2b2496416226e46aa38e
# seed: 2842114094

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def convertToBase7(self, num):
        if num < 0:
            return '-' + self.convertToBase7(-num)
        result = ''
        while num:
            result = str(num % 7) + result
            num //= 7
        return result if result else '0'