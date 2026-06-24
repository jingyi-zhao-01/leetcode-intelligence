# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: base-7
# source_path: LeetCode-Solutions-master/Python/base-7.py
# solution_class: Solution2
# submission_id: 2bbb56d3046bf309943908113bc19fbe97fa6811
# seed: 3360932468

# Time:  O(1)
# Space: O(1)

class Solution2(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            return '-' + self.convertToBase7(-num)
        if num < 7:
            return str(num)
        return self.convertToBase7(num // 7) + str(num % 7)