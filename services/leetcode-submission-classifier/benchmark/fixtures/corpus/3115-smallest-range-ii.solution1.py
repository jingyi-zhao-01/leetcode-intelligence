# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-range-ii
# source_path: LeetCode-Solutions-master/Python/smallest-range-ii.py
# solution_class: Solution
# submission_id: efa9dacfd1d67f18d381d392ff551d9e28485c01
# seed: 2350281170

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        result = A[-1]-A[0]
        for i in xrange(len(A)-1):
            result = min(result,
                         max(A[-1]-K, A[i]+K) -
                         min(A[0]+K, A[i+1]-K))
        return result