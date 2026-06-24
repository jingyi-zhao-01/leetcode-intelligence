# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: stable-subarrays-with-equal-boundary-and-interior-sum
# source_path: LeetCode-Solutions-master/Python/stable-subarrays-with-equal-boundary-and-interior-sum.py
# solution_class: Solution
# submission_id: 4c26e54171294428731773db91b4f7e5b911e89e
# seed: 2995471616

# Time:  O(n)
# Space: O(n)

import collections


# freq table, prefix sum

class Solution(object):
    def countStableSubarrays(self, capacity):
        """
        :type capacity: List[int]
        :rtype: int
        """
        L = 3
        cnt = collections.defaultdict(lambda: collections.defaultdict(int))
        result = prefix = prefix2 = 0
        for i in xrange(len(capacity)):
            result += cnt[capacity[i]][prefix-capacity[i]]
            prefix += capacity[i]
            if (i+1)-L+1 >= 0:
                prefix2 += capacity[(i+1)-L+1]
                cnt[capacity[(i+1)-L+1]][prefix2] += 1
        return result