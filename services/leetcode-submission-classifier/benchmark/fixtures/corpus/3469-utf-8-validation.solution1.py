# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: utf-8-validation
# source_path: LeetCode-Solutions-master/Python/utf-8-validation.py
# solution_class: Solution
# submission_id: c1b6ac712f3c9b6cb88e601a0c0c05504efbe540
# seed: 850330325

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for c in data:
            if count == 0:
                if (c >> 5) == 0b110:
                    count = 1
                elif (c >> 4) == 0b1110:
                    count = 2
                elif (c >> 3) == 0b11110:
                    count = 3
                elif (c >> 7):
                    return False
            else:
                if (c >> 6) != 0b10:
                    return False
                count -= 1
        return count == 0