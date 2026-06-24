# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: guess-the-number-using-bitwise-questions-ii
# source_path: LeetCode-Solutions-master/Python/guess-the-number-using-bitwise-questions-ii.py
# solution_class: Solution2
# submission_id: ee000686be127f6ad85e50c8e5a909db450a2967
# seed: 3734235120

# Time:  O(logr)
# Space: O(1)

# bit manipulation

class Solution2(object):
    def findNumber(self):
        """
        :rtype: int
        """
        BIT_COUNT = 30
        return reduce(lambda accu, i: accu|(1<<i if commonBits(1<<i)-commonBits(1<<i) == 1 else 0), xrange(BIT_COUNT), 0)