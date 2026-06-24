# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: exactly-one-consecutive-set-bits-pair
# source_path: LeetCode-Solutions-master/Python/exactly-one-consecutive-set-bits-pair.py
# solution_class: Solution
# submission_id: e5262d117d905955c62e4133afd3126f2ea2eeb8
# seed: 4027268032

# Time:  O(1)
# Space: O(1)

# bit manipulation

class Solution(object):
    def consecutiveSetBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def is_power_of_2(n):
            return n > 0 and n&(n-1) == 0

        return is_power_of_2(n&(n>>1))