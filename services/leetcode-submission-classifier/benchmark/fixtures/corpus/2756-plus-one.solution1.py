# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: plus-one
# source_path: LeetCode-Solutions-master/Python/plus-one.py
# solution_class: Solution
# submission_id: 727c1b98fe61e939057c884a3389d277e87a6f2a
# seed: 3650692546

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(xrange(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits