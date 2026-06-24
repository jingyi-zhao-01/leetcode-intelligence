# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-odd-binary-number
# source_path: LeetCode-Solutions-master/Python/maximum-odd-binary-number.py
# solution_class: Solution2
# submission_id: 07eaf635fc92f6c526d876aa74dadcbb53b2d151
# seed: 3359498994

# Time:  O(n)
# Space: O(1)

# greedy, partition

class Solution2(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = s.count('1')
        return "".join(['1']*(n-1)+['0']*(len(s)-n)+['1'])