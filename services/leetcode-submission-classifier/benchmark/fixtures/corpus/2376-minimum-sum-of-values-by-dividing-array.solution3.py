# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-sum-of-values-by-dividing-array
# source_path: LeetCode-Solutions-master/Python/minimum-sum-of-values-by-dividing-array.py
# solution_class: Solution3
# submission_id: ae615a8a9b7f193014023ba4a0a6b99b0fd827c7
# seed: 2244975642

# Time:  O(n * m * logr), r = max(nums)
# Space: O(n + logr)

import collections


# dp, mono deque, two pointers

class Solution3(object):
    def minimumValueSum(self, nums, andValues):
        """
        :type nums: List[int]
        :type andValues: List[int]
        :rtype: int
        """
        INF = float("inf")
        FULL_MASK = (1<<max(nums).bit_length())-1
        def memoization(i, j, mask): 
            if i == len(nums) and j == len(andValues):
                return 0
            if i == len(nums) or j == len(andValues) or mask < andValues[j]:
                return INF 
            if  mask not in lookup[i][j]:
                curr = memoization(i+1, j, mask&nums[i])
                if mask&nums[i] == andValues[j]:
                    curr = min(curr, nums[i]+memoization(i+1, j+1, FULL_MASK))
                lookup[i][j][mask] = curr
            return lookup[i][j][mask]
    
        lookup = [[collections.defaultdict(int) for _ in xrange(len(andValues))] for _ in xrange(len(nums))]
        result = memoization(0, 0, FULL_MASK)
        return result if result != INF else -1