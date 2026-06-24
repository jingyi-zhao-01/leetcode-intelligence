# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-consecutive-subsequences
# source_path: LeetCode-Solutions-master/Python/sum-of-consecutive-subsequences.py
# solution_class: Solution
# submission_id: 9d4a63f149aa61e3d492627dfd3d6357fc98e941
# seed: 2130901134

# Time:  O(n)
# Space: O(n)

import collections


# combinatorics, prefix sum, freq table, dp

class Solution(object):
    def getSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def count(d):
            result = 0
            cnt = collections.defaultdict(int)
            prefix = collections.defaultdict(int)
            for x in nums:
                c = (cnt[x-d]+1)%MOD
                cnt[x] = (cnt[x]+c)%MOD
                total = (prefix[x-d]+x*c)%MOD
                prefix[x] = (prefix[x]+total)%MOD
                result = (result+total)%MOD
            return result
    
        MOD = 10**9+7
        return (count(+1)+count(-1)-reduce(lambda accu, x: (accu+x)%MOD, nums, 0))%MOD