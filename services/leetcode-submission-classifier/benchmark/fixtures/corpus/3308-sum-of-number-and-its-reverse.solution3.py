# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-number-and-its-reverse
# source_path: LeetCode-Solutions-master/Python/sum-of-number-and-its-reverse.py
# solution_class: Solution3
# submission_id: 4036b29e270653993a65a869708e24cb31d8e52f
# seed: 2346039796

# Time:  O(2^(log10(n)/2)) = O(n^(1/(2*log2(10))))
# Space: O(log10(n)/2)

# backtracking

class Solution3(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return any(x+int(str(x)[::-1]) == num for x in xrange(num//2, num+1))