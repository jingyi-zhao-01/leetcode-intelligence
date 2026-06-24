# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-commas-in-range-ii
# source_path: LeetCode-Solutions-master/Python/count-commas-in-range-ii.py
# solution_class: Solution
# submission_id: 872af39e2bb8061502568b2af7b7c3f1060f9142
# seed: 963598959

# Time:  O(logn)
# Space: O(1)

# math

class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt, base = 0, 1
        while base*1000 <= n:
            base *= 1000
            cnt += 1
        result, base = 0, 1
        for i in xrange(cnt):
            base *= 1000
            result += n-base+1
        return result