# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-consecutive-values-you-can-make
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-consecutive-values-you-can-make.py
# solution_class: Solution
# submission_id: f27a56df9ff6548905877b5025e1ddb3e0684f07
# seed: 371278871

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        result = 1
        for c in coins:
            if c > result:
                break
            result += c
        return result