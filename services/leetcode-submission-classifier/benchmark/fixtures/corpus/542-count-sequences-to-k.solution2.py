# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-sequences-to-k
# source_path: LeetCode-Solutions-master/Python/count-sequences-to-k.py
# solution_class: Solution2
# submission_id: b16fc7cd922f5e3fc95a1978a0cb7c4063da240c
# seed: 9462718

# Time:  O(3^(n/2))
# Space: O(3^(n/2))

import collections


# dp, meet in the middle

class Solution2(object):
    def countSequences(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        LOOKUP = {1:(0, 0, 0), 2:(1, 0, 0), 3:(0, 1, 0), 4:(2, 0, 0), 5:(0, 0, 1), 6:(1, 1, 0)}
        def factors(x):
            cnt2 = 0
            while x%2 == 0:
                x //= 2
                cnt2 += 1
            cnt3 = 0
            while x%3 == 0:
                x //= 3
                cnt3 += 1
            cnt5 = 0
            while x%5 == 0:
                x //= 5
                cnt5 += 1
            return (cnt2, cnt3, cnt5) if x == 1 else (-1, -1, -1)
    
        def count(nums):
            dp = collections.defaultdict(int)
            dp[0, 0, 0] = 1
            for x in nums:
                new_dp = collections.defaultdict(int)
                d2, d3, d5 = LOOKUP[x]
                for (c2, c3, c5), c in dp.iteritems():
                    new_dp[c2, c3, c5] += c
                    new_dp[c2+d2, c3+d3, c5+d5] += c
                    new_dp[c2-d2, c3-d3, c5-d5] += c
                dp = new_dp
            return dp
        
        c2, c3, c5 = factors(k)
        if c2 == -1:
            return 0
        dp = count(nums)
        return dp[c2, c3, c5]