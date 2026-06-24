# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-sum-of-values-by-dividing-array
# source_path: LeetCode-Solutions-master/Python/minimum-sum-of-values-by-dividing-array.py
# solution_class: Solution2
# submission_id: 6cf364fbfeb2d0aa6e8e4fdb89ac6e357658b3aa
# seed: 2563957927

# Time:  O(n * m * logr), r = max(nums)
# Space: O(n + logr)

import collections


# dp, mono deque, two pointers

class Solution2(object):
    def minimumValueSum(self, nums, andValues):
        """
        :type nums: List[int]
        :type andValues: List[int]
        :rtype: int
        """
        INF = float("inf")
        # RMQ - Sparse Table
        # Template: https://github.com/kamyu104/GoogleCodeJam-Farewell-Rounds/blob/main/Round%20D/genetic_sequences2.py3
        # Time:  ctor:  O(NlogN) * O(fn)
        #        query: O(fn)
        # Space: O(NlogN)
        class SparseTable(object):
            def __init__(self, arr, fn):
                self.fn = fn
                self.bit_length = [0]
                n = len(arr)
                k = n.bit_length()-1  # log2_floor(n)
                for i in xrange(k+1):
                    self.bit_length.extend(i+1 for _ in xrange(min(1<<i, (n+1)-len(self.bit_length))))
                self.st = [[0]*n for _ in xrange(k+1)]
                self.st[0] = arr[:]
                for i in xrange(1, k+1):  # Time: O(NlogN) * O(fn)
                    for j in xrange((n-(1<<i))+1):
                        self.st[i][j] = fn(self.st[i-1][j], self.st[i-1][j+(1<<(i-1))])
        
            def query(self, L, R):  # Time: O(fn)
                i = self.bit_length[R-L+1]-1  # log2_floor(R-L+1)
                return self.fn(self.st[i][L], self.st[i][R-(1<<i)+1])
        
        dp = [INF]*(len(nums)+1)
        dp[0] = 0
        for j in xrange(len(andValues)):
            new_dp = [INF]*(len(nums)+1)
            masks = []
            st = SparseTable(dp, min)
            for i in xrange(j, len(nums)):
                masks.append([nums[i], i])
                for x in masks:
                    x[0] &= nums[i]
                masks = [x for k, x in enumerate(masks) if k == 0 or masks[k-1][0] != masks[k][0]]
                for k, [mask, left] in enumerate(masks):
                    if mask == andValues[j]:
                        # any j in range(left, right+1) has same and(nums[j:i+1]) = mask
                        right = masks[k+1][1]-1 if k+1 != len(masks) else i
                        new_dp[i+1] = min(new_dp[i+1], st.query(left, right)+nums[i])
                        break
            dp = new_dp
        return dp[-1] if dp[-1] != INF else -1