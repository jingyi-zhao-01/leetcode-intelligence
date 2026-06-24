# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-balanced-subsequence-sum
# source_path: LeetCode-Solutions-master/Python/maximum-balanced-subsequence-sum.py
# solution_class: Solution
# submission_id: a21ef3ecb432a406e597f7c4f6c6f97638572341
# seed: 2657722493

# Time:  O(nlogn)
# Space: O(n)

from sortedcontainers import SortedList


# sorted list, binary search, mono stack

class Solution(object):
    def maxBalancedSubsequenceSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        NEG_INF = float("-inf")
        def query(sl, k):
            j = sl.bisect_left((k,))
            return sl[j-1][1] if j-1 >= 0 else NEG_INF
    
        def update(sl, k, v):
            j = sl.bisect_left((k,))
            if j < len(sl) and sl[j][0] == k:
                if not (sl[j][1] < v):
                    return
                del sl[j]
            elif not (j-1 < 0 or sl[j-1][1] < v):
                return
            sl.add((k, v))
            while j+1 < len(sl) and sl[j+1][1] <= sl[j][1]:
                del sl[j+1]

        sl = SortedList()
        for i, x in enumerate(nums):
            v = max(query(sl, (x-i)+1), 0)+x
            update(sl, x-i, v)
        return sl[-1][1]