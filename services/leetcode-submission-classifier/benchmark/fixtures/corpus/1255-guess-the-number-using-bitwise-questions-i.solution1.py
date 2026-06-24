# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: guess-the-number-using-bitwise-questions-i
# source_path: LeetCode-Solutions-master/Python/guess-the-number-using-bitwise-questions-i.py
# solution_class: Solution
# submission_id: 93ca4079ac23952a6e504473bc41199b3ab8d7f8
# seed: 3917945907

# Time:  O(logn):
# Space: O(1)

# bit manipulation

class Solution(object):
    def findNumber(self):
        """
        :rtype: int
        """
        return reduce(lambda accu, x: accu|x, (1<<i for i in xrange(30) if commonSetBits(1<<i)))