# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-the-array-k-increasing
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-the-array-k-increasing.py
# solution_class: Solution
# submission_id: 787e45e6eb932c7270d7febee8987fd6773c80b1
# seed: 3510218955

# Time:  O(k * (n/k)log(n/k)) = O(nlog(n/k))
# Space: O(n/k)

import bisect

class Solution(object):
    def kIncreasing(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        def longest_non_decreasing_subsequence(arr):
            result = []
            for x in arr:
                right = bisect.bisect_right(result, x)
                if right == len(result):
                    result.append(x)
                else:
                    result[right] = x
            return len(result)

        return len(arr) - sum(longest_non_decreasing_subsequence((arr[j] for j in xrange(i, len(arr), k))) for i in xrange(k))