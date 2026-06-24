# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: guess-the-number-using-bitwise-questions-ii
# source_path: LeetCode-Solutions-master/Python/guess-the-number-using-bitwise-questions-ii.py
# solution_class: Solution
# submission_id: 3254dcaff1220b2e073d5d0b91d5cb9545986a6c
# seed: 4039865421

# Time:  O(logr)
# Space: O(1)

# bit manipulation

class Solution(object):
    def findNumber(self):
        """
        :rtype: int
        """
        BIT_COUNT = 30
        result = 0
        prev = commonBits(0)
        for i in xrange(BIT_COUNT):
            curr = commonBits(1<<i)
            if curr-prev == 1:
                result |= 1<<i
            prev = curr
        return result