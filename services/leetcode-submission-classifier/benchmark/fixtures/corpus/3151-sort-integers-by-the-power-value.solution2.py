# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-integers-by-the-power-value
# source_path: LeetCode-Solutions-master/Python/sort-integers-by-the-power-value.py
# solution_class: Solution2
# submission_id: 66df3ec66b3ca0f00617189dce5ec69a16c4bc1a
# seed: 1952487642

# Time:  O(n) on average
# Space: O(n)

import random

class Solution2(object):
    dp = {}

    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        def power_value(x):
            y, result = x, 0
            while x > 1 and x not in Solution2.dp:
                result += 1
                if x%2:
                    x = 3*x + 1
                else:
                    x //= 2
            Solution2.dp[y] = result + (Solution2.dp[x] if x > 1 else 0)
            return Solution2.dp[y], y
        
        return sorted(range(lo, hi+1), key=power_value)[k-1]