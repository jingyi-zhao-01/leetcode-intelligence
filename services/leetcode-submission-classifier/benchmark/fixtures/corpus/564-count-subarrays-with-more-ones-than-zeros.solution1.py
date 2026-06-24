# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-subarrays-with-more-ones-than-zeros
# source_path: LeetCode-Solutions-master/Python/count-subarrays-with-more-ones-than-zeros.py
# solution_class: Solution
# submission_id: 632317e841cad35ca4f16b01254c927430332dfb
# seed: 649613562

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def subarraysWithMoreZerosThanOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7

        lookup = collections.defaultdict(int)
        lookup[0] = 1
        result = total = same = more = 0
        for x in nums:
            total += 1 if x == 1 else -1
            new_same = lookup[total]
            new_more = (same+more+1)%MOD if x == 1 else (more-new_same)%MOD
            lookup[total] += 1
            result = (result+new_more)%MOD
            same, more = new_same, new_more
        return result