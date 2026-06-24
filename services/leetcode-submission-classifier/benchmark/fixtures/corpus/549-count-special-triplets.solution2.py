# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-special-triplets
# source_path: LeetCode-Solutions-master/Python/count-special-triplets.py
# solution_class: Solution2
# submission_id: 4d55bf542f907270a67c099b106818a34fbcfa48
# seed: 3279976060

# Time:  O(n)
# Space: O(n)

import collections


# dp

class Solution2(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        result = 0
        right = collections.defaultdict(int)
        for x in nums:
            right[x] += 1
        left = collections.defaultdict(int)
        for x in nums:
            right[x] -= 1
            if not right[x]:
                del right[x]
            if 2*x in left and 2*x in right:
                result = (result+left[2*x]*right[2*x])%MOD
            left[x] += 1
        return result